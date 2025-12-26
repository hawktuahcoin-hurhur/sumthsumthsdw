#!/bin/bash
# Quick start script for Novel Reader Web App

echo "🚀 Starting Novel Reader Web App"
echo ""
echo "📦 Installing dependencies..."
pip install -q Flask Flask-SQLAlchemy ebooklib beautifulsoup4 numpy textstat 2>/dev/null

echo "✅ Dependencies installed"
echo ""
echo "🌐 Starting web server..."
cd /workspaces/sumthsumthsdw
python run_web_app.py &
APP_PID=$!

sleep 3

echo "✅ Web app is running!"
echo ""
echo "📖 Access the app at: http://localhost:5000"
echo ""
echo "📥 Load novels with:"
echo "   curl 'http://localhost:5000/api/admin/load-epub?path=Shadow%20Slave%20Chapters%201%20-%202720.epub'"
echo ""
echo "API Endpoints:"
echo "  GET  /                          - Homepage"
echo "  GET  /api/novels                - List all novels"
echo "  GET  /novel/<id>                - View novel with chapters"
echo "  GET  /chapter/<id>              - Read chapter"
echo "  GET  /api/search?q=<query>      - Full-text search"
echo "  GET  /api/semantic-search?q=<query> - AI semantic search"
echo ""
echo "To stop the server: kill $APP_PID"
