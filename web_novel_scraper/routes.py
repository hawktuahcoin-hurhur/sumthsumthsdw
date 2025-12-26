"""
Flask routes for the novel reading web app.
"""
import os
import secrets
from datetime import datetime
from functools import wraps
from flask import render_template, request, jsonify, send_file, redirect, url_for, session
from web_novel_scraper.web_app import db, Novel, Chapter, Character
from web_novel_scraper.ai_features import ai_features
from web_novel_scraper.epub_extractor import calculate_word_count, estimate_reading_time
import json

try:
    import requests
except ImportError:
    requests = None


def get_oauth_config():
    """Get OAuth configuration from environment."""
    base_url = os.getenv('BASE_URL', 'http://localhost:5000')
    return {
        'google': {
            'client_id': os.getenv('GOOGLE_CLIENT_ID'),
            'client_secret': os.getenv('GOOGLE_CLIENT_SECRET'),
            'redirect_uri': f'{base_url}/auth/google/callback',
            'auth_url': 'https://accounts.google.com/o/oauth2/v2/auth',
            'token_url': 'https://oauth2.googleapis.com/token',
            'user_url': 'https://www.googleapis.com/oauth2/v2/userinfo',
        },
        'discord': {
            'client_id': os.getenv('DISCORD_CLIENT_ID'),
            'client_secret': os.getenv('DISCORD_CLIENT_SECRET'),
            'redirect_uri': f'{base_url}/auth/discord/callback',
            'auth_url': 'https://discord.com/api/oauth2/authorize',
            'token_url': 'https://discord.com/api/oauth2/token',
            'user_url': 'https://discord.com/api/users/@me',
        }
    }


