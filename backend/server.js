/**
 * AgroCure AI - Node.js / Express.js REST API Server.
 * Connects to MongoDB, manages file uploads via Multer,
 * and interfaces with the Python AI engine for MobileNetV2 / OpenCV inference.
 */

const express = require('express');
const cors = require('cors');
const multer = require('multer');
const path = require('path');
const fs = require('fs');
const { spawn } = require('child_process');
const mongoose = require('mongoose');

const Scan = require('./models/Scan');

const app = express();
const PORT = process.env.PORT || 5000;
const MONGODB_URI = process.env.MONGODB_URI || 'mongodb://127.0.0.1:27017/agrocure_ai';

app.use(cors());
app.use(express.json());
app.use('/static', express.static(path.join(__dirname, '..', 'static')));
app.use(express.static(path.join(__dirname, '..', 'frontend')));

// Upload configuration
const uploadDir = path.join(__dirname, '..', 'data', 'uploads');
if (!fs.existsSync(uploadDir)) {
  fs.mkdirSync(uploadDir, { recursive: true });
}

const storage = multer.diskStorage({
  destination: (req, file, cb) => cb(null, uploadDir),
  filename: (req, file, cb) => cb(null, `scan_${Date.now()}${path.extname(file.originalname)}`)
});
const upload = multer({ storage });

// MongoDB Connection
mongoose.connect(MONGODB_URI)
  .then(() => console.log('[AgroCure AI] Connected to MongoDB.'))
  .catch(err => console.warn('[AgroCure AI] MongoDB offline, falling back to in-memory/file logging:', err.message));

// Temporary in-memory scan history if MongoDB is not running locally
const memoryScans = [];

/**
 * Route: POST /api/scan
 * Accepts multipart image upload + optional crop_hint and lang
 */
app.post('/api/scan', upload.single('image'), async (req, res) => {
  if (!req.file) {
    return res.status(400).json({ error: 'No image uploaded' });
  }

  const imagePath = req.file.path;
  const cropHint = req.body.crop_hint || 'Auto-Detect';
  const lang = req.body.lang || 'en';

  // Execute Python AI Engine
  const pythonScript = path.join(__dirname, '..', 'ai_engine', 'inference.py');
  const pythonProc = spawn('python', [
    '-c',
    `
from PIL import Image
from ai_engine.inference import agrocure_ai_engine
import json

img = Image.open(r"${imagePath}")
res = agrocure_ai_engine.predict(img, crop_hint="${cropHint}", lang="${lang}")
print(json.dumps(res))
    `
  ], { cwd: path.join(__dirname, '..') });

  let stdoutData = '';
  let stderrData = '';

  pythonProc.stdout.on('data', chunk => stdoutData += chunk);
  pythonProc.stderr.on('data', chunk => stderrData += chunk);

  pythonProc.on('close', async (code) => {
    if (code !== 0) {
      console.error('Python error:', stderrData);
      return res.status(500).json({ error: 'AI inference failed', details: stderrData });
    }

    try {
      const result = JSON.parse(stdoutData.trim());

      // Save Scan to Database or Memory
      const scanRecord = {
        crop: result.prediction.crop,
        disease: result.prediction.disease,
        severity: result.prediction.severity,
        confidence: result.prediction.confidence,
        isHealthy: result.prediction.is_healthy,
        leafMetrics: {
          isLeafDetected: result.detection.is_leaf_detected,
          boundingBox: result.detection.bounding_box,
          leafCoveragePct: result.detection.leaf_coverage_pct,
          healthyGreenPct: result.detection.healthy_green_pct,
          lesionPct: result.detection.lesion_pct
        },
        treatment: result.treatment,
        language: lang,
        imageUrl: `/data/uploads/${path.basename(imagePath)}`,
        createdAt: new Date()
      };

      try {
        if (mongoose.connection.readyState === 1) {
          await Scan.create(scanRecord);
        } else {
          memoryScans.unshift(scanRecord);
        }
      } catch (dbErr) {
        console.warn('DB Save Error:', dbErr.message);
        memoryScans.unshift(scanRecord);
      }

      return res.json(result);
    } catch (parseErr) {
      return res.status(500).json({ error: 'Failed to parse AI output', raw: stdoutData });
    }
  });
});

/**
 * Route: GET /api/scans
 * Returns recent scan history
 */
app.get('/api/scans', async (req, res) => {
  try {
    if (mongoose.connection.readyState === 1) {
      const scans = await Scan.find().sort({ createdAt: -1 }).limit(20);
      return res.json(scans);
    }
    return res.json(memoryScans.slice(0, 20));
  } catch (err) {
    return res.json(memoryScans.slice(0, 20));
  }
});

/**
 * Route: GET /api/status
 */
app.get('/api/status', (req, res) => {
  res.json({
    project: 'AgroCure AI',
    status: 'online',
    supported_crops: ['Pepper', 'Grapes', 'Wheat', 'Corn'],
    supported_languages: ['en', 'hi', 'kn'],
    core_technologies: ['React.js', 'Node.js', 'Express.js', 'Python', 'MobileNetV2', 'OpenCV', 'MongoDB'],
    mongo_connected: mongoose.connection.readyState === 1
  });
});

app.listen(PORT, () => {
  console.log(`[AgroCure AI] Server listening on http://127.0.0.1:${PORT}`);
});
