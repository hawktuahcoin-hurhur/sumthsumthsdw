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
    --warning: #fbbf24;
    --border: rgba(255, 255, 255, 0.12);
    --border-strong: rgba(255, 255, 255, 0.18);
    --radius-sm: 0px;
    --radius: 0px;
    --radius-lg: 0px;
    --shadow: none;
}

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
    background: var(--dark-bg);
    color: var(--text);
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    line-height: 1.6;
    min-height: 100vh;
}

header {
    background: rgba(0, 0, 0, 0.35);
    padding: 1rem 2rem;
    border-bottom: 1px solid var(--border);
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
    font-weight: 650;
    color: var(--text);
    text-decoration: none;
}

.nav-links { display: flex; gap: 1.5rem; }
.nav-links a {
    color: var(--text);
    text-decoration: none;
    transition: color 0.2s ease;
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

/* Form controls */
input[type="text"],
input[type="search"],
textarea {
    font: inherit;
    color: var(--text);
    caret-color: var(--text);
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid var(--border-strong);
    border-radius: 0;
    -webkit-appearance: none;
    appearance: none;
}
input[type="text"]::placeholder,
input[type="search"]::placeholder,
textarea::placeholder {
    color: rgba(255, 255, 255, 0.45);
}
input[type="text"]:focus,
input[type="search"]:focus,
textarea:focus {
    outline: none;
    border-color: rgba(0, 212, 255, 0.35);
    background: rgba(255, 255, 255, 0.08);
}
input:-webkit-autofill {
    -webkit-text-fill-color: var(--text);
    -webkit-box-shadow: 0 0 0px 1000px rgba(255, 255, 255, 0.06) inset;
    transition: background-color 9999s ease-in-out 0s;
}

/* Hero */
.hero { text-align: center; padding: 4rem 0; }
.hero h1 {
    font-size: 3rem;
    color: var(--text);
    margin-bottom: 0.5rem;
    letter-spacing: -0.02em;
}
.hero .author { color: var(--text-light); font-size: 1.2rem; margin-bottom: 2rem; }

.disclaimer-banner {
    background: rgba(251, 191, 36, 0.08);
    border: 1px solid rgba(251, 191, 36, 0.2);
    border-radius: var(--radius);
    padding: 0.75rem 1rem;
    margin: 0 auto 1.5rem;
    max-width: 600px;
    text-align: center;
}
.disclaimer-banner p {
    margin: 0;
    color: rgba(255, 255, 255, 0.82);
    font-size: 0.9rem;
}

.btn {
    display: inline-block;
    padding: 1rem 2rem;
    background: rgba(0, 212, 255, 0.14);
    color: var(--text);
    border-radius: var(--radius);
    font-weight: 650;
    font-size: 1.1rem;
    text-decoration: none;
    transition: background 0.2s ease, border-color 0.2s ease;
    border: 1px solid rgba(0, 212, 255, 0.25);
    cursor: pointer;
}
.btn:hover {
    background: rgba(0, 212, 255, 0.2);
    border-color: rgba(0, 212, 255, 0.35);
    color: var(--text);
}

.menu-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.menu-card {
    background: rgba(255, 255, 255, 0.035);
    padding: 2rem;
    border-radius: var(--radius);
    text-align: center;
    border: 1px solid var(--border);
    transition: background 0.2s ease, border-color 0.2s ease;
    text-decoration: none;
    color: var(--text);
}
.menu-card:hover {
    background: rgba(255, 255, 255, 0.055);
    border-color: var(--border-strong);
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
    background: rgba(255, 255, 255, 0.035);
    padding: 2rem;
    border-radius: var(--radius);
    text-align: center;
    border: 1px solid var(--border);
}
.stat-number {
    font-size: 2.5rem;
    font-weight: bold;
    color: var(--text);
}
.stat-label { color: var(--text-light); margin-top: 0.5rem; }

.resume-section {
    background: rgba(0, 212, 255, 0.08);
    padding: 2rem;
    border-radius: var(--radius);
    margin: 2rem 0;
    text-align: center;
    border: 1px solid rgba(0, 212, 255, 0.18);
    display: none;
}
.resume-section.visible { display: block; }
.resume-section h3 { margin-bottom: 1rem; color: var(--primary); }

/* Chapter reader */
.chapter-container { flex: 1; }

.chapter-header {
    margin-bottom: 2rem;
    padding-bottom: 1rem;
    border-bottom: 1px solid var(--border);
}
.chapter-header h1 {
    font-size: 1.8rem;
    color: var(--text);
}
.chapter-meta { color: var(--text-light); font-size: 0.9rem; margin-top: 0.5rem; }

/* Text-to-Speech */
.tts-controls {
    margin-top: 0.75rem;
    display: flex;
    gap: 0.5rem;
    align-items: center;
    flex-wrap: wrap;
}
.tts-controls .tts-btn {
    padding: 0.45rem 0.7rem;
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid var(--border);
    color: var(--text);
    cursor: pointer;
    font: inherit;
    border-radius: 0;
}
.tts-controls .tts-btn:hover {
    background: rgba(255, 255, 255, 0.06);
    border-color: var(--border-strong);
}
.tts-controls .tts-btn:disabled {
    opacity: 0.45;
    cursor: not-allowed;
}
.tts-controls .tts-rate-label {
    display: inline-flex;
    gap: 0.4rem;
    align-items: center;
    color: var(--text-light);
    font-size: 0.85rem;
}
.tts-controls .tts-rate {
    padding: 0.45rem 0.6rem;
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid var(--border);
    color: var(--text);
    border-radius: 0;
}
.tts-unsupported {
    color: var(--text-light);
    font-size: 0.85rem;
}

.chapter-content {
    background: rgba(255, 255, 255, 0.02);
    padding: 2rem;
    border-radius: var(--radius);
    border: 1px solid var(--border);
    line-height: 1.9;
    font-size: 1.05rem;
}
.chapter-content p { margin-bottom: 1.5rem; text-align: justify; }

.chapter-content .chapter-paragraph.tts-active {
    background: rgba(0, 212, 255, 0.08);
    outline: 1px solid rgba(0, 212, 255, 0.22);
    outline-offset: 0;
}

.chapter-content .tts-word-active {
    background: rgba(0, 212, 255, 0.4);
    color: #fff;
    padding: 0.1em 0.2em;
    border-radius: 2px;
    font-weight: 500;
    transition: background 0.05s ease;
}

.chapter-nav {
    display: flex;
    justify-content: space-between;
    margin-top: 2rem;
    padding-top: 2rem;
    border-top: 1px solid var(--border);
    flex-wrap: wrap;
    gap: 1rem;
}
.chapter-nav a {
    padding: 0.75rem 1.5rem;
    background: rgba(255, 255, 255, 0.04);
    border-radius: var(--radius);
    border: 1px solid var(--border);
    transition: background 0.2s ease, border-color 0.2s ease;
}
.chapter-nav a:hover { background: rgba(255, 255, 255, 0.06); border-color: var(--border-strong); }
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
    color: var(--text);
}
.search-box {
    padding: 0.75rem 1rem;
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid var(--border-strong);
    border-radius: var(--radius);
    color: var(--text);
    width: 300px;
    max-width: 100%;
    min-height: 42px;
}
.search-box:focus { outline: none; border-color: rgba(0, 212, 255, 0.35); }

.chapters-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 1rem;
}
.chapter-card {
    background: rgba(255, 255, 255, 0.03);
    padding: 1rem 1.5rem;
    border-radius: var(--radius);
    border: 1px solid var(--border);
    transition: background 0.2s ease, border-color 0.2s ease;
    text-decoration: none;
    color: var(--text);
    display: block;
}
.chapter-card:hover {
    background: rgba(255, 255, 255, 0.05);
    border-color: var(--border-strong);
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
    cursor: pointer;
}
.wiki-item:hover {
    background: rgba(255, 255, 255, 0.08);
    border-left-color: var(--primary);
    transform: translateX(3px);
}
.wiki-item .description-preview {
    font-size: 0.8rem;
    line-height: 1.4;
    color: var(--text-light);
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
}
.wiki-item .click-hint {
    font-size: 0.65rem;
    color: var(--primary);
    opacity: 0.7;
    margin-top: 0.3rem;
}
.wiki-item:hover .click-hint {
    opacity: 1;
}
.wiki-item.new-this-chapter {
    border-left-color: var(--success);
    background: rgba(74, 222, 128, 0.1);
}
.wiki-item.rank-upgraded {
    border-left-color: var(--warning);
    background: rgba(251, 191, 36, 0.1);
    animation: rankGlow 2s ease-in-out;
}
@keyframes rankGlow {
    0%, 100% { box-shadow: none; }
    50% { box-shadow: 0 0 15px rgba(251, 191, 36, 0.5); }
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
    display: none;
}

