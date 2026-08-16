# Smart Waste Classification System 🌿

A production-ready Flask + MySQL web app that uses simulated deep learning to classify waste images and provide eco-friendly disposal advice.

---

## 📁 Folder Structure

```
smart_waste/
├── app.py                  ← Flask application (all routes & logic)
├── requirements.txt        ← Python dependencies
├── database.sql            ← MySQL setup script
├── README.md
├── templates/
│   ├── base.html           ← Shared navbar + footer
│   ├── index.html          ← Home page
│   ├── classify.html       ← Classify Waste page
│   └── history.html        ← History / Dashboard page
└── static/
    ├── css/
    │   └── style.css       ← All styles (eco green theme)
    ├── js/
    │   └── script.js       ← Animations, counters
    └── uploads/            ← Uploaded images stored here (auto-created)
```

---

## 🛠 Prerequisites

| Tool | Version | Download |
|------|---------|----------|
| Python | 3.9 + | https://python.org |
| XAMPP  | 8.x   | https://apachefriends.org |
| VS Code | any  | https://code.visualstudio.com |

---

## ⚡ Step-by-Step Setup

### Step 1 — Start MySQL via XAMPP

1. Open **XAMPP Control Panel**
2. Click **Start** next to **MySQL** (Apache is not needed)
3. Click **Admin** next to MySQL → opens **phpMyAdmin** in your browser

### Step 2 — Create the Database

1. In phpMyAdmin click **SQL** tab
2. Copy-paste the entire contents of `database.sql`
3. Click **Go**
4. You should see database `smart_waste_db` appear in the left panel

### Step 3 — Open Project in VS Code

```bash
# In a terminal / VS Code terminal:
cd path/to/smart_waste
```

### Step 4 — Create a Python Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### Step 5 — Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6 — Configure Database Password (if needed)

Open `app.py` and find:

```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',          # ← put your MySQL root password here if set
    'database': 'smart_waste_db'
}
```

XAMPP MySQL default has **no password** — leave it as `''`.

---

## ▶ Run the Project

```bash
python app.py
```

Open your browser at: **http://127.0.0.1:5000**

---

## 🗺 Pages & Routes

| URL | Description |
|-----|-------------|
| `/` | Home — hero, stats, steps, technology |
| `/classify` | Upload an image → get AI prediction |
| `/upload` (POST) | API endpoint called by classify page |
| `/history` | Dashboard — chart, filters, records table |
| `/api/stats` | JSON stats endpoint |

---

## 🤖 ML Simulation

Since a real TensorFlow model is not bundled, predictions are **randomly simulated**:

```python
category   = random.choice(['Plastic','Paper','Metal','Organic','Glass'])
confidence = random.uniform(72, 99)
```

To plug in a real model, replace the `simulate_classification()` function in `app.py` with your TensorFlow/PyTorch inference code.

---

## 🖼 Image Upload

- Uploaded files are saved to `static/uploads/` with a UUID prefix
- Supported formats: JPG, PNG, WEBP, GIF
- Max size: 16 MB
- Paths are stored in MySQL and served statically by Flask

---

## 📊 Chart

The History page uses **Chart.js 4.x** (loaded from CDN) to render a bar chart of waste distribution by category.

---

## 🛑 Common Issues

| Problem | Fix |
|---------|-----|
| `mysql.connector.errors.DatabaseError` | Check XAMPP MySQL is running and password in `DB_CONFIG` is correct |
| `ModuleNotFoundError: flask` | Make sure venv is activated and `pip install -r requirements.txt` ran |
| Images not showing | Ensure `static/uploads/` folder exists (auto-created on run) |
| Port 5000 in use | Run `python app.py --port 5001` or kill the process using port 5000 |

---

## 🎨 Tech Stack

- **Backend**: Python 3 + Flask
- **Database**: MySQL via mysql-connector-python
- **Frontend**: Vanilla HTML / CSS / JavaScript
- **Fonts**: Syne (headings) + DM Sans (body) — Google Fonts
- **Charts**: Chart.js 4
- **ML**: Simulated (drop-in ready for TensorFlow/PyTorch)
