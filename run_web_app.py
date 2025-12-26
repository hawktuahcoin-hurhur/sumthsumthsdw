"""
Entry point for the web novel reader application.
Loads pre-extracted chapter data for instant startup.
"""
import os
import sys
import json

# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

from web_novel_scraper.web_app import create_app

def load_chapters_from_json():
    """Load chapters from pre-extracted JSON file - instant loading."""
    from web_novel_scraper.web_app import db, Novel, Chapter
    from web_novel_scraper.epub_extractor import calculate_word_count, estimate_reading_time
    
    # Try multiple paths for chapters data
    possible_paths = [
        os.path.join(os.path.dirname(__file__), 'chapters_data.json'),
        '/workspaces/sumthsumthsdw/chapters_data.json',
        'chapters_data.json',
    ]
    
    json_path = None
    for path in possible_paths:
        if os.path.exists(path):
            json_path = path
            break
    
    if not json_path:
        print(f"⚠️  Chapters data not found: {json_path}")
        return
    
    # Check if already loaded
    existing = Novel.query.filter_by(title='Shadow Slave').first()
    if existing and existing.chapters.count() > 100:
        print(f"✅ Novel already loaded ({existing.chapters.count()} chapters)")
        return
    
    print(f"📚 Loading {json_path}...")
    try:
        with open(json_path, 'r') as f:
            data = json.load(f)
        
        # Create novel
        novel = Novel(
            title=data['metadata']['title'],
            author=data['metadata']['author'],
            description=data['metadata']['description'],
            language=data['metadata']['language'],
            tags=json.dumps(data['metadata']['tags']),
        )
        db.session.add(novel)
        db.session.commit()
        print(f"📖 Created: {novel.title}")
        
        # Batch load chapters
        batch_size = 200
        for idx, chapter_data in enumerate(data['chapters']):
            word_count = calculate_word_count(chapter_data['content'])
            reading_time = estimate_reading_time(word_count)
            
            chapter = Chapter(
                novel_id=novel.id,
                chapter_number=chapter_data['chapter_number'],
                title=chapter_data['title'],
                content=chapter_data['content'],
                raw_html=chapter_data.get('raw_html', ''),
                word_count=word_count,
                reading_time_minutes=reading_time,
                url=chapter_data.get('url', ''),
            )
            db.session.add(chapter)
            
            if (idx + 1) % batch_size == 0:
                db.session.commit()
                print(f"  ✓ {idx + 1}/{len(data['chapters'])} chapters...")
        
        db.session.commit()
        print(f"✅ Loaded {len(data['chapters'])} chapters!")
        print(f"🚀 Ready to read!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    # Create Flask app
    app = create_app({
        'SQLALCHEMY_DATABASE_URI': 'sqlite:////tmp/novel_reader.db',
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
        'SECRET_KEY': os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production'),
    })
    
    # Load chapters on startup (only if not already loaded)
    with app.app_context():
        from web_novel_scraper.web_app import Novel
        if Novel.query.count() == 0:
            load_chapters_from_json()
        else:
            print("✅ Chapters already loaded")
    
    print("\n🚀 Novel Reader running!")
    print("📖 http://localhost:5000\n")
    
    # Run WITHOUT debug mode for stability
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port, use_reloader=False)

# For Gunicorn - create app at module level
app = create_app({
    'SQLALCHEMY_DATABASE_URI': os.environ.get('DATABASE_URL', 'sqlite:////tmp/novel_reader.db'),
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    'SECRET_KEY': os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production'),
})

# Load chapters when app starts
with app.app_context():
    from web_novel_scraper.web_app import Novel
    if Novel.query.count() == 0:
        load_chapters_from_json()