/* Wiki Modal */
.wiki-modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.85);
    backdrop-filter: blur(5px);
    z-index: 2000;
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 0;
    visibility: hidden;
    transition: all 0.3s ease;
}
.wiki-modal-overlay.active {
    opacity: 1;
    visibility: visible;
}
.wiki-modal {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    border-radius: 16px;
    max-width: 600px;
    width: 90%;
    max-height: 80vh;
    overflow-y: auto;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
    border: 1px solid rgba(255, 255, 255, 0.1);
    transform: scale(0.9) translateY(20px);
    transition: transform 0.3s ease;
}
.wiki-modal-overlay.active .wiki-modal {
    transform: scale(1) translateY(0);
}
.wiki-modal-header {
    padding: 1.5rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    position: sticky;
    top: 0;
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    z-index: 1;
}
.wiki-modal-header h2 {
    color: var(--primary);
    font-size: 1.5rem;
    margin: 0;
}
.wiki-modal-header .badges {
    display: flex;
    gap: 0.5rem;
    margin-top: 0.5rem;
    flex-wrap: wrap;
}
.wiki-modal-header .badge {
    font-size: 0.75rem;
    padding: 0.25rem 0.6rem;
    border-radius: 4px;
    background: var(--secondary);
    color: white;
}
.wiki-modal-header .badge.new { background: var(--success); }
.wiki-modal-header .badge.rank { background: var(--warning); color: #1a1a2e; }
.wiki-modal-close {
    background: none;
    border: none;
    color: var(--text-light);
    font-size: 1.5rem;
    cursor: pointer;
    padding: 0.5rem;
    transition: color 0.2s;
}
.wiki-modal-close:hover {
    color: var(--primary);
}
.wiki-modal-body {
    padding: 1.5rem;
}
.wiki-modal-section {
    margin-top: 1.25rem;
}
.wiki-modal-section h3 {
    margin: 0 0 0.5rem 0;
    font-size: 1.1rem;
    color: var(--primary);
}
.chip-list {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
}
.chip {
    padding: 0.35rem 0.6rem;
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(255, 255, 255, 0.15);
    font-size: 0.8rem;
    color: var(--text);
}
.chip .meta {
    margin-left: 0.35rem;
    color: var(--text-light);
    font-size: 0.7rem;
}
.wiki-modal-aliases {
    color: var(--text-light);
    font-size: 0.9rem;
    margin-bottom: 1rem;
    font-style: italic;
}
.wiki-modal-description {
    font-size: 1rem;
    line-height: 1.7;
    color: var(--text);
    margin-bottom: 1.5rem;
}
.wiki-modal-meta {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 0.75rem;
    margin-bottom: 1.5rem;
}
.wiki-modal-meta-item {
    background: rgba(255, 255, 255, 0.05);
    padding: 0.75rem;
    border-radius: 8px;
    border-left: 3px solid var(--secondary);
}
.wiki-modal-meta-item label {
    display: block;
    font-size: 0.7rem;
    color: var(--text-light);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 0.25rem;
}
.wiki-modal-meta-item span {
    color: var(--primary);
    font-weight: 500;
}
.wiki-modal-rank-history {
    background: rgba(251, 191, 36, 0.1);
    border-radius: 8px;
    padding: 1rem;
    border: 1px solid rgba(251, 191, 36, 0.2);
}
.wiki-modal-rank-history h4 {
    color: var(--warning);
    font-size: 0.9rem;
    margin: 0 0 0.75rem 0;
}
.wiki-modal-rank-list {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
}
.wiki-modal-rank-entry {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    background: rgba(0, 0, 0, 0.3);
    padding: 0.5rem 0.75rem;
    border-radius: 6px;
}
.wiki-modal-rank-entry.current {
    background: rgba(251, 191, 36, 0.2);
    border: 1px solid var(--warning);
}
.wiki-modal-rank-entry .rank {
    color: var(--primary);
    font-weight: 600;
}
.wiki-modal-rank-entry .chapter {
    color: var(--text-light);
    font-size: 0.8rem;
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
    border-radius: var(--radius-sm);
}
.wiki-item .meta span.rank-upgrade {
    background: rgba(251, 191, 36, 0.3);
    color: var(--warning);
    font-weight: bold;
}

/* Rank History */
.rank-history {
    margin-top: 0.5rem;
    padding-top: 0.5rem;
    border-top: 1px solid var(--border);
}
.rank-history .rank-title {
    font-size: 0.7rem;
    color: var(--text-light);
    margin-bottom: 0.3rem;
}
.rank-history .rank-entry {
    display: inline-flex;
    align-items: center;
    gap: 0.25rem;
    font-size: 0.7rem;
    margin-right: 0.5rem;
    margin-bottom: 0.25rem;
    padding: 0.15rem 0.4rem;
    background: rgba(255, 255, 255, 0.05);
    border-radius: 3px;
}
.rank-history .rank-entry.current {
    background: rgba(251, 191, 36, 0.2);
    border: 1px solid rgba(251, 191, 36, 0.5);
}
.rank-history .rank-name {
    color: var(--primary);
    font-weight: 500;
}
.rank-history .rank-chapter {
    color: var(--text-light);
    font-size: 0.65rem;
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

/* AI Chat Widget - Sleek Minimal Design */
.ai-chat-widget {
    position: fixed;
    bottom: 20px;
    right: 20px;
    z-index: 1000;
}

.ai-chat-button {
    width: 48px;
    height: 48px;
    border-radius: var(--radius);
    background: var(--card-bg);
    border: 1px solid var(--border);
    cursor: pointer;
    font-size: 1.25rem;
    color: var(--text);
    transition: all 0.2s ease;
}
.ai-chat-button:hover { 
    background: rgba(255, 255, 255, 0.08);
    border-color: rgba(255, 255, 255, 0.25);
}

.ai-chat-panel {
    position: fixed;
    bottom: 80px;
    right: 20px;
    width: 360px;
    max-width: calc(100vw - 40px);
    height: 480px;
    max-height: 70vh;
    background: var(--card-bg);
    border-radius: var(--radius);
    border: 1px solid var(--border);
    display: none;
    flex-direction: column;
    box-shadow: none;
}
.ai-chat-panel.open { display: flex; }

.ai-chat-header {
    padding: 0.875rem 1rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.ai-chat-header h3 {
    font-size: 0.875rem;
    font-weight: 500;
    color: var(--text);
    letter-spacing: 0.02em;
}
.ai-chat-close {
    background: none;
    border: none;
    color: rgba(255, 255, 255, 0.5);
    font-size: 1.25rem;
    cursor: pointer;
    padding: 0;
    line-height: 1;
    transition: color 0.2s;
}
.ai-chat-close:hover { color: var(--text); }

.ai-chat-messages {
    flex: 1;
    overflow-y: auto;
    padding: 1rem;
    display: flex;
    flex-direction: column;
    gap: 0;
}
.ai-message {
    max-width: 100%;
    width: 100%;
    padding: 0.75rem 0.875rem;
    font-size: 0.875rem;
    line-height: 1.5;
    border-radius: 0;
    background: transparent;
    border-top: 1px solid var(--border);
}
.ai-chat-messages .ai-message:first-child {
    border-top: none;
}
.ai-message.bot {
    border-left: 2px solid rgba(255, 255, 255, 0.2);
    border-right: none;
    align-self: stretch;
    color: rgba(255, 255, 255, 0.85);
}
.ai-message.user {
    border-right: 2px solid rgba(255, 255, 255, 0.2);
    border-left: none;
    align-self: stretch;
    color: var(--text);
    text-align: right;
}

.ai-chat-input {
    padding: 0.875rem 1rem;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    display: flex;
    gap: 0.5rem;
}
.ai-chat-input input {
    flex: 1;
    padding: 0.625rem 0.75rem;
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid var(--border-strong);
    border-radius: var(--radius-sm);
    color: var(--text);
    font-size: 0.875rem;
    min-height: 40px;
}
.ai-chat-input input:focus { 
    outline: none; 
    border-color: rgba(0, 212, 255, 0.35);
    background: rgba(255, 255, 255, 0.08);
}
.ai-chat-input button {
    padding: 0.625rem 1rem;
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid var(--border);
    border-radius: var(--radius-sm);
    color: var(--text);
    cursor: pointer;
    font-size: 0.875rem;
    transition: all 0.2s;
}
.ai-chat-input button:hover {
    background: rgba(255, 255, 255, 0.15);
}

/* Login */
.login-container {
    max-width: 400px;
    margin: 4rem auto;
    background: rgba(255, 255, 255, 0.035);
    padding: 3rem;
    border-radius: var(--radius-lg);
    border: 1px solid var(--border);
    text-align: center;
}
.login-container h1 {
    color: var(--text);
    margin-bottom: 1rem;
}
.login-info {
    background: rgba(0, 212, 255, 0.08);
    padding: 1.5rem;
    border-radius: var(--radius);
    margin: 2rem 0;
    border: 1px solid rgba(0, 212, 255, 0.2);
}

/* Comment System & Modals */
#comment-modal {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.7);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 2000;
}

/* Generic modal styling */
.modal {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.75);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 2000;
}

.modal .modal-content {
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 2rem;
    max-width: 420px;
    width: 90vw;
    max-height: 85vh;
    overflow-y: auto;
}

.modal .close-btn {
    background: transparent;
    border: none;
    color: var(--text-light);
    font-size: 1.5rem;
    cursor: pointer;
    padding: 0;
    line-height: 1;
}

.modal .close-btn:hover {
    color: var(--text);
}

#comment-modal .modal-content {
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 2rem;
    max-width: 500px;
    width: 90vw;
    max-height: 80vh;
    overflow-y: auto;
}

#comment-modal h3 {
    margin-bottom: 1rem;
    color: var(--text);
}

.paragraph-comments {
    margin-top: 1rem;
    padding: 1rem;
    background: rgba(255, 255, 255, 0.03);
    border-left: 2px solid var(--secondary);
    border-radius: var(--radius);
    font-size: 0.9rem;
    color: var(--text);
}

.paragraph-comments > div {
    margin-bottom: 0.75rem;
    padding-bottom: 0.75rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

.paragraph-comments > div:last-child {
    margin-bottom: 0;
    border-bottom: none;
    padding-bottom: 0;
}

.close-btn {
    background: none;
    border: none;
    color: var(--text);
    font-size: 1.5rem;
    cursor: pointer;
    padding: 0;
    line-height: 1;
}

#auth-container {
    display: flex !important;
    align-items: center;
    gap: 0.5rem;
}

