from flask import Flask, render_template, request, jsonify
import mysql.connector
import os
import uuid
import base64
import json
import anthropic
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

# ── DB CONFIG ─────────────────────────────────────────────────────────────────
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',          # change if your MySQL root has a password
    'database': 'smart_waste_db'
}

# ── WASTE CATEGORY METADATA ───────────────────────────────────────────────────
WASTE_CATEGORIES = {
    'Plastic':  {'suggestion': 'Rinse thoroughly and place in the yellow recycling bin.',                         'color': '#22c55e'},
    'Paper':    {'suggestion': 'Flatten and bundle with other paper. Place in the blue recycling bin.',           'color': '#3b82f6'},
    'Metal':    {'suggestion': 'Check for local scrap metal programs or drop at a recycling centre.',             'color': '#f59e0b'},
    'Organic':  {'suggestion': 'Compost at home or use the brown organic waste bin for garden fertiliser.',       'color': '#84cc16'},
    'Glass':    {'suggestion': 'Rinse and drop off at a glass collection bank. Do not mix colours.',              'color': '#06b6d4'},
}

# ── CLAUDE VISION CLASSIFICATION ─────────────────────────────────────────────
def classify_with_claude(image_path):
    """Send image to Claude Vision API and get real waste classification."""
    client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from environment

    ext = image_path.rsplit('.', 1)[-1].lower()
    mime_map = {
        'jpg':  'image/jpeg',
        'jpeg': 'image/jpeg',
        'png':  'image/png',
        'gif':  'image/gif',
        'webp': 'image/webp'
    }
    media_type = mime_map.get(ext, 'image/jpeg')

    with open(image_path, 'rb') as f:
        image_data = base64.standard_b64encode(f.read()).decode('utf-8')

    prompt = """You are a waste classification AI. Carefully look at this image and identify what material the waste item is made of.

Classify it into EXACTLY ONE of these 5 categories:
- Plastic  (bottles, bags, containers, packaging, plastic toys, synthetic items)
- Paper    (cardboard, newspaper, books, magazines, envelopes, paper bags, tissues)
- Metal    (iron, steel, aluminium cans, tins, foil, screws, tools, appliances, wires, rust)
- Organic  (food scraps, vegetables, fruit, leaves, wood, plant material, food waste)
- Glass    (glass bottles, jars, mirrors, windows, broken glass)

Respond with ONLY a valid JSON object, no explanation, no markdown:
{"category": "<one of the five categories above>", "confidence": <integer between 80 and 98>}"""

    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=100,
        messages=[{
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": media_type,
                        "data": image_data
                    }
                },
                {"type": "text", "text": prompt}
            ]
        }]
    )

    raw = message.content[0].text.strip()

    # Strip markdown code fences if present
    if '```' in raw:
        raw = raw.split('```')[1]
        if raw.startswith('json'):
            raw = raw[4:]
    raw = raw.strip()

    result = json.loads(raw)

    category = result.get('category', 'Plastic').strip().title()
    if category not in WASTE_CATEGORIES:
        category = 'Plastic'

    confidence = float(result.get('confidence', 88))
    confidence = round(min(max(confidence, 50.0), 99.0), 1)

    suggestion = WASTE_CATEGORIES[category]['suggestion']
    return category, confidence, suggestion


# ── HELPERS ───────────────────────────────────────────────────────────────────
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_db():
    return mysql.connector.connect(**DB_CONFIG)

def get_stats():
    db = get_db()
    cur = db.cursor(dictionary=True)
    cur.execute("SELECT COUNT(*) AS total FROM waste_logs")
    total = cur.fetchone()['total']
    cur.execute("SELECT AVG(confidence) AS avg_conf FROM waste_logs")
    avg_conf = round(cur.fetchone()['avg_conf'] or 0, 1)
    cur.execute("SELECT category, COUNT(*) AS cnt FROM waste_logs GROUP BY category ORDER BY cnt DESC LIMIT 1")
    row = cur.fetchone()
    most_common = row['category'] if row else 'N/A'
    db.close()
    carbon = round(total * 0.33, 1)
    return total, avg_conf, most_common, carbon


# ── ROUTES ────────────────────────────────────────────────────────────────────
@app.route('/')
def index():
    total, avg_conf, most_common, carbon = get_stats()
    return render_template('index.html', total=total, avg_conf=avg_conf,
                           most_common=most_common, carbon=carbon)

@app.route('/classify')
def classify():
    return render_template('classify.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    if not allowed_file(file.filename):
        return jsonify({'error': 'File type not allowed'}), 400

    filename  = str(uuid.uuid4()) + '_' + secure_filename(file.filename)
    save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(save_path)

    try:
        category, confidence, suggestion = classify_with_claude(save_path)
    except Exception as e:
        os.remove(save_path)
        return jsonify({'error': f'Classification failed: {str(e)}'}), 500

    image_url = '/' + save_path.replace('\\', '/')

    db = get_db()
    cur = db.cursor()
    cur.execute(
        "INSERT INTO waste_logs (image_path, category, confidence, suggestion) VALUES (%s,%s,%s,%s)",
        (image_url, category, confidence, suggestion)
    )
    db.commit()
    db.close()

    return jsonify({
        'category':   category,
        'confidence': confidence,
        'suggestion': suggestion,
        'image_url':  image_url,
        'color':      WASTE_CATEGORIES[category]['color']
    })

@app.route('/history')
def history():
    search     = request.args.get('search', '').strip()
    date_range = request.args.get('date_range', 'all')

    db  = get_db()
    cur = db.cursor(dictionary=True)

    cur.execute("SELECT COUNT(*) AS total FROM waste_logs")
    total = cur.fetchone()['total']
    cur.execute("SELECT AVG(confidence) AS avg_conf FROM waste_logs")
    avg_conf = round(cur.fetchone()['avg_conf'] or 0, 1)
    cur.execute("SELECT category, COUNT(*) AS cnt FROM waste_logs GROUP BY category ORDER BY cnt DESC LIMIT 1")
    row = cur.fetchone()
    most_common     = row['category'] if row else 'N/A'
    most_common_pct = round((row['cnt'] / total) * 100) if row and total else 0

    cur.execute("SELECT category, COUNT(*) AS cnt FROM waste_logs GROUP BY category")
    chart_rows   = cur.fetchall()
    chart_labels = [r['category'] for r in chart_rows]
    chart_values = [r['cnt'] for r in chart_rows]

    query  = "SELECT * FROM waste_logs WHERE 1=1"
    params = []
    if search:
        query  += " AND (category LIKE %s OR suggestion LIKE %s)"
        params += [f'%{search}%', f'%{search}%']
    if date_range == '7':
        query += " AND created_at >= DATE_SUB(NOW(), INTERVAL 7 DAY)"
    elif date_range == '30':
        query += " AND created_at >= DATE_SUB(NOW(), INTERVAL 30 DAY)"
    elif date_range == '90':
        query += " AND created_at >= DATE_SUB(NOW(), INTERVAL 90 DAY)"
    query += " ORDER BY created_at DESC"
    cur.execute(query, params)
    records = cur.fetchall()
    db.close()

    return render_template('history.html', records=records, total=total,
                           avg_conf=avg_conf, most_common=most_common,
                           most_common_pct=most_common_pct,
                           chart_labels=chart_labels, chart_values=chart_values,
                           search=search, date_range=date_range)

@app.route('/api/stats')
def api_stats():
    total, avg_conf, most_common, carbon = get_stats()
    return jsonify({'total': total, 'avg_conf': avg_conf,
                    'most_common': most_common, 'carbon': carbon})


if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
