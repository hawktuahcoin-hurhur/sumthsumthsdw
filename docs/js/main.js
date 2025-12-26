// Shadow Slave Reader - by Guiltythree
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
    const match = window.location.pathname.match(/chapters\/([0-9]+)\.html/);
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
        const match = card.href.match(/chapters\/([0-9]+)\.html/);
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
