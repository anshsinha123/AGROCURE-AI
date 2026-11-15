/**
 * AgroCure AI - Admin RBAC Middleware
 * Verifies JWT signature and extracts role ('Super Admin', 'Admin', 'Content Manager')
 */
const jwt = require('jsonwebtoken');
const crypto = require('crypto');

const configuredSecret = process.env.AGROCURE_ADMIN_SECRET;
const JWT_SECRET = configuredSecret || crypto.randomBytes(32).toString('hex');

if (!configuredSecret) {
  console.warn('[AgroCure AI] AGROCURE_ADMIN_SECRET is unset; admin tokens will expire after a server restart.');
}

const verifyAdminToken = (req, res, next) => {
  const authHeader = req.headers.authorization;
  if (!authHeader || !authHeader.startsWith('Bearer ')) {
    return res.status(401).json({ detail: 'Access denied: No authentication token provided.' });
  }

  const token = authHeader.split(' ')[1];
  try {
    const decoded = jwt.verify(token, JWT_SECRET);
    if (!['Super Admin', 'Admin', 'Content Manager'].includes(decoded.role)) {
      return res.status(403).json({ detail: 'Forbidden: Insufficient administrative privileges.' });
    }
    req.admin = decoded;
    next();
  } catch (err) {
    return res.status(401).json({ detail: 'Session expired or invalid token.' });
  }
};

const requireSuperAdmin = (req, res, next) => {
  if (req.admin && req.admin.role === 'Super Admin') {
    return next();
  }
  return res.status(403).json({ detail: 'Forbidden: Action requires Super Admin authority.' });
};

module.exports = { verifyAdminToken, requireSuperAdmin };
