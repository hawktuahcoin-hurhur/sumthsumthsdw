/**
 * Main JavaScript for Novel Reader
 */

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    console.log('Novel Reader initialized');
    
    // Add any global event listeners
    setupGlobalListeners();
});

function setupGlobalListeners() {
    // Add keyboard shortcuts
    document.addEventListener('keydown', (e) => {
        // Arrow keys for chapter navigation
        if (e.key === 'ArrowRight') {
            const nextBtn = document.querySelector('.nav-button:last-child a');
            if (nextBtn) nextBtn.click();
        } else if (e.key === 'ArrowLeft') {
            const prevBtn = document.querySelector('.nav-button:first-child a');
            if (prevBtn) prevBtn.click();
        }
    });
}

/**
 * API utilities
 */
async function apiFetch(endpoint, options = {}) {
    try {
        const response = await fetch(endpoint, options);
        if (!response.ok) throw new Error(`API error: ${response.status}`);
        return await response.json();
    } catch (error) {
        console.error('API error:', error);
        return null;
    }
}

/**
 * Search functionality
 */
async function performSearch(query, type = 'text') {
    if (!query) return [];
    
    const endpoint = type === 'semantic' 
        ? `/api/semantic-search?q=${encodeURIComponent(query)}`
        : `/api/search?q=${encodeURIComponent(query)}`;
    
    return apiFetch(endpoint);
}

/**
 * UI utilities
 */
function showLoading(element) {
    element.innerHTML = '<div class="loading"></div>';
}

function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 1rem;
        background: ${type === 'error' ? '#f44336' : '#4caf50'};
        color: white;
        border-radius: 4px;
        z-index: 1000;
        animation: slideIn 0.3s ease;
    `;
    notification.textContent = message;
    document.body.appendChild(notification);
    
    setTimeout(() => notification.remove(), 3000);
}

/**
 * Chapter utilities
 */
async function loadChapterSummary(chapterId) {
    const data = await apiFetch(`/api/chapter/${chapterId}/summary`);
    if (data && data.summary) {
        return data.summary;
    }
    return null;
}

/**
 * Character utilities
 */
async function loadCharacters(novelId) {
    const data = await apiFetch(`/api/novel/${novelId}/characters`);
    return data || [];
}

/**
 * Recommendation utilities
 */
async function getRecommendations(novelId) {
    const data = await apiFetch(`/api/novel/${novelId}/recommendations`);
    return data || [];
}

/**
 * Text utilities
 */
function highlightText(text, query) {
    const regex = new RegExp(`(${query})`, 'gi');
    return text.replace(regex, '<mark>$1</mark>');
}

/**
 * Local storage utilities
 */
const Storage = {
    setReadingProgress(chapterId, progress) {
        localStorage.setItem(`chapter_${chapterId}_progress`, progress);
    },
    getReadingProgress(chapterId) {
        return parseFloat(localStorage.getItem(`chapter_${chapterId}_progress`) || 0);
    },
    addBookmark(chapterId, chapterTitle) {
        const bookmarks = JSON.parse(localStorage.getItem('bookmarks') || '[]');
        if (!bookmarks.find(b => b.id === chapterId)) {
            bookmarks.push({ id: chapterId, title: chapterTitle, date: new Date().toISOString() });
            localStorage.setItem('bookmarks', JSON.stringify(bookmarks));
        }
    },
    getBookmarks() {
        return JSON.parse(localStorage.getItem('bookmarks') || '[]');
    },
    removeBookmark(chapterId) {
        const bookmarks = JSON.parse(localStorage.getItem('bookmarks') || '[]');
        localStorage.setItem('bookmarks', JSON.stringify(bookmarks.filter(b => b.id !== chapterId)));
    }
};

/**
 * Animation utilities
 */
function fadeIn(element, duration = 300) {
    element.style.opacity = '0';
    element.style.transition = `opacity ${duration}ms ease`;
    setTimeout(() => {
        element.style.opacity = '1';
    }, 10);
}

function fadeOut(element, duration = 300) {
    element.style.transition = `opacity ${duration}ms ease`;
    element.style.opacity = '0';
    setTimeout(() => {
        element.style.display = 'none';
    }, duration);
}

// Export for external use
window.NovelReader = {
    search: performSearch,
    getChapterSummary: loadChapterSummary,
    getCharacters: loadCharacters,
    getRecommendations: getRecommendations,
    showNotification: showNotification,
    storage: Storage,
};