def register_routes(app):
    """Register all Flask routes."""
    
    @app.route('/')
    def index():
        """Homepage - show main menu."""
        return render_template('index.html')
    
    @app.route('/login')
    def login_page():
        """Login page."""
        return render_template('login.html')
    
    @app.route('/auth/google')
    def google_login():
        """Initiate Google OAuth login."""
        config = get_oauth_config()['google']
        if not config['client_id']:
            return redirect('/login?error=Google+OAuth+not+configured')
        
        state = secrets.token_urlsafe(32)
        session['oauth_state'] = state
        
        params = {
            'client_id': config['client_id'],
            'redirect_uri': config['redirect_uri'],
            'response_type': 'code',
            'scope': 'openid profile email',
            'state': state,
        }
        auth_url = config['auth_url'] + '?' + '&'.join(f'{k}={v}' for k, v in params.items())
        return redirect(auth_url)
    
    @app.route('/auth/google/callback')
    def google_callback():
        """Handle Google OAuth callback."""
        if not requests:
            return redirect('/login?error=requests+module+not+installed')
        
        code = request.args.get('code')
        state = request.args.get('state')
        
        if not code or state != session.get('oauth_state'):
            return redirect('/login?error=Invalid+OAuth+state')
        
        config = get_oauth_config()['google']
        
        # Exchange code for token
        token_resp = requests.post(config['token_url'], data={
            'code': code,
            'client_id': config['client_id'],
            'client_secret': config['client_secret'],
            'redirect_uri': config['redirect_uri'],
            'grant_type': 'authorization_code',
        })
        
        if token_resp.status_code != 200:
            return redirect('/login?error=Token+exchange+failed')
        
        access_token = token_resp.json().get('access_token')
        
        # Get user info
        user_resp = requests.get(config['user_url'], headers={'Authorization': f'Bearer {access_token}'})
        if user_resp.status_code != 200:
            return redirect('/login?error=Failed+to+get+user+info')
        
        user_data = user_resp.json()
        session['user_id'] = user_data.get('id')
        session['username'] = user_data.get('name', 'User')
        session['email'] = user_data.get('email')
        session['avatar'] = user_data.get('picture')
        session['provider'] = 'google'
        
        return redirect('/chapter/1')
    
    @app.route('/auth/discord')
    def discord_login():
        """Initiate Discord OAuth login."""
        config = get_oauth_config()['discord']
        if not config['client_id']:
            return redirect('/login?error=Discord+OAuth+not+configured')
        
        state = secrets.token_urlsafe(32)
        session['oauth_state'] = state
        
        params = {
            'client_id': config['client_id'],
            'redirect_uri': config['redirect_uri'],
            'response_type': 'code',
            'scope': 'identify email',
            'state': state,
        }
        auth_url = config['auth_url'] + '?' + '&'.join(f'{k}={v}' for k, v in params.items())
        return redirect(auth_url)
    
    @app.route('/auth/discord/callback')
    def discord_callback():
        """Handle Discord OAuth callback."""
        if not requests:
            return redirect('/login?error=requests+module+not+installed')
        
        code = request.args.get('code')
        state = request.args.get('state')
        
        if not code or state != session.get('oauth_state'):
            return redirect('/login?error=Invalid+OAuth+state')
        
        config = get_oauth_config()['discord']
        
        # Exchange code for token
        token_resp = requests.post(config['token_url'], data={
            'code': code,
            'client_id': config['client_id'],
            'client_secret': config['client_secret'],
            'redirect_uri': config['redirect_uri'],
            'grant_type': 'authorization_code',
        })
        
        if token_resp.status_code != 200:
            return redirect('/login?error=Token+exchange+failed')
        
        access_token = token_resp.json().get('access_token')
        
        # Get user info
        user_resp = requests.get(config['user_url'], headers={'Authorization': f'Bearer {access_token}'})
        if user_resp.status_code != 200:
            return redirect('/login?error=Failed+to+get+user+info')
        
        user_data = user_resp.json()
        avatar_hash = user_data.get('avatar')
        avatar_url = f"https://cdn.discordapp.com/avatars/{user_data.get('id')}/{avatar_hash}.png" if avatar_hash else None
        
        session['user_id'] = user_data.get('id')
        session['username'] = user_data.get('username', 'User')
        session['email'] = user_data.get('email')
        session['avatar'] = avatar_url
        session['provider'] = 'discord'
        
        return redirect('/chapter/1')
    
    @app.route('/logout')
    def logout():
        """Logout user."""
        session.clear()
        return redirect('/')
    
    @app.route('/chapter-list')
    def chapter_list():
        """Show all chapters."""
        novel = Novel.query.first()
        if not novel:
            return redirect('/')
        chapters = Chapter.query.filter_by(novel_id=novel.id).order_by(Chapter.chapter_number).all()
        return render_template('chapter-list.html', chapters=[c.to_dict() for c in chapters])
    
    @app.route('/about')
    def about():
        """About page."""
        return render_template('about.html')
    
    @app.route('/api/novels')
    def api_novels():
        """API endpoint for novels list."""
        novels = Novel.query.all()
        return jsonify([n.to_dict() for n in novels])
    
    @app.route('/novel/<int:novel_id>')
    def novel_view(novel_id):
        """View novel with chapter list and info."""
        novel = Novel.query.get_or_404(novel_id)
        chapters = Chapter.query.filter_by(novel_id=novel_id).order_by(Chapter.chapter_number).all()
        characters = Character.query.filter_by(novel_id=novel_id).order_by(Character.mention_count.desc()).all()
        
        return render_template('novel.html',
                             novel=novel.to_dict(),
                             chapters=[c.to_dict() for c in chapters],
                             characters=[ch.to_dict() for ch in characters])
    
    @app.route('/api/novels/<int:novel_id>/chapters')
    def api_novel_chapters(novel_id):
        """Get chapters for a novel."""
        chapter_num = request.args.get('number')
        
        query = Chapter.query.filter_by(novel_id=novel_id)
        if chapter_num:
            chapter = query.filter_by(chapter_number=int(chapter_num)).first()
            if chapter:
                return jsonify(chapter.to_dict())
            return jsonify({'error': 'Chapter not found'}), 404
        
        chapters = query.order_by(Chapter.chapter_number).all()
        return jsonify([c.to_dict() for c in chapters])
    
    @app.route('/api/novel/<int:novel_id>')
    def api_novel(novel_id):
        """API endpoint for novel details."""
        novel = Novel.query.get_or_404(novel_id)
        chapters = Chapter.query.filter_by(novel_id=novel_id).order_by(Chapter.chapter_number).all()
        
        return jsonify({
            'novel': novel.to_dict(),
            'chapters': [c.to_dict() for c in chapters],
        })
    
    @app.route('/chapter/<int:chapter_id>')
    def read_chapter(chapter_id):
        """Read a specific chapter."""
        chapter = Chapter.query.get_or_404(chapter_id)
        novel = chapter.novel
        
        # Get adjacent chapters
        prev_chapter = Chapter.query.filter_by(
            novel_id=chapter.novel_id,
            chapter_number=chapter.chapter_number - 1
        ).first()
        next_chapter = Chapter.query.filter_by(
            novel_id=chapter.novel_id,
            chapter_number=chapter.chapter_number + 1
        ).first()
        
        # Get characters mentioned in this chapter
        characters = Character.query.filter_by(novel_id=chapter.novel_id).all()
        
        return render_template('reader.html',
                             chapter=chapter.to_dict(include_content=True),
                             novel=novel.to_dict(),
                             prev_chapter=prev_chapter.to_dict() if prev_chapter else None,
                             next_chapter=next_chapter.to_dict() if next_chapter else None,
                             characters=[c.to_dict() for c in characters])
    
    @app.route('/api/chapter/<int:chapter_id>')
    def api_chapter(chapter_id):
        """API endpoint for chapter details."""
        chapter = Chapter.query.get_or_404(chapter_id)
        return jsonify(chapter.to_dict(include_content=True))
    
    @app.route('/api/search')
    def api_search():
        """Search chapters by title or content."""
        query = request.args.get('q', '').lower()
        novel_id = request.args.get('novel_id')
        
        if not query:
            return jsonify([])
        
        q = Chapter.query
        if novel_id:
            q = q.filter_by(novel_id=novel_id)
        
        # Simple text search
        results = []
        for chapter in q.all():
            if (query in chapter.title.lower() or 
                query in chapter.content.lower()[:500]):  # Search first 500 chars
                results.append(chapter.to_dict())
        
        return jsonify(results[:50])  # Limit to 50 results
    
    @app.route('/api/semantic-search')
    def api_semantic_search():
        """Semantic search using embeddings."""
        query = request.args.get('q', '')
        novel_id = request.args.get('novel_id')
        
        if not query:
            return jsonify([])
        
        # Generate query embedding
        query_embedding = ai_features.generate_embeddings(query)
        if not query_embedding:
            return jsonify([])
        
        # Get chapters and embeddings
        q = Chapter.query
        if novel_id:
            q = q.filter_by(novel_id=novel_id)
        
        chapters = q.all()
        embeddings = []
        valid_chapters = []
        
        for chapter in chapters:
            if chapter.embedding:
                try:
                    emb = json.loads(chapter.embedding)
                    embeddings.append(emb)
                    valid_chapters.append(chapter)
                except:
                    pass
        
        if not embeddings:
            return jsonify([])
        
        # Find similar chapters
        similar_indices = ai_features.find_similar_chapters(query_embedding, embeddings, top_k=10)
        results = [valid_chapters[i].to_dict() for i in similar_indices if i < len(valid_chapters)]
        
        return jsonify(results)
    
    @app.route('/api/chapter/<int:chapter_id>/summary')
    def api_chapter_summary(chapter_id):
        """Get or generate chapter summary."""
        chapter = Chapter.query.get_or_404(chapter_id)
        
        if not chapter.summary:
            # Generate summary
            summary = ai_features.generate_summary(chapter.content[:2000])  # Limit text
            chapter.summary = summary
            db.session.commit()
        
        return jsonify({
            'chapter_id': chapter_id,
            'summary': chapter.summary,
        })
    
    @app.route('/api/novel/<int:novel_id>/characters')
    def api_novel_characters(novel_id):
        """Get characters in a novel."""
        characters = Character.query.filter_by(novel_id=novel_id).order_by(
            Character.mention_count.desc()
        ).all()
        
        return jsonify([c.to_dict() for c in characters])
    
    @app.route('/api/character/<int:character_id>')
    def api_character(character_id):
        """Get character details."""
        character = Character.query.get_or_404(character_id)
        return jsonify(character.to_dict())
    
    @app.route('/api/novel/<int:novel_id>/recommendations')
    def api_recommendations(novel_id):
        """Get recommended chapters based on novel content."""
        novel = Novel.query.get_or_404(novel_id)
        
        # Simple recommendation: highly-rated or most discussed chapters
        chapters = Chapter.query.filter_by(novel_id=novel_id).order_by(
            Chapter.chapter_number.desc()
        ).limit(10).all()
        
        return jsonify([c.to_dict() for c in chapters])
    
    @app.route('/api/admin/load-epub')
    def api_load_epub():
        """Admin endpoint to load EPUB into database."""
        from web_novel_scraper.epub_extractor import extract_epub_data
        import os
        
        epub_path = request.args.get('path', 'Shadow Slave Chapters 1 - 2720.epub')
        
        # Check if file exists in workspace
        if not os.path.exists(epub_path):
            epub_path = f'/workspaces/sumthsumthsdw/{epub_path}'
        
        if not os.path.exists(epub_path):
            return jsonify({'error': f'EPUB file not found: {epub_path}'}), 404
        
        try:
            data = extract_epub_data(epub_path)
            
            # Create or update novel
            novel = Novel.query.filter_by(title=data['metadata']['title']).first()
            if not novel:
                novel = Novel(
                    title=data['metadata']['title'],
                    author=data['metadata']['author'],
                    description=data['metadata']['description'],
                    language=data['metadata']['language'],
                    tags=json.dumps(data['metadata']['tags']),
                )
                db.session.add(novel)
                db.session.commit()
            
            # Add chapters
            for chapter_data in data['chapters']:
                existing = Chapter.query.filter_by(
                    novel_id=novel.id,
                    chapter_number=chapter_data['chapter_number']
                ).first()
                
                if not existing:
                    word_count = calculate_word_count(chapter_data['content'])
                    reading_time = estimate_reading_time(word_count)
                    
                    # Generate AI features
                    summary = ai_features.generate_summary(chapter_data['content'][:2000])
                    embedding = ai_features.generate_embeddings(chapter_data['content'][:500])
                    readability = ai_features.calculate_readability(chapter_data['content'])
                    characters = ai_features.extract_characters(chapter_data['content'])
                    
                    chapter = Chapter(
                        novel_id=novel.id,
                        chapter_number=chapter_data['chapter_number'],
                        title=chapter_data['title'],
                        content=chapter_data['content'],
                        raw_html=chapter_data.get('raw_html', ''),
                        word_count=word_count,
                        summary=summary,
                        readability_score=readability.get('flesch_kincaid_grade', 0),
                        reading_time_minutes=reading_time,
                        embedding=json.dumps(embedding) if embedding else None,
                        url=chapter_data.get('url', ''),
                    )
                    db.session.add(chapter)
                    db.session.commit()
                    
                    # Add/update characters
                    for char_name, char_data in characters.items():
                        character = Character.query.filter_by(
                            novel_id=novel.id,
                            name=char_name
                        ).first()
                        
                        if not character:
                            character = Character(
                                novel_id=novel.id,
                                name=char_name,
                                first_appearance_chapter=chapter.chapter_number,
                                mention_count=char_data.get('mention_count', 1),
                            )
                            db.session.add(character)
                        else:
                            character.mention_count += char_data.get('mention_count', 1)
                        
                        db.session.commit()
            
            return jsonify({
                'success': True,
                'novel_id': novel.id,
                'chapters_loaded': len(data['chapters']),
            })
        
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    @app.route('/health')
    def health():
        """Health check endpoint."""
        return jsonify({'status': 'healthy'})
