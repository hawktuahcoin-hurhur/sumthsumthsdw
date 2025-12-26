#!/usr/bin/env python3
"""
Generate a static site from the chapters data.
Features: AI Assistant, Comprehensive Wiki Sidebar that updates per chapter.
by Guiltythree
"""
import json
from pathlib import Path

OUTPUT_DIR = Path('docs')

def load_chapters():
    with open('chapters_data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def load_characters():
    with open('character_data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def get_css():
    return '''/* Shadow Slave Reader - by Guiltythree */
:root {
    --primary: #00d4ff;
    --secondary: #7b2cbf;
    --dark-bg: #1a1a2e;
    --card-bg: #16213e;
    --sidebar-bg: #0f1729;
    --text: #e0e0e0;
    --text-light: rgba(255, 255, 255, 0.6);
    --accent: #ff6b6b;
    --success: #4ade80;
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
    max-width: 1400px;
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

main.with-sidebar {
    max-width: 1400px;
    display: grid;
    grid-template-columns: 1fr 350px;
    gap: 2rem;
}

a { color: var(--primary); text-decoration: none; }
a:hover { color: var(--secondary); }

/* Hero */
.hero { text-align: center; padding: 4rem 0; }
.hero h1 {
    font-size: 3rem;
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.5rem;
}
.hero .author { color: var(--text-light); font-size: 1.2rem; margin-bottom: 2rem; }

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
    border: none;
    cursor: pointer;
}
.btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 30px rgba(0, 212, 255, 0.3);
    color: white;
}

.menu-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.menu-card {
    background: rgba(255, 255, 255, 0.05);
    padding: 2rem;
    border-radius: 12px;
    text-align: center;
    border: 1px solid rgba(255, 255, 255, 0.1);
    transition: all 0.3s;
    text-decoration: none;
    color: var(--text);
}
.menu-card:hover {
    background: rgba(255, 255, 255, 0.1);
    border-color: var(--primary);
    transform: translateY(-3px);
}
.menu-card .icon { font-size: 2.5rem; margin-bottom: 1rem; }
.menu-card h3 { margin-bottom: 0.5rem; color: var(--primary); }
.menu-card p { color: var(--text-light); font-size: 0.9rem; }

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
    background: rgba(0, 212, 255, 0.1);
    padding: 2rem;
    border-radius: 12px;
    margin: 2rem 0;
    text-align: center;
    border: 1px solid rgba(0, 212, 255, 0.2);
    display: none;
}
.resume-section.visible { display: block; }
.resume-section h3 { margin-bottom: 1rem; color: var(--primary); }

/* Chapter reader */
.chapter-container { flex: 1; }

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
.chapter-meta { color: var(--text-light); font-size: 0.9rem; margin-top: 0.5rem; }

.chapter-content {
    background: rgba(255, 255, 255, 0.03);
    padding: 2rem;
    border-radius: 12px;
    line-height: 1.9;
    font-size: 1.1rem;
}
.chapter-content p { margin-bottom: 1.5rem; text-align: justify; }

.chapter-nav {
    display: flex;
    justify-content: space-between;
    margin-top: 2rem;
    padding-top: 2rem;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    flex-wrap: wrap;
    gap: 1rem;
}
.chapter-nav a {
    padding: 0.75rem 1.5rem;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 8px;
    transition: background 0.3s;
}
.chapter-nav a:hover { background: rgba(255, 255, 255, 0.2); }
.chapter-nav a.disabled { opacity: 0.3; pointer-events: none; }

/* Chapter list */
.chapter-list-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2rem;
    flex-wrap: wrap;
    gap: 1rem;
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
    max-width: 100%;
}
.search-box:focus { outline: none; border-color: var(--primary); }

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
.chapter-card.read { border-left: 3px solid var(--primary); }
.chapter-number { color: var(--primary); font-weight: bold; font-size: 0.9rem; }
.chapter-title { margin-top: 0.25rem; font-size: 0.95rem; }

/* Wiki Sidebar */
.wiki-sidebar {
    background: var(--sidebar-bg);
    border-radius: 12px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    height: fit-content;
    position: sticky;
    top: 80px;
    max-height: calc(100vh - 100px);
    overflow: hidden;
    display: flex;
    flex-direction: column;
}

.wiki-sidebar-header {
    padding: 1rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    background: rgba(0, 0, 0, 0.2);
}
.wiki-sidebar-header h3 {
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 1.1rem;
    margin-bottom: 0.25rem;
}
.wiki-sidebar-header p {
    font-size: 0.8rem;
    color: var(--text-light);
}

.wiki-tabs {
    display: flex;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    background: rgba(0, 0, 0, 0.1);
}
.wiki-tab {
    flex: 1;
    padding: 0.6rem 0.3rem;
    background: transparent;
    border: none;
    color: var(--text-light);
    cursor: pointer;
    font-size: 0.75rem;
    transition: all 0.3s;
    border-bottom: 2px solid transparent;
}
.wiki-tab:hover { color: var(--text); background: rgba(255, 255, 255, 0.05); }
.wiki-tab.active { 
    color: var(--primary); 
    border-bottom-color: var(--primary);
    background: rgba(0, 212, 255, 0.1);
}

.wiki-content {
    flex: 1;
    overflow-y: auto;
    padding: 0.75rem;
}

.wiki-section { display: none; }
.wiki-section.active { display: block; }

.wiki-item {
    background: rgba(255, 255, 255, 0.03);
    padding: 0.75rem;
    border-radius: 8px;
    margin-bottom: 0.5rem;
    border-left: 3px solid var(--secondary);
    transition: all 0.3s;
}
.wiki-item:hover {
    background: rgba(255, 255, 255, 0.08);
    border-left-color: var(--primary);
}
.wiki-item.new-this-chapter {
    border-left-color: var(--success);
    background: rgba(74, 222, 128, 0.1);
}
.wiki-item h4 {
    color: var(--primary);
    font-size: 0.9rem;
    margin-bottom: 0.25rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.wiki-item .badge {
    font-size: 0.65rem;
    padding: 0.15rem 0.4rem;
    border-radius: 4px;
    background: var(--secondary);
    color: white;
}
.wiki-item .badge.new { background: var(--success); }
.wiki-item .aliases {
    font-size: 0.75rem;
    color: var(--text-light);
    margin-bottom: 0.25rem;
}
.wiki-item .description {
    font-size: 0.8rem;
    line-height: 1.4;
}
.wiki-item .meta {
    font-size: 0.7rem;
    color: var(--text-light);
    margin-top: 0.5rem;
    display: flex;
    gap: 0.5rem;
    flex-wrap: wrap;
}
.wiki-item .meta span {
    background: rgba(255, 255, 255, 0.1);
    padding: 0.1rem 0.3rem;
    border-radius: 3px;
}

.wiki-empty {
    text-align: center;
    color: var(--text-light);
    padding: 2rem 1rem;
    font-size: 0.9rem;
}

.wiki-toggle {
    display: none;
    position: fixed;
    bottom: 20px;
    left: 20px;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    background: linear-gradient(135deg, var(--secondary), var(--primary));
    border: none;
    cursor: pointer;
    font-size: 1.2rem;
    box-shadow: 0 4px 20px rgba(123, 44, 191, 0.4);
    z-index: 1000;
}

/* AI Chat Widget */
.ai-chat-widget {
    position: fixed;
    bottom: 20px;
    right: 20px;
    z-index: 1000;
}

.ai-chat-button {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    border: none;
    cursor: pointer;
    font-size: 1.5rem;
    box-shadow: 0 4px 20px rgba(0, 212, 255, 0.4);
    transition: transform 0.3s;
}
.ai-chat-button:hover { transform: scale(1.1); }

.ai-chat-panel {
    position: fixed;
    bottom: 90px;
    right: 20px;
    width: 380px;
    max-width: calc(100vw - 40px);
    height: 500px;
    max-height: 70vh;
    background: var(--card-bg);
    border-radius: 16px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    display: none;
    flex-direction: column;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
}
.ai-chat-panel.open { display: flex; }

.ai-chat-header {
    padding: 1rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.ai-chat-header h3 {
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.ai-chat-close {
    background: none;
    border: none;
    color: var(--text);
    font-size: 1.5rem;
    cursor: pointer;
}

.ai-chat-messages {
    flex: 1;
    overflow-y: auto;
    padding: 1rem;
    display: flex;
    flex-direction: column;
    gap: 1rem;
}
.ai-message {
    max-width: 85%;
    padding: 0.75rem 1rem;
    border-radius: 12px;
    font-size: 0.95rem;
}
.ai-message.bot {
    background: rgba(255, 255, 255, 0.1);
    align-self: flex-start;
    border-bottom-left-radius: 4px;
}
.ai-message.user {
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    align-self: flex-end;
    border-bottom-right-radius: 4px;
}

.ai-chat-input {
    padding: 1rem;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    display: flex;
    gap: 0.5rem;
}
.ai-chat-input input {
    flex: 1;
    padding: 0.75rem;
    background: rgba(255, 255, 255, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 8px;
    color: var(--text);
}
.ai-chat-input input:focus { outline: none; border-color: var(--primary); }
.ai-chat-input button {
    padding: 0.75rem 1rem;
    background: var(--primary);
    border: none;
    border-radius: 8px;
    color: white;
    cursor: pointer;
}

/* Login */
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
.login-info {
    background: rgba(0, 212, 255, 0.1);
    padding: 1.5rem;
    border-radius: 8px;
    margin: 2rem 0;
    border: 1px solid rgba(0, 212, 255, 0.2);
}

/* Responsive */
@media (max-width: 1024px) {
    main.with-sidebar {
        grid-template-columns: 1fr;
    }
    .wiki-sidebar {
        display: none;
        position: fixed;
        top: 60px;
        left: 0;
        right: 0;
        bottom: 0;
        max-height: none;
        border-radius: 0;
        z-index: 99;
    }
    .wiki-sidebar.mobile-open { display: flex; }
    .wiki-toggle { display: block; }
}

@media (max-width: 768px) {
    .stats { grid-template-columns: 1fr; }
    .hero h1 { font-size: 2rem; }
    nav { flex-direction: column; gap: 1rem; }
    .search-box { width: 100%; }
    .chapter-list-header { flex-direction: column; }
    .menu-grid { grid-template-columns: 1fr; }
    .ai-chat-panel { width: calc(100vw - 40px); }
}
'''

def get_wiki_data_js(char_data):
    """Generate JavaScript object with all wiki data."""
    return f'''const WIKI_DATA = {json.dumps(char_data, indent=2)};'''

def get_js(char_data):
    wiki_data = get_wiki_data_js(char_data)
    return f'''// Shadow Slave Reader - by Guiltythree
// With AI Assistant and Comprehensive Wiki Sidebar

{wiki_data}

const Storage = {{
    getProgress() {{ return JSON.parse(localStorage.getItem('readingProgress') || '{{}}'); }},
    saveProgress(chapterNum) {{
        const progress = this.getProgress();
        progress.lastChapter = chapterNum;
        progress.readChapters = progress.readChapters || [];
        if (!progress.readChapters.includes(chapterNum)) {{
            progress.readChapters.push(chapterNum);
        }}
        progress.lastRead = new Date().toISOString();
        localStorage.setItem('readingProgress', JSON.stringify(progress));
    }},
    getLastChapter() {{ return this.getProgress().lastChapter || null; }},
    isRead(chapterNum) {{ return (this.getProgress().readChapters || []).includes(chapterNum); }},
    getReadCount() {{ return (this.getProgress().readChapters || []).length; }},
    getMaxChapterRead() {{
        const chapters = this.getProgress().readChapters || [];
        return chapters.length > 0 ? Math.max(...chapters) : 0;
    }}
}};

// Wiki Sidebar
const WikiSidebar = {{
    currentChapter: 1,
    
    init(chapterNum) {{
        this.currentChapter = chapterNum;
        this.render();
        this.initTabs();
        this.initMobileToggle();
    }},
    
    render() {{
        this.renderSection('characters', WIKI_DATA.characters, 'characters-list');
        this.renderSection('terms', WIKI_DATA.terms, 'terms-list');
        this.renderSection('locations', WIKI_DATA.locations, 'locations-list');
        this.renderSection('events', WIKI_DATA.events, 'events-list');
    }},
    
    renderSection(type, items, containerId) {{
        const container = document.getElementById(containerId);
        if (!container) return;
        
        const visible = items.filter(item => item.first_appearance <= this.currentChapter);
        visible.sort((a, b) => b.first_appearance - a.first_appearance);
        
        if (visible.length === 0) {{
            container.innerHTML = '<div class="wiki-empty">Nothing discovered yet in this chapter</div>';
            return;
        }}
        
        container.innerHTML = visible.map(item => {{
            const isNew = item.first_appearance === this.currentChapter;
            const newBadge = isNew ? '<span class="badge new">NEW!</span>' : '';
            const typeBadge = item.type ? `<span class="badge">${{item.type}}</span>` : '';
            const categoryBadge = item.category ? `<span class="badge">${{item.category}}</span>` : '';
            
            let aliases = '';
            if (item.aliases && item.aliases.length > 0) {{
                aliases = `<div class="aliases">AKA: ${{item.aliases.join(', ')}}</div>`;
            }}
            
            let meta = [];
            if (item.rank) meta.push(`<span>Rank: ${{item.rank}}</span>`);
            if (item.aspect && item.aspect !== 'N/A') meta.push(`<span>Aspect: ${{item.aspect}}</span>`);
            if (item.clan && item.clan !== 'N/A' && item.clan !== 'None') meta.push(`<span>Clan: ${{item.clan}}</span>`);
            meta.push(`<span>Ch.${{item.first_appearance}}</span>`);
            
            const metaHtml = meta.length > 0 ? `<div class="meta">${{meta.join('')}}</div>` : '';
            
            return `
                <div class="wiki-item ${{isNew ? 'new-this-chapter' : ''}}">
                    <h4>${{item.name}} ${{newBadge || typeBadge || categoryBadge}}</h4>
                    ${{aliases}}
                    <div class="description">${{item.description}}</div>
                    ${{metaHtml}}
                </div>
            `;
        }}).join('');
        
        // Update tab count
        const tab = document.querySelector(`[data-tab="${{type}}"]`);
        if (tab) {{
            const newCount = visible.filter(i => i.first_appearance === this.currentChapter).length;
            const newIndicator = newCount > 0 ? ` (${{newCount}} new)` : '';
            tab.dataset.count = visible.length;
        }}
    }},
    
    initTabs() {{
        const tabs = document.querySelectorAll('.wiki-tab');
        const sections = document.querySelectorAll('.wiki-section');
        
        tabs.forEach(tab => {{
            tab.addEventListener('click', () => {{
                tabs.forEach(t => t.classList.remove('active'));
                sections.forEach(s => s.classList.remove('active'));
                
                tab.classList.add('active');
                const target = tab.dataset.tab;
                document.getElementById(`${{target}}-section`)?.classList.add('active');
            }});
        }});
    }},
    
    initMobileToggle() {{
        const toggle = document.querySelector('.wiki-toggle');
        const sidebar = document.querySelector('.wiki-sidebar');
        
        if (toggle && sidebar) {{
            toggle.addEventListener('click', () => {{
                sidebar.classList.toggle('mobile-open');
                toggle.textContent = sidebar.classList.contains('mobile-open') ? '✕' : '📖';
            }});
        }}
    }}
}};

// AI Assistant
const AIAssistant = {{
    responses: {{
        greetings: [
            "Hello, Sleeper! How can I help you on your journey through the Dream Realm?",
            "Greetings! I'm your guide through Shadow Slave. Ask me anything!",
            "Welcome back! Ready to continue the adventure?"
        ],
        sunny: "Sunny (Sunless) is the protagonist - an orphan from the outskirts who becomes an Awakened. His Aspect is Shadow, allowing him to control shadows and eventually become the 'Lord Shadow'. He's known for his cunning mind and dark humor.",
        nephis: "Nephis (Changing Star) is a brilliant Legacy from Clan Valor. She possesses an inner fire that literally burns within her. She's one of the most powerful Awakened of her generation.",
        cassie: "Cassie is a blind prophet who can see visions of the future. Despite her gentle nature, her prophecies are incredibly accurate and sometimes terrifying.",
        nightmare: "The Nightmare Spell is the mysterious force that brought the Dream Realm to Earth. It grants humans the chance to become Awakened through surviving Nightmares.",
        awakened: "Awakened are humans who survived their First Nightmare and gained supernatural powers called Aspects. They rank from Sleeper → Awakened → Ascended → Master → Saint → Sovereign.",
        aspect: "An Aspect is the unique supernatural ability granted to someone after becoming Awakened. Each Aspect comes with a Flaw - a weakness or curse.",
        shadow: "Sunny's shadow is sentient and has its own personality. It's one of the most mysterious elements of his power.",
        progress: () => {{
            const last = Storage.getLastChapter();
            const count = Storage.getReadCount();
            return last ? `You've read ${{count}} chapters so far. You were last on Chapter ${{last}}. Keep going!` : "You haven't started reading yet. Begin with Chapter 1!";
        }},
        wiki: "Check the Wiki sidebar on the right! It shows characters, terms, locations, and events that have appeared up to your current chapter.",
        help: "I can help with: character info, world terms, your progress, navigation. Try asking about Sunny, Nephis, the Nightmare Spell, or your reading progress!",
        unknown: [
            "I'm not sure about that. Try asking about specific characters or concepts!",
            "That's beyond my knowledge. Ask me about characters, the Nightmare Spell, or Aspects!",
            "Hmm, I don't have info on that. Want to know about the main characters?"
        ]
    }},
    
    processQuery(query) {{
        const q = query.toLowerCase();
        
        if (q.match(/hello|hi|hey|greet/)) return this.random(this.responses.greetings);
        if (q.match(/sunny|sunless|protagonist|main character|lord shadow/)) return this.responses.sunny;
        if (q.match(/nephis|neph|changing star|valor/)) return this.responses.nephis;
        if (q.match(/cassie|cassia|blind|oracle|prophet/)) return this.responses.cassie;
        if (q.match(/nightmare spell|spell|dream realm|world/)) return this.responses.nightmare;
        if (q.match(/awakened|sleeper|master|saint|rank/)) return this.responses.awakened;
        if (q.match(/aspect|flaw|power|ability/)) return this.responses.aspect;
        if (q.match(/shadow|sentient shadow/)) return this.responses.shadow;
        if (q.match(/progress|reading|chapter|where|last/)) return this.responses.progress();
        if (q.match(/wiki|character|spoiler/)) return this.responses.wiki;
        if (q.match(/help|what can|how to/)) return this.responses.help;
        
        return this.random(this.responses.unknown);
    }},
    
    random(arr) {{ return arr[Math.floor(Math.random() * arr.length)]; }}
}};

// Initialize chat
function initChat() {{
    const btn = document.querySelector('.ai-chat-button');
    const panel = document.querySelector('.ai-chat-panel');
    const closeBtn = document.querySelector('.ai-chat-close');
    const input = document.querySelector('.ai-chat-input input');
    const sendBtn = document.querySelector('.ai-chat-input button');
    const messages = document.querySelector('.ai-chat-messages');
    
    if (!btn) return;
    
    btn.onclick = () => panel.classList.toggle('open');
    closeBtn.onclick = () => panel.classList.remove('open');
    
    function sendMessage() {{
        const text = input.value.trim();
        if (!text) return;
        
        const userMsg = document.createElement('div');
        userMsg.className = 'ai-message user';
        userMsg.textContent = text;
        messages.appendChild(userMsg);
        
        input.value = '';
        
        setTimeout(() => {{
            const botMsg = document.createElement('div');
            botMsg.className = 'ai-message bot';
            botMsg.textContent = AIAssistant.processQuery(text);
            messages.appendChild(botMsg);
            messages.scrollTop = messages.scrollHeight;
        }}, 500);
        
        messages.scrollTop = messages.scrollHeight;
    }}
    
    sendBtn.onclick = sendMessage;
    input.onkeypress = (e) => {{ if (e.key === 'Enter') sendMessage(); }};
    
    const greeting = document.createElement('div');
    greeting.className = 'ai-message bot';
    greeting.textContent = "Hello! I'm your Shadow Slave guide. Ask me about characters, concepts, or your reading progress!";
    messages.appendChild(greeting);
}}

// Chapter page
function initChapterPage() {{
    const match = window.location.pathname.match(/chapters\\/([0-9]+)\\.html/);
    if (match) {{
        const chapterNum = parseInt(match[1]);
        Storage.saveProgress(chapterNum);
        WikiSidebar.init(chapterNum);
    }}
}}

// Index page
function initIndexPage() {{
    const lastChapter = Storage.getLastChapter();
    const resumeSection = document.getElementById('resume-section');
    if (lastChapter && resumeSection) {{
        resumeSection.classList.add('visible');
        const link = resumeSection.querySelector('a');
        if (link) {{
            link.href = `chapters/${{lastChapter}}.html`;
            link.textContent = `Continue Chapter ${{lastChapter}}`;
        }}
        const readCount = document.getElementById('read-count');
        if (readCount) readCount.textContent = Storage.getReadCount();
    }}
}}

// Chapter list
function initChapterList() {{
    document.querySelectorAll('.chapter-card').forEach(card => {{
        const match = card.href.match(/chapters\\/([0-9]+)\\.html/);
        if (match && Storage.isRead(parseInt(match[1]))) {{
            card.classList.add('read');
        }}
    }});
    
    const searchBox = document.getElementById('chapter-search');
    if (searchBox) {{
        searchBox.addEventListener('input', (e) => {{
            const query = e.target.value.toLowerCase();
            document.querySelectorAll('.chapter-card').forEach(card => {{
                card.style.display = card.textContent.toLowerCase().includes(query) ? 'block' : 'none';
            }});
        }});
    }}
}}

// Keyboard navigation
document.addEventListener('keydown', (e) => {{
    if (e.key === 'ArrowRight') {{
        const next = document.querySelector('.chapter-nav a:last-child:not(.disabled)');
        if (next) next.click();
    }} else if (e.key === 'ArrowLeft') {{
        const prev = document.querySelector('.chapter-nav a:first-child:not(.disabled)');
        if (prev) prev.click();
    }}
}});

// Init
document.addEventListener('DOMContentLoaded', () => {{
    initChat();
    
    if (document.querySelector('.chapter-content')) initChapterPage();
    else if (document.querySelector('.hero')) initIndexPage();
    else if (document.querySelector('.chapters-grid')) initChapterList();
}});
'''

def get_chat_widget():
    return '''
    <div class="ai-chat-widget">
        <button class="ai-chat-button" title="AI Assistant">🤖</button>
        <div class="ai-chat-panel">
            <div class="ai-chat-header">
                <h3>🤖 Shadow Slave Guide</h3>
                <button class="ai-chat-close">&times;</button>
            </div>
            <div class="ai-chat-messages"></div>
            <div class="ai-chat-input">
                <input type="text" placeholder="Ask about characters, terms...">
                <button>Send</button>
            </div>
        </div>
    </div>'''

def get_wiki_sidebar():
    return '''
    <aside class="wiki-sidebar">
        <div class="wiki-sidebar-header">
            <h3>📖 Wiki</h3>
            <p>Spoiler-free up to current chapter</p>
        </div>
        <div class="wiki-tabs">
            <button class="wiki-tab active" data-tab="characters">👤 Characters</button>
            <button class="wiki-tab" data-tab="terms">📚 Terms</button>
            <button class="wiki-tab" data-tab="locations">🗺️ Places</button>
            <button class="wiki-tab" data-tab="events">⚔️ Events</button>
        </div>
        <div class="wiki-content">
            <div id="characters-section" class="wiki-section active">
                <div id="characters-list"></div>
            </div>
            <div id="terms-section" class="wiki-section">
                <div id="terms-list"></div>
            </div>
            <div id="locations-section" class="wiki-section">
                <div id="locations-list"></div>
            </div>
            <div id="events-section" class="wiki-section">
                <div id="events-list"></div>
            </div>
        </div>
    </aside>
    <button class="wiki-toggle">📖</button>'''

def get_base_template():
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
                <a href="{login_path}">💾 Save</a>
            </div>
        </nav>
    </header>
    <main{main_class}>
        {content}
    </main>
    {chat_widget}
    <script src="{js_path}"></script>
</body>
</html>'''

def generate_index(total_chapters):
    return f'''
    <div class="hero">
        <h1>Shadow Slave</h1>
        <p class="author">by Guiltythree</p>
        <a href="chapters/1.html" class="btn">📖 Start Reading</a>
    </div>
    
    <div id="resume-section" class="resume-section">
        <h3>📚 Continue Reading</h3>
        <p>You've read <strong id="read-count">0</strong> chapters</p>
        <a href="#" class="btn">Continue Chapter 1</a>
    </div>
    
    <div class="menu-grid">
        <a href="chapter-list.html" class="menu-card">
            <div class="icon">📚</div>
            <h3>All Chapters</h3>
            <p>Browse {total_chapters:,} chapters</p>
        </a>
        <a href="chapters/1.html" class="menu-card">
            <div class="icon">📖</div>
            <h3>Read with Wiki</h3>
            <p>Sidebar updates per chapter</p>
        </a>
        <a href="login.html" class="menu-card">
            <div class="icon">💾</div>
            <h3>Save Progress</h3>
            <p>Your progress is auto-saved</p>
        </a>
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

def generate_chapter(chapter, prev_num, next_num, total):
    paragraphs = chapter['content'].split('\n\n')
    content_html = '\n'.join(f'<p>{p.strip()}</p>' for p in paragraphs if p.strip())
    
    word_count = len(chapter['content'].split())
    reading_time = max(1, word_count // 250)
    
    prev_link = f'{prev_num}.html' if prev_num else '#'
    next_link = f'{next_num}.html' if next_num else '#'
    prev_class = '' if prev_num else 'disabled'
    next_class = '' if next_num else 'disabled'
    
    wiki = get_wiki_sidebar()
    
    return f'''
    <div class="chapter-container">
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
    </div>
    {wiki}
    '''

def generate_chapter_list(chapters):
    cards = []
    for ch in chapters:
        cards.append(f'''
        <a href="chapters/{ch['chapter_number']}.html" class="chapter-card">
            <div class="chapter-number">Chapter {ch['chapter_number']}</div>
            <div class="chapter-title">{ch['title']}</div>
        </a>''')
    
    return f'''
    <div class="chapter-list-header">
        <h1>📚 All Chapters</h1>
        <input type="text" id="chapter-search" class="search-box" placeholder="Search chapters...">
    </div>
    <div class="chapters-grid">
        {''.join(cards)}
    </div>
    '''

def generate_login():
    return '''
    <div class="login-container">
        <h1>💾 Save Progress</h1>
        <p>Your reading progress is automatically saved!</p>
        
        <div class="login-info">
            <p>✨ <strong>Good news!</strong> Your reading progress is stored locally in your browser.</p>
            <p style="margin-top: 1rem;">Every chapter you read is automatically tracked. Just keep reading!</p>
        </div>
        
        <a href="chapter-list.html" class="btn">📚 View Chapters</a>
    </div>
    '''

def main():
    print("📚 Generating static site with Wiki Sidebar...")
    
    data = load_chapters()
    char_data = load_characters()
    chapters = data['chapters']
    total = len(chapters)
    
    char_count = len(char_data['characters'])
    term_count = len(char_data['terms'])
    loc_count = len(char_data.get('locations', []))
    event_count = len(char_data.get('events', []))
    
    print(f"   Found {total} chapters")
    print(f"   Wiki: {char_count} characters, {term_count} terms, {loc_count} locations, {event_count} events")
    
    # Create directories
    OUTPUT_DIR.mkdir(exist_ok=True)
    (OUTPUT_DIR / 'chapters').mkdir(exist_ok=True)
    (OUTPUT_DIR / 'css').mkdir(exist_ok=True)
    (OUTPUT_DIR / 'js').mkdir(exist_ok=True)
    
    # Write assets
    (OUTPUT_DIR / 'css' / 'style.css').write_text(get_css())
    (OUTPUT_DIR / 'js' / 'main.js').write_text(get_js(char_data))
    print("   ✓ CSS and JS with embedded wiki data")
    
    template = get_base_template()
    chat = get_chat_widget()
    
    def render(title, content, css='css/style.css', js='js/main.js', home='index.html', chaps='chapter-list.html', login='login.html', with_sidebar=False):
        return template.format(
            title=title, content=content, css_path=css, js_path=js,
            home_path=home, chapters_path=chaps, login_path=login, chat_widget=chat,
            main_class=' class="with-sidebar"' if with_sidebar else ''
        )
    
    # Index
    (OUTPUT_DIR / 'index.html').write_text(render('Shadow Slave - by Guiltythree', generate_index(total)))
    print("   ✓ index.html")
    
    # Chapter list
    (OUTPUT_DIR / 'chapter-list.html').write_text(render('All Chapters - Shadow Slave', generate_chapter_list(chapters)))
    print("   ✓ chapter-list.html")
    
    # Login
    (OUTPUT_DIR / 'login.html').write_text(render('Save Progress - Shadow Slave', generate_login()))
    print("   ✓ login.html")
    
    # Chapters with sidebar
    print(f"   Generating {total} chapter pages with wiki sidebar...")
    for i, chapter in enumerate(chapters):
        num = chapter['chapter_number']
        prev_num = num - 1 if num > 1 else None
        next_num = num + 1 if num < total else None
        
        html = template.format(
            title=f"{chapter['title']} - Shadow Slave",
            content=generate_chapter(chapter, prev_num, next_num, total),
            css_path='../css/style.css',
            js_path='../js/main.js',
            home_path='../index.html',
            chapters_path='../chapter-list.html',
            login_path='../login.html',
            chat_widget=chat,
            main_class=' class="with-sidebar"'
        )
        (OUTPUT_DIR / 'chapters' / f'{num}.html').write_text(html)
        
        if (i + 1) % 500 == 0:
            print(f"      {i + 1}/{total}...")
    
    # .nojekyll
    (OUTPUT_DIR / '.nojekyll').touch()
    
    print(f"\n✅ Static site generated!")
    print(f"   - {total} chapters with wiki sidebar")
    print(f"   - Wiki updates based on current chapter")
    print(f"   - {char_count + term_count + loc_count + event_count} total wiki entries")
    print(f"   - Author: Guiltythree")

if __name__ == '__main__':
    main()
