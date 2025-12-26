#!/usr/bin/env python3
"""
Generate a static site from the chapters data.
All chapters become standalone HTML files.
Reading progress saved in localStorage.
"""
import json
import os
import shutil
from pathlib import Path

# Output directory
OUTPUT_DIR = Path('docs')  # GitHub Pages serves from /docs

def load_chapters():
    """Load chapters from JSON."""
    with open('chapters_data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def get_base_template():
    """Base HTML template."""
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="{css_path}">
</head>
<body>
    <header>
        <nav>
            <a href="{home_path}" class="logo">📖 Shadow Slave</a>
            <div class="nav-links">
                <a href="{chapters_path}">📚 Chapters</a>
                <a href="{login_path}">🔐 Login</a>
            </div>
        </nav>
    </header>
    <main>
        {content}
    </main>
    <script src="{js_path}"></script>
</body>
</html>'''

def get_css():
    """Main stylesheet."""
    return '''/* Shadow Slave Reader - Static Site */
:root {
    --primary: #00d4ff;
    --secondary: #7b2cbf;
    --dark-bg: #1a1a2e;
    --card-bg: #16213e;
    --text: #e0e0e0;
    --text-light: rgba(255, 255, 255, 0.6);
}

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
    background: linear-gradient(135deg, var(--dark-bg) 0%, var(--card-bg) 100%);
    color: var(--text);
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    line-height: 1.6;
    min-height: 100vh;
}

header {
    background: rgba(0, 0, 0, 0.3);
    backdrop-filter: blur(10px);
    padding: 1rem 2rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    position: sticky;
    top: 0;
    z-index: 100;
}

nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: 1200px;
    margin: 0 auto;
}

.logo {
    font-size: 1.5rem;
    font-weight: bold;
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-decoration: none;
}

.nav-links { display: flex; gap: 1.5rem; }
.nav-links a {
    color: var(--text);
    text-decoration: none;
    transition: color 0.3s;
}
.nav-links a:hover { color: var(--primary); }

main {
    max-width: 900px;
    margin: 0 auto;
    padding: 2rem;
}

a { color: var(--primary); text-decoration: none; }
a:hover { color: var(--secondary); }

/* Index page */
.hero {
    text-align: center;
    padding: 4rem 0;
}
.hero h1 {
    font-size: 3rem;
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 1rem;
}
.hero p { color: var(--text-light); font-size: 1.2rem; margin-bottom: 2rem; }

.btn {
    display: inline-block;
    padding: 1rem 2rem;
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    color: white;
    border-radius: 8px;
    font-weight: bold;
    font-size: 1.1rem;
    text-decoration: none;
    transition: transform 0.2s, box-shadow 0.2s;
}
.btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 30px rgba(0, 212, 255, 0.3);
    color: white;
}

