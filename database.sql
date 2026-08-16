-- ═══════════════════════════════════════════════════════════════════════
--  SMART WASTE CLASSIFICATION SYSTEM  ·  database.sql
--  Run this in phpMyAdmin or MySQL Workbench
-- ═══════════════════════════════════════════════════════════════════════

-- 1. Create the database
CREATE DATABASE IF NOT EXISTS smart_waste_db
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE smart_waste_db;

-- 2. Main log table
CREATE TABLE IF NOT EXISTS waste_logs (
  id          INT UNSIGNED   NOT NULL AUTO_INCREMENT,
  image_path  VARCHAR(512)   NOT NULL,
  category    VARCHAR(50)    NOT NULL,
  confidence  DECIMAL(5,2)   NOT NULL,
  suggestion  TEXT           NOT NULL,
  created_at  DATETIME       NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  INDEX idx_category   (category),
  INDEX idx_created_at (created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 3. Optional: seed a few demo rows so History page isn't empty on first run
INSERT INTO waste_logs (image_path, category, confidence, suggestion, created_at) VALUES
  ('/static/uploads/demo1.jpg', 'Plastic',  91.5, 'Rinse thoroughly and place in the yellow recycling bin.',          '2023-11-24 14:30:00'),
  ('/static/uploads/demo2.jpg', 'Paper',    89.8, 'Flatten and bundle with other paper. Place in the blue recycling bin.', '2023-11-24 12:15:00'),
  ('/static/uploads/demo3.jpg', 'Metal',    90.2, 'Check for local scrap metal programs or drop at a recycling centre.',   '2023-11-23 16:45:00'),
  ('/static/uploads/demo4.jpg', 'Organic',  92.1, 'Compost at home or use the brown organic waste bin for garden fertiliser.','2023-11-23 09:30:00'),
  ('/static/uploads/demo5.jpg', 'Glass',    88.4, 'Rinse and drop off at a glass collection bank. Do not mix colours.',    '2023-11-22 18:20:00');
