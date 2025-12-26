#!/usr/bin/env python3
"""
Generate a static site from the chapters data.
Includes AI Assistant and spoiler-free Character Wiki.
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
    --text: #e0e0e0;
    --text-light: rgba(255, 255, 255, 0.6);
    --accent: #ff6b6b;
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

.btn-secondary {
    background: rgba(255, 255, 255, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.2);
}
.btn-secondary:hover {
    background: rgba(255, 255, 255, 0.2);
    box-shadow: none;
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

/* Wiki */
.wiki-header {
    text-align: center;
    margin-bottom: 2rem;
}
.wiki-header h1 {
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.wiki-notice {
    background: rgba(255, 107, 107, 0.1);
    border: 1px solid rgba(255, 107, 107, 0.3);
    padding: 1rem;
    border-radius: 8px;
    margin: 1rem 0;
    color: var(--accent);
}

.wiki-controls {
    display: flex;
    gap: 1rem;
    margin-bottom: 2rem;
    flex-wrap: wrap;
    align-items: center;
}
.wiki-controls label { color: var(--text-light); }
.wiki-controls input, .wiki-controls select {
    padding: 0.5rem 1rem;
    background: rgba(255, 255, 255, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 8px;
    color: var(--text);
}

.wiki-tabs {
    display: flex;
    gap: 1rem;
    margin-bottom: 2rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    padding-bottom: 1rem;
}
.wiki-tab {
    padding: 0.5rem 1.5rem;
    background: transparent;
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 8px;
    color: var(--text);
    cursor: pointer;
    transition: all 0.3s;
}
.wiki-tab:hover, .wiki-tab.active {
    background: var(--primary);
    border-color: var(--primary);
}

.character-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1.5rem;
}
.character-card {
    background: rgba(255, 255, 255, 0.05);
    padding: 1.5rem;
    border-radius: 12px;
    border: 1px solid rgba(255, 255, 255, 0.1);
}
.character-card h3 {
    color: var(--primary);
    margin-bottom: 0.5rem;
}
.character-card .aliases {
    color: var(--text-light);
    font-size: 0.85rem;
    margin-bottom: 0.5rem;
}
.character-card .description {
    margin-bottom: 1rem;
}
.character-card .meta {
    font-size: 0.85rem;
    color: var(--text-light);
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
}
.character-card .meta span {
    background: rgba(255, 255, 255, 0.1);
    padding: 0.25rem 0.5rem;
    border-radius: 4px;
}
.character-card.spoiler {
    opacity: 0.3;
    filter: blur(2px);
    pointer-events: none;
}

.term-list {
    display: grid;
    gap: 1rem;
}
.term-card {
    background: rgba(255, 255, 255, 0.05);
    padding: 1rem 1.5rem;
    border-radius: 8px;
    border-left: 3px solid var(--secondary);
}
.term-card h4 { color: var(--primary); margin-bottom: 0.5rem; }
.term-card.spoiler { opacity: 0.3; filter: blur(2px); }

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
@media (max-width: 768px) {
    .stats { grid-template-columns: 1fr; }
    .hero h1 { font-size: 2rem; }
    nav { flex-direction: column; gap: 1rem; }
    .search-box { width: 100%; }
    .chapter-list-header { flex-direction: column; }
    .menu-grid { grid-template-columns: 1fr; }
    .ai-chat-panel { width: calc(100vw - 40px); right: 20px; }
}
'''

def get_js():
    return '''// Shadow Slave Reader - by Guiltythree
// With AI Assistant and Character Wiki

const Storage = {
    getProgress() { return JSON.parse(localStorage.getItem('readingProgress') || '{}'); },
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
    getLastChapter() { return this.getProgress().lastChapter || null; },
    isRead(chapterNum) { return (this.getProgress().readChapters || []).includes(chapterNum); },
    getReadCount() { return (this.getProgress().readChapters || []).length; },
    getMaxChapterRead() {
        const chapters = this.getProgress().readChapters || [];
        return chapters.length > 0 ? Math.max(...chapters) : 0;
    }
};

// AI Assistant
const AIAssistant = {
    responses: {
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
        progress: () => {
            const last = Storage.getLastChapter();
            const count = Storage.getReadCount();
            return last ? `You've read ${count} chapters so far. You were last on Chapter ${last}. Keep going!` : "You haven't started reading yet. Begin with Chapter 1!";
        },
        wiki: "Check out the Character Wiki! It automatically hides spoilers based on your reading progress.",
        help: "I can help with: character info, world terms, your progress, navigation. Try asking about Sunny, Nephis, the Nightmare Spell, or your reading progress!",
        unknown: [
            "I'm not sure about that. Try asking about specific characters or concepts!",
            "That's beyond my knowledge. Ask me about characters, the Nightmare Spell, or Aspects!",
            "Hmm, I don't have info on that. Want to know about the main characters?"
        ]
    },
    
    processQuery(query) {
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
    },
    
    random(arr) { return arr[Math.floor(Math.random() * arr.length)]; }
};

// Initialize chat
function initChat() {
    const btn = document.querySelector('.ai-chat-button');
    const panel = document.querySelector('.ai-chat-panel');
    const closeBtn = document.querySelector('.ai-chat-close');
    const input = document.querySelector('.ai-chat-input input');
    const sendBtn = document.querySelector('.ai-chat-input button');
    const messages = document.querySelector('.ai-chat-messages');
    
    if (!btn) return;
    
    btn.onclick = () => panel.classList.toggle('open');
    closeBtn.onclick = () => panel.classList.remove('open');
    
    function sendMessage() {
        const text = input.value.trim();
        if (!text) return;
        
        // User message
        const userMsg = document.createElement('div');
        userMsg.className = 'ai-message user';
        userMsg.textContent = text;
        messages.appendChild(userMsg);
        
        input.value = '';
        
        // AI response
        setTimeout(() => {
            const botMsg = document.createElement('div');
            botMsg.className = 'ai-message bot';
            botMsg.textContent = AIAssistant.processQuery(text);
            messages.appendChild(botMsg);
            messages.scrollTop = messages.scrollHeight;
        }, 500);
        
        messages.scrollTop = messages.scrollHeight;
    }
    
    sendBtn.onclick = sendMessage;
    input.onkeypress = (e) => { if (e.key === 'Enter') sendMessage(); };
    
    // Initial greeting
    const greeting = document.createElement('div');
    greeting.className = 'ai-message bot';
    greeting.textContent = "Hello! I'm your Shadow Slave guide. Ask me about characters, concepts, or your reading progress!";
    messages.appendChild(greeting);
}

// Chapter page
function initChapterPage() {
    const match = window.location.pathname.match(/chapters\\/([0-9]+)\\.html/);
    if (match) {
        const chapterNum = parseInt(match[1]);
        Storage.saveProgress(chapterNum);
    }
}

// Index page
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
        if (readCount) readCount.textContent = Storage.getReadCount();
    }
}

// Chapter list
function initChapterList() {
    document.querySelectorAll('.chapter-card').forEach(card => {
        const match = card.href.match(/chapters\\/([0-9]+)\\.html/);
        if (match && Storage.isRead(parseInt(match[1]))) {
            card.classList.add('read');
        }
    });
    
    const searchBox = document.getElementById('chapter-search');
    if (searchBox) {
        searchBox.addEventListener('input', (e) => {
            const query = e.target.value.toLowerCase();
            document.querySelectorAll('.chapter-card').forEach(card => {
                card.style.display = card.textContent.toLowerCase().includes(query) ? 'block' : 'none';
            });
        });
    }
}

// Wiki
function initWiki() {
    const slider = document.getElementById('chapter-slider');
    const sliderValue = document.getElementById('slider-value');
    const characters = document.querySelectorAll('.character-card');
    const terms = document.querySelectorAll('.term-card');
    const tabs = document.querySelectorAll('.wiki-tab');
    
    if (!slider) return;
    
    // Set slider to max chapter read
    const maxRead = Storage.getMaxChapterRead();
    if (maxRead > 0) {
        slider.value = maxRead;
        sliderValue.textContent = maxRead;
    }
    
    function updateWiki() {
        const maxChapter = parseInt(slider.value);
        sliderValue.textContent = maxChapter;
        
        characters.forEach(card => {
            const firstAppear = parseInt(card.dataset.firstAppearance);
            card.classList.toggle('spoiler', firstAppear > maxChapter);
        });
        
        terms.forEach(card => {
            const firstAppear = parseInt(card.dataset.firstAppearance);
            card.classList.toggle('spoiler', firstAppear > maxChapter);
        });
    }
    
    slider.oninput = updateWiki;
    updateWiki();
    
    // Tabs
    tabs.forEach(tab => {
        tab.onclick = () => {
            tabs.forEach(t => t.classList.remove('active'));
            tab.classList.add('active');
            
            const target = tab.dataset.tab;
            document.getElementById('characters-section').style.display = target === 'characters' ? 'block' : 'none';
            document.getElementById('terms-section').style.display = target === 'terms' ? 'block' : 'none';
        };
    });
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

// Init
document.addEventListener('DOMContentLoaded', () => {
    initChat();
    
    if (document.querySelector('.chapter-content')) initChapterPage();
    else if (document.querySelector('.hero')) initIndexPage();
    else if (document.querySelector('.chapters-grid')) initChapterList();
    else if (document.querySelector('.wiki-header')) initWiki();
});
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
                <a href="{wiki_path}">📝 Wiki</a>
                <a href="{login_path}">💾 Save</a>
            </div>
        </nav>
    </header>
    <main>
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
        <a href="wiki.html" class="menu-card">
            <div class="icon">📝</div>
            <h3>Character Wiki</h3>
            <p>Spoiler-free character guide</p>
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
    
    return f'''
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
        <a href="../wiki.html">📝 Wiki</a>
        <a href="{next_link}" class="{next_class}">Next →</a>
    </div>
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

def generate_wiki(char_data, total_chapters):
    # Characters
    char_cards = []
    for char in sorted(char_data['characters'], key=lambda x: x['first_appearance']):
        aliases = ', '.join(char['aliases']) if char['aliases'] else 'None'
        aspect = char.get('aspect', 'Unknown')
        char_cards.append(f'''
        <div class="character-card" data-first-appearance="{char['first_appearance']}" data-type="{char['type']}">
            <h3>{char['name']}</h3>
            <div class="aliases">AKA: {aliases}</div>
            <div class="description">{char['description']}</div>
            <div class="meta">
                <span>First: Ch.{char['first_appearance']}</span>
                <span>Type: {char['type'].title()}</span>
                <span>Aspect: {aspect}</span>
            </div>
        </div>''')
    
    # Terms
    term_cards = []
    for term in sorted(char_data['terms'], key=lambda x: x['first_appearance']):
        term_cards.append(f'''
        <div class="term-card" data-first-appearance="{term['first_appearance']}">
            <h4>{term['name']}</h4>
            <p>{term['description']}</p>
            <small>First mentioned: Chapter {term['first_appearance']}</small>
        </div>''')
    
    return f'''
    <div class="wiki-header">
        <h1>📝 Character Wiki</h1>
        <p>Spoiler-free based on your reading progress</p>
    </div>
    
    <div class="wiki-notice">
        ⚠️ <strong>Spoiler Protection:</strong> Characters and terms are hidden until you've read the chapter where they first appear. Adjust the slider to reveal more!
    </div>
    
    <div class="wiki-controls">
        <label>Show content up to Chapter:</label>
        <input type="range" id="chapter-slider" min="1" max="{total_chapters}" value="1">
        <span id="slider-value">1</span>
    </div>
    
    <div class="wiki-tabs">
        <button class="wiki-tab active" data-tab="characters">👤 Characters</button>
        <button class="wiki-tab" data-tab="terms">📖 Terms & Concepts</button>
    </div>
    
    <div id="characters-section">
        <div class="character-grid">
            {''.join(char_cards)}
        </div>
    </div>
    
    <div id="terms-section" style="display: none;">
        <div class="term-list">
            {''.join(term_cards)}
        </div>
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
    print("📚 Generating static site with AI Assistant & Wiki...")
    
    data = load_chapters()
    char_data = load_characters()
    chapters = data['chapters']
    total = len(chapters)
    print(f"   Found {total} chapters, {len(char_data['characters'])} characters, {len(char_data['terms'])} terms")
    
    # Create directories
    OUTPUT_DIR.mkdir(exist_ok=True)
    (OUTPUT_DIR / 'chapters').mkdir(exist_ok=True)
    (OUTPUT_DIR / 'css').mkdir(exist_ok=True)
    (OUTPUT_DIR / 'js').mkdir(exist_ok=True)
    
    # Write assets
    (OUTPUT_DIR / 'css' / 'style.css').write_text(get_css())
    (OUTPUT_DIR / 'js' / 'main.js').write_text(get_js())
    print("   ✓ CSS and JS")
    
    template = get_base_template()
    chat = get_chat_widget()
    
    def render(title, content, css='css/style.css', js='js/main.js', home='index.html', chaps='chapter-list.html', wiki='wiki.html', login='login.html'):
        return template.format(
            title=title, content=content, css_path=css, js_path=js,
            home_path=home, chapters_path=chaps, wiki_path=wiki, login_path=login, chat_widget=chat
        )
    
    # Index
    (OUTPUT_DIR / 'index.html').write_text(render('Shadow Slave - by Guiltythree', generate_index(total)))
    print("   ✓ index.html")
    
    # Chapter list
    (OUTPUT_DIR / 'chapter-list.html').write_text(render('All Chapters - Shadow Slave', generate_chapter_list(chapters)))
    print("   ✓ chapter-list.html")
    
    # Wiki
    (OUTPUT_DIR / 'wiki.html').write_text(render('Character Wiki - Shadow Slave', generate_wiki(char_data, total)))
    print("   ✓ wiki.html")
    
    # Login
    (OUTPUT_DIR / 'login.html').write_text(render('Save Progress - Shadow Slave', generate_login()))
    print("   ✓ login.html")
    
    # Chapters
    print(f"   Generating {total} chapter pages...")
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
            wiki_path='../wiki.html',
            login_path='../login.html',
            chat_widget=chat
        )
        (OUTPUT_DIR / 'chapters' / f'{num}.html').write_text(html)
        
        if (i + 1) % 500 == 0:
            print(f"      {i + 1}/{total}...")
    
    # .nojekyll
    (OUTPUT_DIR / '.nojekyll').touch()
    
    print(f"\n✅ Static site generated!")
    print(f"   - {total} chapters")
    print(f"   - AI Assistant on every page")
    print(f"   - Spoiler-free Character Wiki")
    print(f"   - Author: Guiltythree")

if __name__ == '__main__':
    main()
