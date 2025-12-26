"""
Flask web application for reading novels with AI features.
"""
import os
import sys
from pathlib import Path
from datetime import datetime
import json

# Suppress SQLAlchemy warnings
import warnings
warnings.filterwarnings('ignore')

from flask import Flask, render_template, request, jsonify

try:
    from flask_sqlalchemy import SQLAlchemy
    from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey, func
except ImportError:
    print("Installing database packages...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "flask-sqlalchemy"])
    from flask_sqlalchemy import SQLAlchemy
    from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey, func

# Initialize Flask app and database
db = SQLAlchemy()

class Novel(db.Model):
    """Novel metadata model."""
    __tablename__ = 'novels'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(512), unique=True, nullable=False, index=True)
    author = Column(String(256))
    description = Column(Text)
    language = Column(String(50))
    cover_image = Column(String(512))
    tags = Column(Text)  # JSON string of tags
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    chapters = db.relationship('Chapter', backref='novel', lazy=True, cascade='all, delete-orphan')
    characters = db.relationship('Character', backref='novel', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'description': self.description,
            'language': self.language,
            'cover_image': self.cover_image,
            'tags': json.loads(self.tags) if self.tags else [],
            'chapter_count': len(self.chapters),
            'created_at': self.created_at.isoformat(),
        }


class Chapter(db.Model):
    """Novel chapter model."""
    __tablename__ = 'chapters'
    
    id = Column(Integer, primary_key=True)
    novel_id = Column(Integer, ForeignKey('novels.id'), nullable=False, index=True)
    chapter_number = Column(Integer, nullable=False)
    title = Column(String(512), nullable=False)
    content = Column(Text, nullable=False)  # Cleaned HTML content
    raw_html = Column(Text)  # Original HTML
    word_count = Column(Integer)
    summary = Column(Text)  # AI-generated summary
    readability_score = Column(Float)  # Flesch-Kincaid score
    reading_time_minutes = Column(Integer)  # Estimated reading time
    embedding = Column(Text)  # JSON string of embedding vector
    url = Column(String(1024))  # Original chapter URL
    created_at = Column(DateTime, default=datetime.utcnow)
    
    def to_dict(self, include_content=False):
        data = {
            'id': self.id,
            'novel_id': self.novel_id,
            'chapter_number': self.chapter_number,
            'title': self.title,
            'word_count': self.word_count,
            'summary': self.summary,
            'readability_score': self.readability_score,
            'reading_time_minutes': self.reading_time_minutes,
        }
        if include_content:
            data['content'] = self.content
        return data


class Character(db.Model):
    """Character tracking model."""
    __tablename__ = 'characters'
    
    id = Column(Integer, primary_key=True)
    novel_id = Column(Integer, ForeignKey('novels.id'), nullable=False, index=True)
    name = Column(String(256), nullable=False)
    first_appearance_chapter = Column(Integer)
    mention_count = Column(Integer, default=0)
    description = Column(Text)  # AI-extracted description
    sentiment_score = Column(Float)  # Average sentiment towards character
    mentions = Column(Text)  # JSON list of chapter numbers where mentioned
    relationships = Column(Text)  # JSON dict of character relationships
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'first_appearance_chapter': self.first_appearance_chapter,
            'mention_count': self.mention_count,
            'description': self.description,
            'sentiment_score': self.sentiment_score,
            'mentions': json.loads(self.mentions) if self.mentions else [],
            'relationships': json.loads(self.relationships) if self.relationships else {},
        }


class UserProgress(db.Model):
    """User reading progress (optional, for future user accounts)."""
    __tablename__ = 'user_progress'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)  # Will be FK when user model added
    chapter_id = Column(Integer, ForeignKey('chapters.id'), nullable=False)
    last_read_position = Column(Float)  # 0.0 to 1.0
    is_completed = Column(Integer, default=0)  # 0/1 boolean
    bookmarked = Column(Integer, default=0)
    notes = Column(Text)
    last_read_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


def create_app(config=None):
    """Create and configure the Flask application."""
    app = Flask(__name__, 
                template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates'),
                static_folder=os.path.join(os.path.dirname(__file__), '..', 'static'))
    
    # Configuration
    if config is None:
        config = {
            'SQLALCHEMY_DATABASE_URI': 'sqlite:////tmp/novel_reader.db',
            'SQLALCHEMY_TRACK_MODIFICATIONS': False,
            'SECRET_KEY': os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production'),
        }
    
    app.config.update(config)
    
    # Initialize database with app
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
    
    # Register routes
    from . import routes
    routes.register_routes(app)
    
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
