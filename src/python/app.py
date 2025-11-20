from flask import Flask, jsonify
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'OK',
        'service': 'python'
    }), 200

@app.route('/info')
def info():
    """Service information endpoint"""
    return jsonify({
        'service': 'Signant Health Demo - Python Service',
        'version': '1.0.0',
        'timestamp': datetime.utcnow().isoformat() + 'Z'
    }), 200

@app.route('/')
def root():
    """Root endpoint"""
    return jsonify({
        'message': 'Welcome to Signant Health Demo API',
        'service': 'python'
    }), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)