.stats {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2rem;
    margin: 3rem 0;
}
.stat {
    background: rgba(255, 255, 255, 0.05);
    padding: 2rem;
    border-radius: 12px;
    text-align: center;
    border: 1px solid rgba(255, 255, 255, 0.1);
}
.stat-number {
    font-size: 2.5rem;
    font-weight: bold;
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.stat-label { color: var(--text-light); margin-top: 0.5rem; }

.resume-section {
    background: rgba(255, 255, 255, 0.05);
    padding: 2rem;
    border-radius: 12px;
    margin: 2rem 0;
    text-align: center;
    border: 1px solid rgba(255, 255, 255, 0.1);
    display: none;
}
.resume-section.visible { display: block; }
.resume-section h3 { margin-bottom: 1rem; color: var(--primary); }

/* Chapter reader */
.chapter-header {
    margin-bottom: 2rem;
    padding-bottom: 1rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}
.chapter-header h1 {
    font-size: 1.8rem;
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.chapter-meta {
    color: var(--text-light);
    font-size: 0.9rem;
    margin-top: 0.5rem;
}

.chapter-content {
    background: rgba(255, 255, 255, 0.03);
    padding: 2rem;
    border-radius: 12px;
    line-height: 1.9;
    font-size: 1.1rem;
}
.chapter-content p {
    margin-bottom: 1.5rem;
    text-align: justify;
}

.chapter-nav {
    display: flex;
    justify-content: space-between;
    margin-top: 2rem;
    padding-top: 2rem;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
}
.chapter-nav a {
    padding: 0.75rem 1.5rem;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 8px;
    transition: background 0.3s;
}
.chapter-nav a:hover { background: rgba(255, 255, 255, 0.2); }
.chapter-nav a.disabled {
    opacity: 0.3;
    pointer-events: none;
}

/* Chapter list */
.chapter-list-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2rem;
}
.chapter-list-header h1 {
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.search-box {
    padding: 0.75rem 1rem;
    background: rgba(255, 255, 255, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 8px;
    color: var(--text);
    width: 300px;
}
.search-box:focus {
    outline: none;
    border-color: var(--primary);
}

.chapters-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 1rem;
}
.chapter-card {
    background: rgba(255, 255, 255, 0.05);
    padding: 1rem 1.5rem;
    border-radius: 8px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    transition: all 0.3s;
    text-decoration: none;
    color: var(--text);
    display: block;
}
.chapter-card:hover {
    background: rgba(255, 255, 255, 0.1);
    border-color: var(--primary);
    transform: translateY(-2px);
}
.chapter-card.read {
    border-left: 3px solid var(--primary);
}
.chapter-number {
    color: var(--primary);
    font-weight: bold;
    font-size: 0.9rem;
}
.chapter-title {
    margin-top: 0.25rem;
    font-size: 0.95rem;
}

/* Login page */
.login-container {
    max-width: 400px;
    margin: 4rem auto;
    background: rgba(255, 255, 255, 0.05);
    padding: 3rem;
    border-radius: 16px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    text-align: center;
}
.login-container h1 {
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 1rem;
}
.login-container p {
    color: var(--text-light);
    margin-bottom: 2rem;
}
.login-info {
    background: rgba(0, 212, 255, 0.1);
    padding: 1.5rem;
    border-radius: 8px;
    margin-bottom: 2rem;
    border: 1px solid rgba(0, 212, 255, 0.2);
}
.login-info p { margin: 0; color: var(--text); }

.oauth-buttons { display: flex; flex-direction: column; gap: 1rem; }
.oauth-btn {
    padding: 1rem;
    border-radius: 8px;
    font-weight: bold;
    cursor: pointer;
    border: none;
    font-size: 1rem;
    transition: transform 0.2s;
    text-decoration: none;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
}
.oauth-btn:hover { transform: translateY(-2px); }
.oauth-btn.google { background: #4285f4; color: white; }
.oauth-btn.discord { background: #5865F2; color: white; }
.oauth-btn.local { background: rgba(255, 255, 255, 0.1); color: var(--text); }

/* Responsive */
@media (max-width: 768px) {
    .stats { grid-template-columns: 1fr; }
    .hero h1 { font-size: 2rem; }
    nav { flex-direction: column; gap: 1rem; }
    .search-box { width: 100%; }
    .chapter-list-header { flex-direction: column; gap: 1rem; }
}
'''

def get_js():
    """Main JavaScript for reading progress."""
    return '''// Shadow Slave Reader - Static Site JS

const Storage = {
    getProgress() {
        return JSON.parse(localStorage.getItem('readingProgress') || '{}');
    },
    saveProgress(chapterNum) {
        const progress = this.getProgress();
        progress.lastChapter = chapterNum;
        progress.readChapters = progress.readChapters || [];
        if (!progress.readChapters.includes(chapterNum)) {
            progress.readChapters.push(chapterNum);
        }
        progress.lastRead = new Date().toISOString();
        localStorage.setItem('readingProgress', JSON.stringify(progress));
    },
    getLastChapter() {
        return this.getProgress().lastChapter || null;
    },
    isRead(chapterNum) {
        const progress = this.getProgress();
        return (progress.readChapters || []).includes(chapterNum);
    },
    getReadCount() {
        return (this.getProgress().readChapters || []).length;
    }
};

// Save progress when reading a chapter
function initChapterPage() {
    const match = window.location.pathname.match(/chapters\\/([0-9]+)\\.html/);
    if (match) {
        const chapterNum = parseInt(match[1]);
        Storage.saveProgress(chapterNum);
    }
}

// Show resume button on index
function initIndexPage() {
    const lastChapter = Storage.getLastChapter();
    const resumeSection = document.getElementById('resume-section');
    if (lastChapter && resumeSection) {
        resumeSection.classList.add('visible');
        const link = resumeSection.querySelector('a');
        if (link) {
            link.href = `chapters/${lastChapter}.html`;
            link.textContent = `Continue Chapter ${lastChapter}`;
        }
        const readCount = document.getElementById('read-count');
        if (readCount) {
            readCount.textContent = Storage.getReadCount();
        }
    }
}

// Mark read chapters in list
function initChapterList() {
    document.querySelectorAll('.chapter-card').forEach(card => {
        const match = card.href.match(/chapters\\/([0-9]+)\\.html/);
        if (match) {
            const chapterNum = parseInt(match[1]);
            if (Storage.isRead(chapterNum)) {
                card.classList.add('read');
            }
        }
    });
    
    // Search functionality
    const searchBox = document.getElementById('chapter-search');
    if (searchBox) {
        searchBox.addEventListener('input', (e) => {
            const query = e.target.value.toLowerCase();
            document.querySelectorAll('.chapter-card').forEach(card => {
                const text = card.textContent.toLowerCase();
                card.style.display = text.includes(query) ? 'block' : 'none';
            });
        });
    }
}

// Keyboard navigation
document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight') {
        const next = document.querySelector('.chapter-nav a:last-child:not(.disabled)');
        if (next) next.click();
    } else if (e.key === 'ArrowLeft') {
        const prev = document.querySelector('.chapter-nav a:first-child:not(.disabled)');
        if (prev) prev.click();
    }
});

// Init based on page
document.addEventListener('DOMContentLoaded', () => {
    if (document.querySelector('.chapter-content')) {
        initChapterPage();
    } else if (document.querySelector('.hero')) {
        initIndexPage();
    } else if (document.querySelector('.chapters-grid')) {
        initChapterList();
    }
});
'''

def generate_index(data, total_chapters):
    """Generate index.html."""
    content = f'''
    <div class="hero">
        <h1>Shadow Slave</h1>
        <p>by {data['metadata']['author']}</p>
        <a href="chapters/1.html" class="btn">📖 Start Reading</a>
    </div>
    
    <div id="resume-section" class="resume-section">
        <h3>📚 Continue Reading</h3>
        <p>You've read <strong id="read-count">0</strong> chapters</p>
        <a href="#" class="btn">Continue Chapter 1</a>
    </div>
    
    <div class="stats">
        <div class="stat">
            <div class="stat-number">{total_chapters:,}</div>
            <div class="stat-label">Chapters</div>
        </div>
        <div class="stat">
            <div class="stat-number">~{total_chapters * 2000:,}</div>
            <div class="stat-label">Words</div>
        </div>
        <div class="stat">
            <div class="stat-number">~{total_chapters * 8:,}</div>
            <div class="stat-label">Minutes to Read</div>
        </div>
    </div>
    '''
    return content

def generate_chapter(chapter, prev_num, next_num, total):
    """Generate a single chapter page."""
    # Convert content to paragraphs
    paragraphs = chapter['content'].split('\n\n')
    content_html = '\n'.join(f'<p>{p.strip()}</p>' for p in paragraphs if p.strip())
    
    word_count = len(chapter['content'].split())
    reading_time = max(1, word_count // 250)
    
    prev_link = f'{prev_num}.html' if prev_num else '#'
    next_link = f'{next_num}.html' if next_num else '#'
    prev_class = '' if prev_num else 'disabled'
    next_class = '' if next_num else 'disabled'
    
    content = f'''
    <div class="chapter-header">
        <h1>{chapter['title']}</h1>
        <div class="chapter-meta">
            Chapter {chapter['chapter_number']} of {total} • {word_count:,} words • {reading_time} min read
        </div>
    </div>
    
    <div class="chapter-content">
        {content_html}
    </div>
    
    <div class="chapter-nav">
        <a href="{prev_link}" class="{prev_class}">← Previous</a>
        <a href="../chapter-list.html">📚 All Chapters</a>
        <a href="{next_link}" class="{next_class}">Next →</a>
    </div>
    '''
    return content

def generate_chapter_list(chapters):
    """Generate chapter list page."""
    cards = []
    for ch in chapters:
        cards.append(f'''
        <a href="chapters/{ch['chapter_number']}.html" class="chapter-card">
            <div class="chapter-number">Chapter {ch['chapter_number']}</div>
            <div class="chapter-title">{ch['title']}</div>
        </a>''')
    
    content = f'''
    <div class="chapter-list-header">
        <h1>📚 All Chapters</h1>
        <input type="text" id="chapter-search" class="search-box" placeholder="Search chapters...">
    </div>
    <div class="chapters-grid">
        {''.join(cards)}
    </div>
    '''
    return content

def generate_login():
    """Generate login page."""
    content = '''
    <div class="login-container">
        <h1>🔐 Login</h1>
        <p>Save your reading progress</p>
        
        <div class="login-info">
            <p>✨ <strong>Good news!</strong> Your reading progress is automatically saved in your browser!</p>
        </div>
        
        <div class="oauth-buttons">
            <button class="oauth-btn local" onclick="alert('Your progress is already being saved locally! Just keep reading.')">
                💾 Progress Saved Locally
            </button>
        </div>
        
        <p style="margin-top: 2rem; color: var(--text-light); font-size: 0.9rem;">
            Your reading progress is stored in your browser's local storage.
            No account needed!
        </p>
    </div>
    '''
    return content

def main():
    print("📚 Generating static site...")
    
    # Load data
    data = load_chapters()
    chapters = data['chapters']
    total = len(chapters)
    print(f"   Found {total} chapters")
    
    # Create output directories
    OUTPUT_DIR.mkdir(exist_ok=True)
    (OUTPUT_DIR / 'chapters').mkdir(exist_ok=True)
    (OUTPUT_DIR / 'css').mkdir(exist_ok=True)
    (OUTPUT_DIR / 'js').mkdir(exist_ok=True)
    
    # Write CSS and JS
    (OUTPUT_DIR / 'css' / 'style.css').write_text(get_css())
    (OUTPUT_DIR / 'js' / 'main.js').write_text(get_js())
    print("   ✓ CSS and JS")
    
    template = get_base_template()
    
    # Generate index
    index_html = template.format(
        title='Shadow Slave - Web Reader',
        css_path='css/style.css',
        js_path='js/main.js',
        home_path='index.html',
        chapters_path='chapter-list.html',
        login_path='login.html',
        content=generate_index(data, total)
    )
    (OUTPUT_DIR / 'index.html').write_text(index_html)
    print("   ✓ index.html")
    
    # Generate chapter list
    list_html = template.format(
        title='All Chapters - Shadow Slave',
        css_path='css/style.css',
        js_path='js/main.js',
        home_path='index.html',
        chapters_path='chapter-list.html',
        login_path='login.html',
        content=generate_chapter_list(chapters)
    )
    (OUTPUT_DIR / 'chapter-list.html').write_text(list_html)
    print("   ✓ chapter-list.html")
    
    # Generate login
    login_html = template.format(
        title='Login - Shadow Slave',
        css_path='css/style.css',
        js_path='js/main.js',
        home_path='index.html',
        chapters_path='chapter-list.html',
        login_path='login.html',
        content=generate_login()
    )
    (OUTPUT_DIR / 'login.html').write_text(login_html)
    print("   ✓ login.html")
    
    # Generate all chapters
    print(f"   Generating {total} chapter pages...")
    for i, chapter in enumerate(chapters):
        num = chapter['chapter_number']
        prev_num = num - 1 if num > 1 else None
        next_num = num + 1 if num < total else None
        
        chapter_html = template.format(
            title=f"{chapter['title']} - Shadow Slave",
            css_path='../css/style.css',
            js_path='../js/main.js',
            home_path='../index.html',
            chapters_path='../chapter-list.html',
            login_path='../login.html',
            content=generate_chapter(chapter, prev_num, next_num, total)
        )
        (OUTPUT_DIR / 'chapters' / f'{num}.html').write_text(chapter_html)
        
        if (i + 1) % 500 == 0:
            print(f"      {i + 1}/{total} chapters...")
    
    print(f"\n✅ Static site generated in '{OUTPUT_DIR}/'")
    print(f"   Total files: {total + 4} HTML + CSS + JS")
    print(f"\n🚀 To deploy on GitHub Pages:")
    print(f"   1. git add docs/")
    print(f"   2. git commit -m 'Generate static site'")
    print(f"   3. git push")
    print(f"   4. Go to repo Settings → Pages → Source: 'main' branch, '/docs' folder")

if __name__ == '__main__':
    main()
