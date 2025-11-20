const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

// Health check endpoint
app.get('/health', (req, res) => {
    res.status(200).json({ status: 'OK', service: 'nodejs' });
});

// Info endpoint
app.get('/info', (req, res) => {
    res.status(200).json({ 
        service: 'Signant Health Demo - Node.js Service',
        version: process.env.npm_package_version || '1.0.0',
        timestamp: new Date().toISOString()
    });
});

// Root endpoint
app.get('/', (req, res) => {
    res.status(200).json({ 
        message: 'Welcome to Signant Health Demo API',
        service: 'nodejs'
    });
});

app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});

module.exports = app;