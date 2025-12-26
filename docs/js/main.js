// Shadow Slave Reader - Static Site JS

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
    const match = window.location.pathname.match(/chapters\/([0-9]+)\.html/);
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
        const match = card.href.match(/chapters\/([0-9]+)\.html/);
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