.btn-sm {
    padding: 0.5rem 1rem;
    font-size: 0.85rem;
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
    chapterContent: '',
    allItems: [],
    
    init(chapterNum, chapterContent) {{
        this.currentChapter = chapterNum;
        this.chapterContent = (chapterContent || '').toLowerCase();
        this.allItems = [
            ...WIKI_DATA.characters.map(i => ({{...i, itemType: 'character'}})),
            ...WIKI_DATA.terms.map(i => ({{...i, itemType: 'term'}})),
            ...WIKI_DATA.locations.map(i => ({{...i, itemType: 'location'}})),
            ...WIKI_DATA.events.map(i => ({{...i, itemType: 'event'}}))
        ];
        this.createModal();
        this.render();
        this.initTabs();
        this.initMobileToggle();
    }},
    
    createModal() {{
        if (document.getElementById('wiki-modal-overlay')) return;
        const overlay = document.createElement('div');
        overlay.id = 'wiki-modal-overlay';
        overlay.className = 'wiki-modal-overlay';
        overlay.innerHTML = `
            <div class="wiki-modal">
                <div class="wiki-modal-header">
                    <div>
                        <h2 id="wiki-modal-title"></h2>
                        <div class="badges" id="wiki-modal-badges"></div>
                    </div>
                    <button class="wiki-modal-close" onclick="WikiSidebar.closeModal()">✕</button>
                </div>
                <div class="wiki-modal-body">
                    <div id="wiki-modal-aliases" class="wiki-modal-aliases"></div>
                    <div id="wiki-modal-description" class="wiki-modal-description"></div>
                    <div id="wiki-modal-meta" class="wiki-modal-meta"></div>
                    <div id="wiki-modal-ranks"></div>
                </div>
            </div>
        `;
        document.body.appendChild(overlay);
        overlay.addEventListener('click', (e) => {{
            if (e.target === overlay) this.closeModal();
        }});
        document.addEventListener('keydown', (e) => {{
            if (e.key === 'Escape') this.closeModal();
        }});
    }},
    
    getTerms(item) {{
        const base = [item.name, ...(item.aliases || [])];
        const terms = (item.search_terms && item.search_terms.length > 0) ? item.search_terms : base;
        return terms.map(t => t.toLowerCase());
    }},
    
    coMentionedItems(subjectItem, targetType) {{
        const subjectTerms = this.getTerms(subjectItem);
        const items = this.allItems.filter(i => i.itemType === targetType && i.first_appearance <= this.currentChapter);
        return items.filter(it => {{
            const itTerms = this.getTerms(it);
            const subjectMentioned = subjectTerms.some(t => this.chapterContent.includes(t));
            const itMentioned = itTerms.some(t => this.chapterContent.includes(t));
            return subjectMentioned && itMentioned;
        }});
    }},

    openModal(itemName) {{
        const item = this.allItems.find(i => i.name === itemName);
        if (!item) return;
        
        const overlay = document.getElementById('wiki-modal-overlay');
        const isNew = item.first_appearance === this.currentChapter;
        
        // Title
        document.getElementById('wiki-modal-title').textContent = item.name;
        
        // Badges
        let badges = [];
        if (isNew) badges.push('<span class="badge new">FIRST APPEARANCE!</span>');
        if (item.type) badges.push(`<span class="badge">${{item.type}}</span>`);
        if (item.category) badges.push(`<span class="badge">${{item.category}}</span>`);
        
        // Current rank badge
        let currentRank = '';
        if (item.rank_progression && item.rank_progression.length > 0) {{
            const applicableRanks = item.rank_progression.filter(r => r.from_chapter <= this.currentChapter);
            if (applicableRanks.length > 0) {{
                currentRank = applicableRanks[applicableRanks.length - 1].rank;
                badges.push(`<span class="badge rank">${{currentRank}}</span>`);
            }}
        }}
        document.getElementById('wiki-modal-badges').innerHTML = badges.join('');
        
        // Aliases
        const aliasesEl = document.getElementById('wiki-modal-aliases');
        if (item.aliases && item.aliases.length > 0) {{
            aliasesEl.innerHTML = `Also known as: ${{item.aliases.join(', ')}}`;
            aliasesEl.style.display = 'block';
        }} else {{
            aliasesEl.style.display = 'none';
        }}
        
        // Description (progressive, stacked up to current chapter)
        const descEl = document.getElementById('wiki-modal-description');
        if (item.description_progression && Array.isArray(item.description_progression)) {{
            const visible = item.description_progression
                .filter(p => p.from_chapter <= this.currentChapter)
                .sort((a, b) => a.from_chapter - b.from_chapter);
            if (visible.length > 0) {{
                descEl.innerHTML = visible.map(p => `<p>${{p.text}}</p>`).join('');
            }} else {{
                descEl.innerHTML = `<p>${{item.description}}</p>`;
            }}
        }} else {{
            descEl.innerHTML = `<p>${{item.description}}</p>`;
        }}
        
        // Meta info
        let metaItems = [];
        metaItems.push(`<div class="wiki-modal-meta-item"><label>First Appearance</label><span>Chapter ${{item.first_appearance}}</span></div>`);
        if (item.aspect && item.aspect !== 'N/A') {{
            metaItems.push(`<div class="wiki-modal-meta-item"><label>Aspect</label><span>${{item.aspect}}</span></div>`);
        }}
        if (item.clan && item.clan !== 'N/A' && item.clan !== 'None') {{
            metaItems.push(`<div class="wiki-modal-meta-item"><label>Clan</label><span>${{item.clan}}</span></div>`);
        }}
        if (item.itemType) {{
            metaItems.push(`<div class="wiki-modal-meta-item"><label>Type</label><span style="text-transform:capitalize">${{item.itemType}}</span></div>`);
        }}
        document.getElementById('wiki-modal-meta').innerHTML = metaItems.join('');
        
        // Rank history
        const ranksEl = document.getElementById('wiki-modal-ranks');
        if (item.rank_progression && item.rank_progression.length > 0) {{
            const visibleRanks = item.rank_progression.filter(r => r.from_chapter <= this.currentChapter);
            if (visibleRanks.length > 0) {{
                ranksEl.innerHTML = `
                    <div class="wiki-modal-rank-history">
                        <h4>⚔️ Rank Progression</h4>
                        <div class="wiki-modal-rank-list">
                            ${{visibleRanks.map(r => `
                                <div class="wiki-modal-rank-entry ${{r.from_chapter === this.currentChapter ? 'current' : ''}}">
                                    <span class="rank">${{r.rank}}</span>
                                    <span class="chapter">Ch.${{r.from_chapter}}</span>
                                </div>
                            `).join('')}}
                        </div>
                    </div>
                `;
                ranksEl.style.display = 'block';
            }} else {{
                ranksEl.style.display = 'none';
            }}
        }} else {{
            ranksEl.style.display = 'none';
        }}

        // Power System: Aspect, Flaw, co-mentioned powers terms (up to current chapter)
        const powerChips = [];
        if (item.aspect && item.aspect !== 'N/A') {{
            powerChips.push(`Aspect: ${{item.aspect}}`);
        }}
        if (item.flaw && item.flaw !== 'N/A') {{
            powerChips.push(`Flaw: ${{item.flaw}}`);
        }}
        if (currentRank) {{
            powerChips.push(`Rank: ${{currentRank}}`);
        }}
        // Co-mentioned terms in category "powers"
        const coTerms = this.coMentionedItems(item, 'term').filter(t => (t.category || '') === 'powers');
        coTerms.forEach(t => powerChips.push(t.name));
        // Explicit powers mapping to terms (if present), filtered by current chapter
        if (Array.isArray(item.explicit_powers) && item.explicit_powers.length > 0) {{
            const explicit = item.explicit_powers
                .map(name => this.allItems.find(i => i.name === name && i.itemType === 'term' && (i.category || '') === 'powers'))
                .filter(t => t && t.first_appearance <= this.currentChapter);
            explicit.forEach(t => powerChips.push(`${{t.name}} (Ch.${{t.first_appearance}})`));
        }}

        const body = document.querySelector('.wiki-modal-body');
        body.querySelectorAll('.wiki-modal-section.dynamic').forEach(el => el.remove());
        if (powerChips.length > 0) {{
            const sec = document.createElement('div');
            sec.className = 'wiki-modal-section dynamic';
            sec.innerHTML = `
                <h3>Power System</h3>
                <div class="chip-list">${{powerChips.map(c => `<span class="chip">${{c}}</span>`).join('')}}
                </div>
            `;
            body.appendChild(sec);
        }}

        // Attributes (explicit or fallback from meta)
        let attributes = Array.isArray(item.attributes) ? item.attributes.slice() : [];
        if (attributes.length === 0) {{
            const auto = [];
            if (item.type) auto.push(`Type: ${{item.type}}`);
            if (currentRank) auto.push(`Rank: ${{currentRank}}`);
            if (item.aspect && item.aspect !== 'N/A') auto.push(`Aspect: ${{item.aspect}}`);
            if (item.flaw && item.flaw !== 'N/A') auto.push(`Flaw: ${{item.flaw}}`);
            if (item.clan && item.clan !== 'N/A' && item.clan !== 'None') auto.push(`Clan: ${{item.clan}}`);
            attributes = auto;
        }}
        // Echoes
        let echoes = [];
        if (Array.isArray(item.echoes) && item.echoes.length > 0) {{
            echoes = item.echoes
                .map(name => this.allItems.find(i => i.name === name && i.itemType === 'echo'))
                .filter(e => e && e.first_appearance <= this.currentChapter);
        }} else if (item.itemType === 'character') {{
            echoes = this.coMentionedItems(item, 'echo');
        }}
        // Memories
        let memories = [];
        if (Array.isArray(item.memories) && item.memories.length > 0) {{
            memories = item.memories
                .map(name => this.allItems.find(i => i.name === name && i.itemType === 'memory'))
                .filter(m => m && m.first_appearance <= this.currentChapter);
        }} else if (item.itemType === 'character') {{
            memories = this.coMentionedItems(item, 'memory');
        }}

        // Render sections (Attributes, Echoes, Memories)
        if (attributes.length > 0) {{
            const sec = document.createElement('div');
            sec.className = 'wiki-modal-section dynamic';
            sec.innerHTML = `
                <h3>Attributes</h3>
                <div class="chip-list">${{attributes.map(a => `<span class="chip">${{a}}</span>`).join('')}}
                </div>
            `;
            body.appendChild(sec);
        }}
        if (echoes.length > 0) {{
            const sec = document.createElement('div');
            sec.className = 'wiki-modal-section dynamic';
            sec.innerHTML = `
                <h3>Echoes</h3>
                <div class="chip-list">${{echoes.map(e => `<span class="chip">${{e.name}}<span class="meta">Ch.${{e.first_appearance}}</span></span>`).join('')}}
                </div>
            `;
            body.appendChild(sec);
        }}
        if (memories.length > 0) {{
            const sec = document.createElement('div');
            sec.className = 'wiki-modal-section dynamic';
            sec.innerHTML = `
                <h3>Memories</h3>
                <div class="chip-list">${{memories.map(m => `<span class="chip">${{m.name}}<span class="meta">Ch.${{m.first_appearance}}</span></span>`).join('')}}
                </div>
            `;
            body.appendChild(sec);
        }}
        
        overlay.classList.add('active');
        document.body.style.overflow = 'hidden';
    }},
    
    closeModal() {{
        const overlay = document.getElementById('wiki-modal-overlay');
        if (overlay) {{
            overlay.classList.remove('active');
            document.body.style.overflow = '';
        }}
    }},
    
    isItemMentioned(item) {{
        // Hard gate: never show items before their first appearance
        if (typeof item.first_appearance === 'number' && item.first_appearance > this.currentChapter) {{
            return false;
        }}
        if (!item.search_terms || item.search_terms.length === 0) {{
            const terms = [item.name, ...(item.aliases || [])];
            return terms.some(term => this.chapterContent.includes(term.toLowerCase()));
        }}
        return item.search_terms.some(term => this.chapterContent.includes(term.toLowerCase()));
    }},
    
    truncate(text, maxLen = 80) {{
        if (text.length <= maxLen) return text;
        return text.substring(0, maxLen).trim() + '...';
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
        
        const visible = items.filter(item => this.isItemMentioned(item));
        visible.sort((a, b) => b.first_appearance - a.first_appearance);
        
        if (visible.length === 0) {{
            container.innerHTML = '<div class="wiki-empty">No wiki entries mentioned in this chapter</div>';
            return;
        }}
        
        container.innerHTML = visible.map(item => {{
            const isNew = item.first_appearance === this.currentChapter;
            const newBadge = isNew ? '<span class="badge new">NEW</span>' : '';
            const typeBadge = item.type ? `<span class="badge">${{item.type}}</span>` : '';
            const categoryBadge = item.category ? `<span class="badge">${{item.category}}</span>` : '';
            
            // Get current rank if applicable
            let rankBadge = '';
            if (item.rank_progression && item.rank_progression.length > 0) {{
                const applicableRanks = item.rank_progression.filter(r => r.from_chapter <= this.currentChapter);
                if (applicableRanks.length > 0) {{
                    const currentRank = applicableRanks[applicableRanks.length - 1].rank;
                    const isUpgrade = applicableRanks[applicableRanks.length - 1].from_chapter === this.currentChapter && applicableRanks.length > 1;
                    rankBadge = isUpgrade ? `<span class="badge" style="background:#fbbf24;color:#1a1a2e">⬆️ ${{currentRank}}</span>` : '';
                }}
            }}
            
            // Progressive preview: latest paragraph up to current chapter or base description
            let previewText = item.description;
            if (item.description_progression && Array.isArray(item.description_progression)) {{
                const visible = item.description_progression
                    .filter(p => p.from_chapter <= this.currentChapter)
                    .sort((a, b) => a.from_chapter - b.from_chapter);
                if (visible.length > 0) {{
                    previewText = visible[visible.length - 1].text;
                }}
            }}
            const preview = this.truncate(previewText, 100);
            
            // Use single-quoted HTML attribute and JSON.stringify to safely handle apostrophes in item names.
            const safeName = JSON.stringify(item.name);
            return `
                <div class="wiki-item ${{isNew ? 'new-this-chapter' : ''}}" onclick='WikiSidebar.openModal(${{safeName}})'>
                    <h4>${{item.name}} ${{newBadge || rankBadge || typeBadge || categoryBadge}}</h4>
                    <div class="description-preview">${{preview}}</div>
                    <div class="click-hint">Click for more →</div>
                </div>
            `;
        }}).join('');
        
        const tab = document.querySelector(`[data-tab="${{type}}"]`);
        if (tab) {{
            const newCount = visible.filter(i => i.first_appearance === this.currentChapter).length;
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

// Text-to-Speech (Chapter pages)
const TTS = {{
    utterance: null,
    paragraphs: [],
    index: 0,
    supported: () => (typeof window !== 'undefined' && 'speechSynthesis' in window && 'SpeechSynthesisUtterance' in window),

    clearHighlight() {{
        this.paragraphs.forEach(p => p.classList.remove('tts-active'));
    }},

    setHighlight(i) {{
        this.clearHighlight();
        const el = this.paragraphs[i];
        if (!el) return;
        el.classList.add('tts-active');
        // Keep it visible without being too jumpy
        try {{ el.scrollIntoView({{ block: 'nearest' }}); }} catch (e) {{ /* ignore */ }}
    }},

    loadParagraphs() {{
        const nodes = Array.from(document.querySelectorAll('.chapter-content .chapter-paragraph'));
        this.paragraphs = nodes;
    }},

    getText() {{
        // Kept for backwards compatibility; paragraph-based TTS uses DOM paragraphs
        const container = document.querySelector('.chapter-content');
        if (!container) return '';
        const text = (container.innerText || container.textContent || '').trim();
        return text.replace(/\\s+/g, ' ');
    }},

    clearHighlight() {{
        // Clear word-by-word highlights
        document.querySelectorAll('.tts-word-active').forEach(span => {{
            const parent = span.parentNode;
            if (!parent) return;
            const text = span.textContent;
            parent.replaceChild(document.createTextNode(text), span);
            parent.normalize();
        }});
        // Clear paragraph highlights
        if (this.paragraphs) {{
            this.paragraphs.forEach(p => p.classList.remove('tts-active'));
        }}
    }},

    highlightWord(wordIndex) {{
        // Find and highlight the word at wordIndex
        const container = document.querySelector('.chapter-content');
        if (!container) return;
        
        let currentWord = 0;
        const targetWord = wordIndex;
        
        const walkDOM = (node) => {{
            if (node.nodeType === 3) {{ // Text node
                const text = node.textContent;
                const words = text.match(/\\b\\w+\\b|\\s+/g) || [];
                const newSpans = [];
                
                for (const word of words) {{
                    if (word.match(/\\s/)) {{
                        newSpans.push(document.createTextNode(word));
                    }} else {{
                        if (currentWord === targetWord) {{
                            const span = document.createElement('span');
                            span.className = 'tts-word-active';
                            span.textContent = word;
                            newSpans.push(span);
                        }} else {{
                            newSpans.push(document.createTextNode(word));
                        }}
                        currentWord++;
                    }}
                }}
                
                if (newSpans.length > 0) {{
                    node.parentNode.replaceChild(newSpans[0], node);
                    let prev = newSpans[0];
                    for (let i = 1; i < newSpans.length; i++) {{
                        prev.parentNode.insertBefore(newSpans[i], prev.nextSibling);
                        prev = newSpans[i];
                    }}
                }}
            }} else if (node.nodeType === 1) {{ // Element node
                Array.from(node.childNodes).forEach(child => walkDOM(child));
            }}
        }};
        
        walkDOM(container);
    }},

    stop() {{
        if (!this.supported()) return;
        window.speechSynthesis.cancel();
        this.utterance = null;
        this.index = 0;
        this.wordIndex = 0;
        this.clearHighlight();
    }},

    speakCurrent(rate = 1.0) {{
        if (!this.supported()) return;
        if (!this.paragraphs || this.paragraphs.length === 0) this.loadParagraphs();
        if (!this.paragraphs || this.paragraphs.length === 0) return;
        if (this.index < 0) this.index = 0;
        if (this.index >= this.paragraphs.length) {{
            this.stop();
            return;
        }}

        const text = (this.paragraphs[this.index].innerText || this.paragraphs[this.index].textContent || '').trim();
        if (!text) {{
            this.index += 1;
            this.speakCurrent(rate);
            return;
        }}

        const u = new SpeechSynthesisUtterance(text);
        u.rate = Math.max(0.5, Math.min(2.0, Number(rate) || 1.0));
        u.pitch = 1.0;
        u.volume = 1.0;

        this.utterance = u;
        this.setHighlight(this.index);
        this.wordIndex = 0;

        u.onboundary = (event) => {{
            if (event.name === 'word') {{
                this.clearHighlight();
                this.setHighlight(this.index);
                this.highlightWord(this.wordIndex);
                this.wordIndex++;
            }}
        }};

        u.onend = () => {{
            this.wordIndex = 0;
            this.index += 1;
            this.speakCurrent(rate);
        }};
        u.onerror = () => {{
            this.stop();
        }};

        window.speechSynthesis.speak(u);
    }},

    speak(rate = 1.0) {{
        if (!this.supported()) return;
        this.stop();
        this.loadParagraphs();
        this.index = 0;
        this.wordIndex = 0;
        this.speakCurrent(rate);
    }},

    pause() {{
        if (!this.supported()) return;
        if (window.speechSynthesis.speaking && !window.speechSynthesis.paused) window.speechSynthesis.pause();
    }},

    resume() {{
        if (!this.supported()) return;
        if (window.speechSynthesis.paused) window.speechSynthesis.resume();
    }}
}};

// AI Assistant
const AIAssistant = {{
    responses: {{
        greetings: [
            "Hello, Sleeper! Welcome to your journey through the Dream Realm. I'm here to help you navigate this dark and twisted world. Feel free to ask me about characters, the power system, world lore, or your reading progress. What would you like to know?",
            "Greetings, fellow traveler! I'm your guide through Shadow Slave's intricate world. Whether you want to learn about the Nightmare Spell, understand the Awakened ranks, or get info on specific characters like Sunny and Nephis - just ask. How can I assist you today?",
            "Welcome back to the Dream Realm! Ready to continue your adventure? I can help you with character backgrounds, world-building concepts, the complex power system, or help you pick up where you left off. What's on your mind?"
        ],
        sunny: "Sunny, also known as Sunless, is the protagonist of Shadow Slave. He grew up as an orphan in the outskirts - the slums outside the protective walls of human cities. After surviving his First Nightmare, he Awakened with the Shadow Aspect, granting him control over shadows and eventually earning him the title 'Lord Shadow'. What makes Sunny unique is his cunning intellect and dark, sarcastic humor. He's a pragmatic survivor who relies on wit rather than brute strength. His journey from a powerless outcast to one of the most formidable beings is the heart of the story. His sentient shadow companion adds another layer of mystery to his already complex abilities.",
        nephis: "Nephis, known by her True Name 'Changing Star', is one of the most compelling characters in Shadow Slave. She's a Legacy - someone born into one of the great clans (Clan Valor) that have shaped humanity's survival against the Nightmare Spell. Nephis possesses an extraordinary inner fire that literally burns within her, making her one of the most powerful Awakened of her generation. Despite her noble background, she's driven by complex motivations that often put her at odds with her own family. Her relationship with Sunny is central to the story - a mix of mutual respect, tension, and something deeper that evolves throughout the chapters.",
        cassie: "Cassie, sometimes called Cassia, is a blind prophet whose abilities are both a gift and a curse. After becoming Awakened, she gained the power to see visions of the future - glimpses of what's to come that are remarkably accurate. Despite her gentle, kind nature, her prophecies often reveal terrifying truths about the world and its fate. Being blind in the physical world but able to 'see' the future creates a fascinating duality in her character. She's one of Sunny's closest companions, and her prophecies have saved the group countless times - though the burden of knowing what's coming weighs heavily on her.",
        nightmare: "The Nightmare Spell is the catastrophic event that changed humanity forever. It brought the Dream Realm - a dimension of monsters, ancient gods, and unimaginable horrors - crashing into Earth's reality. But it also gave humanity a chance: those who survive their First Nightmare in the Dream Realm return as Awakened, gaining supernatural Aspects and powers. The Spell is mysterious - no one fully understands its origins or true purpose. Some believe it's a curse, others a twisted form of evolution. What's certain is that it created the entire power structure of the world: the great clans, the Citadel, the constant war against Nightmare Creatures, and the desperate struggle for humanity's survival.",
        awakened: "The Awakened are humans who survived their First Nightmare and emerged with supernatural powers called Aspects. The ranking system goes: Sleeper (before awakening) → Awakened (first rank) → Ascended → Master → Saint → Sovereign (the highest known rank). Each rank represents an exponential increase in power. Awakened protect humanity from Nightmare Creatures and explore the Dream Realm for resources and knowledge. The higher ranks become almost godlike in their abilities. Most Awakened never progress beyond the first few ranks - reaching Master is exceptional, and Saints are legendary figures. The journey through these ranks, the trials required, and the transformations involved are central to the story's progression.",
        aspect: "An Aspect is the unique supernatural ability granted to someone after becoming Awakened - it defines their power, fighting style, and often their fate. Each Aspect is different: some grant control over elements, others enhance physical abilities, some provide utility powers. But every Aspect comes with a Flaw - an inherent weakness or curse that balances the power. Flaws can be debilitating or even lethal. For example, Sunny's Shadow Aspect gives him incredible abilities, but his Flaw creates significant complications in his life. The interplay between Aspect powers and their Flaws creates strategic depth in combat and character development throughout the story.",
        shadow: "Sunny's sentient shadow is one of the most intriguing mysteries of the series. Unlike normal shadows, his has its own personality, thoughts, and sometimes even seems to act independently. It can express emotions through gestures and movements, often in humorous or sarcastic ways that mirror Sunny's own personality. The shadow's sentience is connected to his Shadow Aspect, but the full extent of their relationship and the shadow's true nature unfolds gradually through the story. It serves as both a companion and an extension of Sunny's powers, adding depth to his abilities and creating memorable comedic and dramatic moments.",
        progress: () => {{
            const last = Storage.getLastChapter();
            const count = Storage.getReadCount();
            if (last) {{
                const percent = Math.round((last / 2720) * 100);
                return `Great progress! You've read ${{count}} chapters so far (${{percent}}% of the story). You were last reading Chapter ${{last}}. The journey continues - there's still so much to discover about Sunny's path through the Dream Realm. Ready to continue?`;
            }}
            return "You haven't started reading yet! Shadow Slave is an epic journey of over 2,700 chapters following Sunny's transformation from an outcast to a legend. Begin with Chapter 1 and experience the Nightmare Spell for yourself!";
        }},
        wiki: "The Wiki sidebar on the right is your companion through the story! It dynamically shows characters, terms, locations, and events that have appeared up to your current chapter - so you won't encounter spoilers for content you haven't read yet. Click on any entry to see more details. It's perfect for refreshing your memory on who's who or understanding the complex terminology of the Dream Realm. Note: The wiki information is approximate and may not be 100% accurate for all entries.",
        help: "I'm here to help you navigate Shadow Slave! Here's what I can assist with:\\n\\n• Character info - Ask about Sunny, Nephis, Cassie, or other characters\\n• World lore - The Nightmare Spell, Dream Realm, great clans\\n• Power system - Aspects, Flaws, Awakened ranks (Sleeper to Sovereign)\\n• Your progress - Where you left off, chapters read\\n• Wiki guide - How to use the spoiler-free sidebar\\n\\nJust type your question naturally. For example: 'Tell me about Sunny' or 'What are Aspects?'",
        unknown: [
            "I don't have specific information on that topic, but I'd love to help with something else! Try asking about the main characters (Sunny, Nephis, Cassie), the power system (Aspects, Awakened ranks), or the world lore (Nightmare Spell, Dream Realm). What interests you?",
            "That's beyond my current knowledge base. I'm best at explaining Shadow Slave's core concepts - the Nightmare Spell, character backgrounds, the Awakened ranking system, Aspects and Flaws. Would you like to know about any of these?",
            "Hmm, I'm not sure about that particular topic. How about I tell you about one of the main characters? Sunny's journey from outcast to legend is fascinating, or I could explain how the Awakened power system works. What sounds interesting?"
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
        // Get chapter content from the page for wiki filtering
        const chapterContent = document.querySelector('.chapter-content')?.textContent || '';
        WikiSidebar.init(chapterNum, chapterContent);

        // Init Text-to-Speech controls
        const ttsRoot = document.querySelector('[data-tts]');
        if (ttsRoot) {{
            const playBtn = ttsRoot.querySelector('.tts-play');
            const pauseBtn = ttsRoot.querySelector('.tts-pause');
            const resumeBtn = ttsRoot.querySelector('.tts-resume');
            const stopBtn = ttsRoot.querySelector('.tts-stop');
            const rateSel = ttsRoot.querySelector('.tts-rate');
            const unsupported = ttsRoot.querySelector('.tts-unsupported');

            const isSupported = TTS.supported();
            if (!isSupported) {{
                if (unsupported) unsupported.style.display = '';
                [playBtn, pauseBtn, resumeBtn, stopBtn, rateSel].forEach(el => {{ if (el) el.disabled = true; }});
            }} else {{
                if (unsupported) unsupported.style.display = 'none';
                if (playBtn) playBtn.addEventListener('click', () => TTS.speak(rateSel?.value || 1));
                if (pauseBtn) pauseBtn.addEventListener('click', () => TTS.pause());
                if (resumeBtn) resumeBtn.addEventListener('click', () => TTS.resume());
                if (stopBtn) stopBtn.addEventListener('click', () => TTS.stop());

                window.addEventListener('beforeunload', () => TTS.stop());
            }}
        }}
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

// Firebase Integration
const FirebaseConfig = {{
    apiKey: "AIzaSyAx2KtNj6znY8ivypcV5fcQzeNzntevKMU",
    authDomain: "shadowslaveread.firebaseapp.com",
    projectId: "shadowslaveread",
    storageBucket: "shadowslaveread.appspot.com",
    messagingSenderId: "956677381164",
    appId: "1:956677381164:web:04832a90c7b82402cbc589"
}};

let currentUser = null;
let db = null;
let pendingLoginSuccess = false;

async function initFirebase() {{
    try {{
        firebase.initializeApp(FirebaseConfig);
        db = firebase.firestore();

        // Listen for login completion from the dedicated auth popup.
        try {{
            if ('BroadcastChannel' in window) {{
                const authChannel = new BroadcastChannel('ss-auth');
                authChannel.onmessage = (ev) => {{
                    if (ev && ev.data && ev.data.type === 'login-success') {{
                        pendingLoginSuccess = true;
                    }}
                }};
            }}
        }} catch (e) {{ /* ignore */ }}

        window.addEventListener('storage', (e) => {{
            if (e && e.key === 'ss-auth-event' && e.newValue) {{
                try {{
                    const payload = JSON.parse(e.newValue);
                    if (payload && payload.type === 'login-success') pendingLoginSuccess = true;
                }} catch (err) {{ /* ignore */ }}
            }}
        }});
        
        firebase.auth().onAuthStateChanged(user => {{
            currentUser = user;
            userProfile = null;  // Reset profile cache on auth change
            updateAuthUI();
            if (!user) return;

            loadUserProfile();  // Load user profile from Firestore
            loadComments();
            if (pendingLoginSuccess) {{
                pendingLoginSuccess = false;
                setTimeout(() => showLoginSuccess(), 250);
            }}
        }});
    }} catch (e) {{
        console.log('Firebase init:', e.message);
    }}
}}

function updateAuthUI() {{
    const loginBtn = document.getElementById('login-btn');
    const logoutBtn = document.getElementById('logout-btn');
    const profileBtn = document.getElementById('profile-btn');
    const authContainer = document.getElementById('auth-container');
    
    if (!authContainer) return;
    
    if (currentUser) {{
        if (loginBtn) loginBtn.style.display = 'none';
        if (profileBtn) profileBtn.style.display = 'block';
        if (logoutBtn) logoutBtn.style.display = 'block';
        authContainer.style.display = 'flex';
    }} else {{
        if (loginBtn) loginBtn.style.display = 'block';
        if (profileBtn) profileBtn.style.display = 'none';
        if (logoutBtn) logoutBtn.style.display = 'none';
    }}
}}

let userProfile = null;

async function loadUserProfile() {{
    if (!currentUser || !db) return;
    try {{
        const doc = await db.collection('users').doc(currentUser.uid).get();
        if (doc.exists) {{
            userProfile = doc.data();
        }} else {{
            // Create default profile
            userProfile = {{
                displayName: currentUser.displayName || '',
                username: currentUser.email.split('@')[0],
                bio: '',
                createdAt: new Date(),
                commentCount: 0
            }};
            await db.collection('users').doc(currentUser.uid).set(userProfile);
        }}
    }} catch (e) {{
        userProfile = null;
    }}
}}

async function showProfile() {{
    const modal = document.getElementById('profile-modal');
    if (!modal) return;
    
    // Load user profile from Firestore if not cached
    if (currentUser && !userProfile) {{
        await loadUserProfile();
    }}
    
    const displayNameEl = document.getElementById('profile-display-name');
    const usernameEl = document.getElementById('profile-username');
    const emailEl = document.getElementById('profile-email');
    const chaptersEl = document.getElementById('profile-chapters');
    const lastEl = document.getElementById('profile-last');
    const progressEl = document.getElementById('profile-progress');
    const commentsEl = document.getElementById('profile-comments');
    const avatarEl = document.getElementById('profile-avatar');
    const bioEl = document.getElementById('profile-bio');
    const providerEl = document.getElementById('profile-provider');
    const joinedEl = document.getElementById('profile-joined');
    const editBioBtn = document.getElementById('edit-bio-btn');
    
    const totalChapters = 2720;
    const readCount = Storage.getReadCount();
    const lastChapter = Storage.getLastChapter();
    const progress = Math.round((readCount / totalChapters) * 100);
    
    if (currentUser) {{
        const displayName = userProfile?.displayName || currentUser.displayName || currentUser.email.split('@')[0];
        const username = userProfile?.username || currentUser.email.split('@')[0];
        const bio = userProfile?.bio || 'No bio yet. Click Edit to add one!';
        const commentCount = userProfile?.commentCount || 0;
        
        if (displayNameEl) displayNameEl.textContent = displayName;
        if (usernameEl) usernameEl.textContent = '@' + username;
        if (emailEl) emailEl.textContent = currentUser.email;
        if (bioEl) bioEl.textContent = bio;
        if (commentsEl) commentsEl.textContent = commentCount;
        if (editBioBtn) editBioBtn.style.display = 'inline-block';
        
        // Use custom avatar first, then Google avatar, then default
        if (avatarEl) {{
            if (userProfile?.customAvatarUrl) {{
                avatarEl.innerHTML = `<img src="${{userProfile.customAvatarUrl}}" style="width: 100%; height: 100%; border-radius: 50%; object-fit: cover;" />`;
            }} else if (currentUser.photoURL) {{
                avatarEl.innerHTML = `<img src="${{currentUser.photoURL}}" style="width: 100%; height: 100%; border-radius: 50%; object-fit: cover;" />`;
            }} else {{
                avatarEl.innerHTML = '👤';
            }}
        }}
        
        // Provider info
        if (providerEl) {{
            const providerId = currentUser.providerData[0]?.providerId || 'unknown';
            const providerNames = {{ 'google.com': 'Google', 'password': 'Email', 'github.com': 'GitHub' }};
            providerEl.textContent = providerNames[providerId] || providerId;
        }}
        
        // Join date
        if (joinedEl) {{
            const createdAt = userProfile?.createdAt?.toDate?.() || currentUser.metadata?.creationTime;
            if (createdAt) {{
                joinedEl.textContent = new Date(createdAt).toLocaleDateString('en-US', {{ month: 'short', year: 'numeric' }});
            }}
        }}
    }} else {{
        if (displayNameEl) displayNameEl.textContent = 'Guest';
        if (usernameEl) usernameEl.textContent = '@guest';
        if (emailEl) emailEl.textContent = 'Sign in to save your progress';
        if (bioEl) bioEl.textContent = 'Sign in to create your profile!';
        if (avatarEl) avatarEl.innerHTML = '👤';
        if (commentsEl) commentsEl.textContent = '0';
        if (editBioBtn) editBioBtn.style.display = 'none';
        if (providerEl) providerEl.textContent = '—';
        if (joinedEl) joinedEl.textContent = '—';
    }}
    
    if (chaptersEl) chaptersEl.textContent = readCount;
    if (lastEl) lastEl.textContent = lastChapter || '—';
    if (progressEl) progressEl.textContent = progress + '%';
    
    modal.style.display = 'flex';
}}

function toggleBioEdit() {{
    const bioText = document.getElementById('profile-bio');
    const bioEdit = document.getElementById('bio-edit-container');
    const bioInput = document.getElementById('bio-input');
    
    if (bioEdit.style.display === 'none') {{
        bioInput.value = userProfile?.bio || '';
        bioText.style.display = 'none';
        bioEdit.style.display = 'block';
    }} else {{
        bioText.style.display = 'block';
        bioEdit.style.display = 'none';
    }}
}}

async function saveBio() {{
    if (!currentUser || !db) return;
    
    const bioInput = document.getElementById('bio-input');
    const bioText = document.getElementById('profile-bio');
    const newBio = bioInput.value.trim().substring(0, 200);
    
    try {{
        await db.collection('users').doc(currentUser.uid).update({{ bio: newBio }});
        if (userProfile) userProfile.bio = newBio;
        if (bioText) bioText.textContent = newBio || 'No bio yet. Click Edit to add one!';
        toggleBioEdit();
    }} catch (e) {{
        // If doc doesn't exist, create it
        try {{
            await db.collection('users').doc(currentUser.uid).set({{
                displayName: currentUser.displayName || '',
                username: currentUser.email.split('@')[0],
                bio: newBio,
                createdAt: new Date(),
                commentCount: 0
            }});
            userProfile = {{ bio: newBio }};
            if (bioText) bioText.textContent = newBio || 'No bio yet. Click Edit to add one!';
            toggleBioEdit();
        }} catch (err) {{
            // ignore
        }}
    }}
}}

async function handleAvatarUpload(event) {{
    if (!currentUser) {{
        alert('Please log in first');
        return;
    }}
    if (!db) return;
    
    const file = event.target.files[0];
    if (!file) return;
    if (!file.type.startsWith('image/')) {{
        alert('Please select an image file');
        return;
    }}
    
    // Limit to 2MB source file
    if (file.size > 2 * 1024 * 1024) {{
        alert('Image must be under 2MB');
        return;
    }}
    
    try {{
        // Compress and resize image to base64 (no Storage needed!)
        const dataUrl = await compressImage(file, 150, 0.8);
        
        // Store base64 directly in Firestore
        await db.collection('users').doc(currentUser.uid).set(
            {{ customAvatarUrl: dataUrl }}, 
            {{ merge: true }}
        );
        
        // Update local profile
        if (userProfile) {{
            userProfile.customAvatarUrl = dataUrl;
        }} else {{
            userProfile = {{ customAvatarUrl: dataUrl }};
        }}
        
        // Update avatar display immediately
        const avatarEl = document.getElementById('profile-avatar');
        if (avatarEl) {{
            avatarEl.innerHTML = `<img src=\"${{dataUrl}}\" style=\"width: 100%; height: 100%; border-radius: 50%; object-fit: cover;\" />`;
        }}
        
        alert('Avatar updated!');
    }} catch (e) {{
        alert('Failed to update avatar: ' + (e.message || 'Unknown error'));
    }}
    
    event.target.value = '';
}}

// Compress image to base64 data URL (no Storage required)
function compressImage(file, maxSize, quality) {{
    return new Promise((resolve, reject) => {{
        const reader = new FileReader();
        reader.onload = (e) => {{
            const img = new Image();
            img.onload = () => {{
                const canvas = document.createElement('canvas');
                let width = img.width;
                let height = img.height;
                
                // Scale down to maxSize x maxSize
                if (width > height) {{
                    if (width > maxSize) {{
                        height = Math.round((height * maxSize) / width);
                        width = maxSize;
                    }}
                }} else {{
                    if (height > maxSize) {{
                        width = Math.round((width * maxSize) / height);
                        height = maxSize;
                    }}
                }}
                
                canvas.width = width;
                canvas.height = height;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(img, 0, 0, width, height);
                
                // Convert to JPEG base64
                resolve(canvas.toDataURL('image/jpeg', quality));
            }};
            img.onerror = reject;
            img.src = e.target.result;
        }};
        reader.onerror = reject;
        reader.readAsDataURL(file);
    }});
}}

function showLoginSuccess() {{
    const nameEl = document.getElementById('login-success-name');
    if (nameEl && currentUser) {{
        nameEl.textContent = 'Hello, ' + (currentUser.displayName || currentUser.email.split('@')[0]) + '!';
    }}
    const modal = document.getElementById('login-success-modal');
    if (modal) modal.style.display = 'flex';
}}

function showPopupBlocked() {{
    const el = document.getElementById('popup-blocked-modal');
    if (el) el.style.display = 'flex';
}}

let loginInProgress = false;

function handleLogin() {{
    if (loginInProgress) return;
    
    try {{
        if (typeof firebase === 'undefined' || !firebase.auth) {{
            console.log('Firebase not ready yet');
            showPopupBlocked();
            return;
        }}

        loginInProgress = true;
        const provider = new firebase.auth.GoogleAuthProvider();
        provider.setCustomParameters({{ prompt: 'select_account' }});

        firebase.auth().signInWithPopup(provider)
            .then((result) => {{
                loginInProgress = false;
                if (result && result.user) {{
                    showLoginSuccess();
                }}
            }})
            .catch((err) => {{
                loginInProgress = false;
                console.log('Auth error:', err && err.code, err && err.message);
                // Only show popup-blocked for actual popup issues
                if (err && (err.code === 'auth/popup-blocked' || err.code === 'auth/popup-closed-by-user')) {{
                    showPopupBlocked();
                }}
            }});
    }} catch (e) {{
        loginInProgress = false;
        console.log('Login error:', e && e.message ? e.message : String(e));
        showPopupBlocked();
    }}
}}

async function handleLogout() {{
    try {{
        await firebase.auth().signOut();
    }} catch (e) {{
        console.log('Logout error:', e.message);
    }}
}}

let currentCommentChapter = null;
let currentCommentParagraph = null;

function showCommentModal(chapterNum, paragraphIndex) {{
    if (!currentUser) {{
        alert('Please sign in to comment');
        return;
    }}
    currentCommentChapter = chapterNum;
    currentCommentParagraph = paragraphIndex;
    document.getElementById('comment-text').value = '';
    document.getElementById('comment-modal').style.display = 'block';
}}

async function submitComment() {{
    const text = document.getElementById('comment-text').value.trim();
    if (!text || !currentUser || !db) {{
        alert('Error: Could not submit comment');
        return;
    }}
    
    try {{
        await db.collection('comments').add({{
            chapter: currentCommentChapter,
            paragraph: currentCommentParagraph,
            userId: currentUser.uid,
            email: currentUser.email,
            text: text,
            timestamp: new Date(),
            likes: 0
        }});
        document.getElementById('comment-modal').style.display = 'none';
        loadComments();
    }} catch (e) {{
        alert('Error posting comment: ' + e.message);
    }}
}}

async function loadComments() {{
    if (!db) return;
    
    const chapterNum = document.querySelector('[data-chapter]')?.dataset.chapter;
    if (!chapterNum) return;
    
    try {{
        const snapshot = await db.collection('comments')
            .where('chapter', '==', parseInt(chapterNum))
            .orderBy('timestamp', 'desc')
            .get();
        
        const paragraphs = document.querySelectorAll('.chapter-paragraph');
        paragraphs.forEach((p, idx) => {{
            const commentsBucket = p.querySelector('.paragraph-comments');
            if (commentsBucket) commentsBucket.remove();
            
            const paraComments = snapshot.docs.filter(doc => doc.data().paragraph === idx);
            if (paraComments.length > 0) {{
                const container = document.createElement('div');
                container.className = 'paragraph-comments';
                container.style.cssText = `
                    margin-top: 1rem;
                    padding: 1rem;
                    background: rgba(255, 255, 255, 0.03);
                    border-left: 2px solid var(--secondary);
                    border-radius: 0;
                    font-size: 0.9rem;
                `;
                
                paraComments.forEach(doc => {{
                    const data = doc.data();
                    const commentEl = document.createElement('div');
                    commentEl.style.marginBottom = '0.75rem';
                    commentEl.innerHTML = `
                        <div style="color: var(--primary); font-weight: 500;">${{data.email.split('@')[0]}}</div>
                        <div style="color: var(--text-light); font-size: 0.8rem; margin-bottom: 0.25rem;">${{new Date(data.timestamp.toDate()).toLocaleDateString()}}</div>
                        <div>${{data.text}}</div>
                    `;
                    container.appendChild(commentEl);
                }});
                
                p.parentNode.insertBefore(container, p.nextSibling);
            }}
        }});
    }} catch (e) {{
        console.log('Comments not available:', e.message);
    }}
}}

// Setup event listeners and handlers
document.addEventListener('DOMContentLoaded', () => {{
    // Auth handlers
    const loginBtn = document.getElementById('login-btn');
    const logoutBtn = document.getElementById('logout-btn');
    if (loginBtn) loginBtn.addEventListener('click', handleLogin);
    if (logoutBtn) logoutBtn.addEventListener('click', handleLogout);
    
    // Comment system: add click handlers to paragraphs
    document.querySelectorAll('.chapter-paragraph').forEach((p, idx) => {{
        p.style.cursor = 'pointer';
        p.addEventListener('click', () => {{
            showCommentModal(document.querySelector('[data-chapter]')?.dataset.chapter, idx);
        }});
    }});
    
    // Initialize Firebase
    initFirebase();
}});

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
                <a href="https://www.webnovel.com/book/shadow-slave_17505878106372705" target="_blank" rel="noopener">🔗 Official Webnovel</a>
                <div id="auth-container" style="display: flex; align-items: center; gap: 0.5rem;">
                    <button id="login-btn" class="btn btn-sm" style="background: var(--secondary);" onclick="handleLogin()">Sign In</button>
                    <button id="profile-btn" class="btn btn-sm" style="background: var(--primary); display: none;" onclick="showProfile()">👤 Profile</button>
                    <button id="logout-btn" class="btn btn-sm" style="background: var(--accent); display: none;" onclick="handleLogout()">Sign Out</button>
                </div>
            </div>
        </nav>
    </header>
    <main{main_class}>
        {content}
    </main>
    {chat_widget}
    <div id="comment-modal" class="modal" style="display: none;">
        <div class="modal-content">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                <h3>Add Comment</h3>
                <button class="close-btn" onclick="document.getElementById('comment-modal').style.display = 'none';">&times;</button>
            </div>
            <textarea id="comment-text" placeholder="Write your comment..." style="width: 100%; min-height: 100px; padding: 0.75rem; background: var(--card-bg); border: 1px solid var(--border); color: var(--text); border-radius: var(--radius); font-family: inherit; margin-bottom: 1rem; resize: vertical;"></textarea>
            <button id="submit-comment-btn" class="btn" onclick="submitComment()">Post Comment</button>
        </div>
    </div>
    <div id="profile-modal" class="modal" style="display: none;">
        <div class="modal-content" style="max-width: 480px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem;">
                <h3>👤 Your Profile</h3>
                <button class="close-btn" onclick="document.getElementById('profile-modal').style.display = 'none';">&times;</button>
            </div>
            
            <!-- Profile Header -->
            <div style="text-align: center; margin-bottom: 1.5rem;">
                <div style="position: relative; width: 100px; height: 100px; margin: 0 auto 1rem;">
                    <div id="profile-avatar" style="width: 100%; height: 100%; border-radius: 50%; background: var(--secondary); display: flex; align-items: center; justify-content: center; font-size: 2.5rem; overflow: hidden;">👤</div>
                    <button id="avatar-upload-btn" onclick="document.getElementById('avatar-file-input').click()" style="position: absolute; bottom: 0; right: 0; width: 32px; height: 32px; border-radius: 50%; background: var(--primary); border: 2px solid var(--dark-bg); cursor: pointer; display: flex; align-items: center; justify-content: center; font-size: 0.8rem; padding: 0; color: var(--dark-bg);" title="Change avatar">📷</button>
                    <input type="file" id="avatar-file-input" accept="image/*" style="display: none;" onchange="handleAvatarUpload(event)">
                </div>
                <div id="profile-display-name" style="font-size: 1.5rem; font-weight: 700; margin-bottom: 0.25rem;"></div>
                <div id="profile-username" style="color: var(--primary); font-size: 0.95rem; margin-bottom: 0.5rem;"></div>
                <div id="profile-email" style="color: var(--text-light); font-size: 0.85rem;"></div>
            </div>
            
            <!-- Bio Section -->
            <div id="profile-bio-section" style="background: rgba(255,255,255,0.03); padding: 1rem; border-radius: var(--radius); margin-bottom: 1rem;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                    <span style="font-weight: 600; font-size: 0.85rem; color: var(--text-light);">BIO</span>
                    <button id="edit-bio-btn" class="btn btn-sm" style="padding: 0.25rem 0.5rem; font-size: 0.75rem;" onclick="toggleBioEdit()">Edit</button>
                </div>
                <p id="profile-bio" style="color: var(--text); font-size: 0.9rem; line-height: 1.5; margin: 0;">No bio yet...</p>
                <div id="bio-edit-container" style="display: none;">
                    <textarea id="bio-input" placeholder="Tell us about yourself..." style="width: 100%; min-height: 80px; padding: 0.75rem; background: var(--card-bg); border: 1px solid var(--border); color: var(--text); border-radius: var(--radius); font-family: inherit; margin-bottom: 0.5rem; resize: vertical;"></textarea>
                    <div style="display: flex; gap: 0.5rem;">
                        <button class="btn btn-sm" style="flex: 1;" onclick="saveBio()">Save</button>
                        <button class="btn btn-sm" style="flex: 1; background: var(--border);" onclick="toggleBioEdit()">Cancel</button>
                    </div>
                </div>
            </div>
            
            <!-- Reading Stats -->
            <div style="background: rgba(255,255,255,0.03); padding: 1rem; border-radius: var(--radius); margin-bottom: 1rem;">
                <div style="font-weight: 600; font-size: 0.85rem; color: var(--text-light); margin-bottom: 0.75rem;">📊 READING STATS</div>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.75rem;">
                    <div style="text-align: center; padding: 0.75rem; background: rgba(255,255,255,0.03); border-radius: var(--radius);">
                        <div id="profile-chapters" style="font-size: 1.5rem; font-weight: 700; color: var(--primary);">0</div>
                        <div style="font-size: 0.75rem; color: var(--text-light);">Chapters Read</div>
                    </div>
                    <div style="text-align: center; padding: 0.75rem; background: rgba(255,255,255,0.03); border-radius: var(--radius);">
                        <div id="profile-last" style="font-size: 1.5rem; font-weight: 700; color: var(--secondary);">—</div>
                        <div style="font-size: 0.75rem; color: var(--text-light);">Last Chapter</div>
                    </div>
                    <div style="text-align: center; padding: 0.75rem; background: rgba(255,255,255,0.03); border-radius: var(--radius);">
                        <div id="profile-progress" style="font-size: 1.5rem; font-weight: 700; color: var(--success);">0%</div>
                        <div style="font-size: 0.75rem; color: var(--text-light);">Progress</div>
                    </div>
                    <div style="text-align: center; padding: 0.75rem; background: rgba(255,255,255,0.03); border-radius: var(--radius);">
                        <div id="profile-comments" style="font-size: 1.5rem; font-weight: 700; color: var(--warning);">0</div>
                        <div style="font-size: 0.75rem; color: var(--text-light);">Comments</div>
                    </div>
                </div>
            </div>
            
            <!-- Account Info -->
            <div style="background: rgba(255,255,255,0.03); padding: 1rem; border-radius: var(--radius); margin-bottom: 1.5rem;">
                <div style="font-weight: 600; font-size: 0.85rem; color: var(--text-light); margin-bottom: 0.75rem;">⚙️ ACCOUNT</div>
                <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem; font-size: 0.9rem;">
                    <span style="color: var(--text-light);">Provider</span>
                    <span id="profile-provider" style="color: var(--text);">Google</span>
                </div>
                <div style="display: flex; justify-content: space-between; font-size: 0.9rem;">
                    <span style="color: var(--text-light);">Member Since</span>
                    <span id="profile-joined" style="color: var(--text);">—</span>
                </div>
            </div>
            
            <button class="btn" style="background: var(--accent); width: 100%;" onclick="handleLogout(); document.getElementById('profile-modal').style.display = 'none';">Sign Out</button>
        </div>
    </div>
    <div id="login-success-modal" class="modal" style="display: none;">
        <div class="modal-content" style="text-align: center;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">✅</div>
            <h3 style="margin-bottom: 0.5rem;">Welcome!</h3>
            <p id="login-success-name" style="color: var(--text-light); margin-bottom: 1.5rem;"></p>
            <p style="margin-bottom: 1.5rem;">You're now signed in. You can comment on chapters and your progress will be synced.</p>
            <button class="btn" style="width: 100%;" onclick="document.getElementById('login-success-modal').style.display = 'none';">Continue Reading</button>
        </div>
    </div>
    <div id="popup-blocked-modal" class="modal" style="display: none;">
        <div class="modal-content" style="text-align: center;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">🪟</div>
            <h3 style="margin-bottom: 0.5rem;">Sign-in couldn’t start</h3>
            <p style="color: var(--text-light); margin-bottom: 1.25rem;">
                If your browser blocked the sign-in popup, allow popups for this site and try again.
            </p>
            <button class="btn" style="width: 100%;" onclick="document.getElementById('popup-blocked-modal').style.display = 'none';">OK</button>
        </div>
    </div>
    <script src="https://www.gstatic.com/firebasejs/9.23.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/9.23.0/firebase-auth-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/9.23.0/firebase-firestore-compat.js"></script>
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
    
    <div class="disclaimer-banner">
        <p>⚠️ <strong>Note:</strong> The wiki is very iffy, so don't take all the info to heart.</p>
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
    content_html = '\n'.join(f'<p class="chapter-paragraph">{p.strip()}</p>' for p in paragraphs if p.strip())
    
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
            <div class="tts-controls" data-tts>
                <button class="tts-btn tts-play" type="button">🔊 Play</button>
                <button class="tts-btn tts-pause" type="button">⏸ Pause</button>
                <button class="tts-btn tts-resume" type="button">▶ Resume</button>
                <button class="tts-btn tts-stop" type="button">⏹ Stop</button>
                <span class="tts-rate-label">Speed
                    <select class="tts-rate">
                        <option value="0.85">0.85×</option>
                        <option value="1" selected>1×</option>
                        <option value="1.15">1.15×</option>
                        <option value="1.3">1.3×</option>
                    </select>
                </span>
                <span class="tts-unsupported" style="display:none;">(TTS not supported in this browser)</span>
            </div>
        </div>
        
        <div class="chapter-content" data-chapter="{chapter['chapter_number']}">
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

def generate_auth_popup():
    # Minimal helper page for popup-based auth:
    # - Opens in a small window
    # - Runs signInWithRedirect inside the popup
    # - On success, signals the main window via BroadcastChannel/localStorage and closes
    return '''
    <div class="login-container" style="max-width: 520px;">
        <h1>🔐 Signing you in…</h1>
        <p style="color: var(--text-light); margin-top: 0.5rem;">
            If this window doesn’t close automatically, finish the Google sign-in and return.
        </p>
        <div class="login-info" style="margin-top: 1.5rem;">
            <p><strong>Tip:</strong> If you don’t see Google sign-in, allow popups for this site.</p>
        </div>
        <button class="btn" style="margin-top: 1.5rem;" onclick="window.close()">Close</button>
    </div>

    <script src="https://www.gstatic.com/firebasejs/9.23.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/9.23.0/firebase-auth-compat.js"></script>
    <script>
    (function () {
        const FirebaseConfig = {
            apiKey: "AIzaSyAx2KtNj6znY8ivypcV5fcQzeNzntevKMU",
            authDomain: "shadowslaveread.firebaseapp.com",
            projectId: "shadowslaveread",
            storageBucket: "shadowslaveread.appspot.com",
            messagingSenderId: "956677381164",
            appId: "1:956677381164:web:04832a90c7b82402cbc589"
        };

        try {
            firebase.initializeApp(FirebaseConfig);
        } catch (e) {
            // ignore double-init
        }

        const provider = new firebase.auth.GoogleAuthProvider();
        provider.setCustomParameters({ prompt: 'select_account' });

        function signalSuccess() {
            try {
                if ('BroadcastChannel' in window) {
                    new BroadcastChannel('ss-auth').postMessage({ type: 'login-success', t: Date.now() });
                }
            } catch (e) {}
            try {
                localStorage.setItem('ss-auth-event', JSON.stringify({ type: 'login-success', t: Date.now() }));
            } catch (e) {}
        }

        firebase.auth().getRedirectResult().then((result) => {
            if (result && result.user) {
                signalSuccess();
                setTimeout(() => window.close(), 250);
                return;
            }
            // Start the redirect flow inside the popup.
            return firebase.auth().signInWithRedirect(provider);
        }).catch((err) => {
            console.log('Auth popup error:', err && err.code, err && err.message);
        });
    })();
    </script>
    '''

def generate_auth_popup_standalone():
    """
    Returns a COMPLETE standalone HTML page for auth.html.
    This is NOT wrapped by render() because we need a minimal page
    without main.js or duplicate Firebase scripts.
    """
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign In - Shadow Slave</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <header>
        <nav>
            <a href="index.html" class="logo">📖 Shadow Slave</a>
            <div class="nav-links">
                <a href="chapter-list.html">📚 Chapters</a>
            </div>
        </nav>
    </header>
    <main>
        <div class="login-container" style="max-width: 520px;">
            <h1>🔐 Signing you in…</h1>
            <p style="color: var(--text-light); margin-top: 0.5rem;">
                If this window doesn't close automatically, finish the Google sign-in and return.
            </p>
            <div class="login-info" style="margin-top: 1.5rem;">
                <p><strong>Tip:</strong> If you don't see Google sign-in, allow popups for this site.</p>
            </div>
            <button class="btn" style="margin-top: 1.5rem;" onclick="window.close()">Close</button>
        </div>
    </main>

    <script src="https://www.gstatic.com/firebasejs/9.23.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/9.23.0/firebase-auth-compat.js"></script>
    <script>
    (function () {
        const FirebaseConfig = {
            apiKey: "AIzaSyAx2KtNj6znY8ivypcV5fcQzeNzntevKMU",
            authDomain: "shadowslaveread.firebaseapp.com",
            projectId: "shadowslaveread",
            storageBucket: "shadowslaveread.appspot.com",
            messagingSenderId: "956677381164",
            appId: "1:956677381164:web:04832a90c7b82402cbc589"
        };

        try {
            firebase.initializeApp(FirebaseConfig);
        } catch (e) {
            // ignore double-init
        }

        const provider = new firebase.auth.GoogleAuthProvider();
        provider.setCustomParameters({ prompt: 'select_account' });

        function signalSuccess() {
            try {
                if ('BroadcastChannel' in window) {
                    new BroadcastChannel('ss-auth').postMessage({ type: 'login-success', t: Date.now() });
                }
            } catch (e) {}
            try {
                localStorage.setItem('ss-auth-event', JSON.stringify({ type: 'login-success', t: Date.now() }));
            } catch (e) {}
        }

        firebase.auth().getRedirectResult().then((result) => {
            if (result && result.user) {
                signalSuccess();
                setTimeout(() => window.close(), 250);
                return;
            }
            // Start the redirect flow inside the popup.
            return firebase.auth().signInWithRedirect(provider);
        }).catch((err) => {
            console.log('Auth popup error:', err && err.code, err && err.message);
        });
    })();
    </script>
</body>
</html>'''

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

    # Auth popup helper (standalone, no main.js)
    (OUTPUT_DIR / 'auth.html').write_text(generate_auth_popup_standalone())
    print("   ✓ auth.html")
    
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
