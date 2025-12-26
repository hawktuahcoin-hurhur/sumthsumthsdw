"""
Extract chapters and metadata from EPUB files.
"""
import re
from pathlib import Path
from ebooklib import epub
from bs4 import BeautifulSoup


def extract_epub_data(epub_path):
    """
    Extract novel metadata and chapters from an EPUB file.
    
    Args:
        epub_path: Path to EPUB file
        
    Returns:
        dict with 'metadata' and 'chapters' keys
    """
    epub_path = Path(epub_path)
    if not epub_path.exists():
        raise FileNotFoundError(f"EPUB file not found: {epub_path}")
    
    book = epub.read_epub(str(epub_path))
    
    # Extract metadata
    metadata = extract_metadata(book)
    
    # Extract chapters
    chapters = extract_chapters(book)
    
    return {
        'metadata': metadata,
        'chapters': chapters,
    }


def extract_metadata(book):
    """Extract novel metadata from EPUB."""
    metadata = {
        'title': 'Unknown',
        'author': 'Unknown',
        'description': '',
        'language': 'en',
        'cover_image': None,
        'tags': [],
    }
    
    # Title
    title_list = book.get_metadata('DC', 'title')
    if title_list:
        metadata['title'] = title_list[0][0]
    
    # Author
    author_list = book.get_metadata('DC', 'creator')
    if author_list:
        metadata['author'] = author_list[0][0]
    
    # Description
    desc_list = book.get_metadata('DC', 'description')
    if desc_list:
        metadata['description'] = desc_list[0][0]
    
    # Language
    lang_list = book.get_metadata('DC', 'language')
    if lang_list:
        metadata['language'] = lang_list[0][0]
    
    # Subject/tags
    subject_list = book.get_metadata('DC', 'subject')
    if subject_list:
        metadata['tags'] = [s[0] for s in subject_list]
    
    # Cover image
    try:
        for item in book.get_items():
            if item.get_type() == epub.ITEM_COVER:
                metadata['cover_image'] = item.get_name()
                break
    except:
        pass
    
    return metadata


def extract_chapters(book):
    """Extract chapters from EPUB book."""
    chapters = []
    chapter_count = 0
    
    # Get HTML items from the book
    html_items = [item for item in book.get_items() if isinstance(item, epub.EpubHtml)]
    
    for item in html_items:
        try:
            content = item.get_content()
            if not content:
                continue
            
            # Parse HTML
            soup = BeautifulSoup(content, 'html.parser')
            
            # Extract title
            title = extract_chapter_title(soup, item.get_name())
            if not title:
                continue
            
            # Extract text content
            text_content = extract_text_content(soup)
            if not text_content or len(text_content.strip()) < 50:
                continue
            
            chapter_count += 1
            
            chapters.append({
                'chapter_number': chapter_count,
                'title': title,
                'content': text_content,
                'raw_html': content.decode('utf-8') if isinstance(content, bytes) else content,
                'url': item.get_name(),
            })
        except Exception as e:
            print(f"Error processing chapter from {item.get_name()}: {e}")
            continue
    
    return chapters


def extract_chapter_title(soup, fallback_name):
    """Extract chapter title from parsed HTML."""
    # Try common title tags
    for tag in ['h1', 'h2', 'h3']:
        title_elem = soup.find(tag)
        if title_elem:
            title = title_elem.get_text(strip=True)
            if title:
                # Remove hex strings at the end (e.g., "21e08487")
                title = re.sub(r'\s+[a-f0-9]{8,}$', '', title, flags=re.IGNORECASE)
                # Properly capitalize title
                title = capitalize_title(title)
                return title
    
    # Try to extract from filename
    if fallback_name:
        name = Path(fallback_name).stem
        # Clean up common filename patterns
        name = re.sub(r'[_\-]', ' ', name)
        name = re.sub(r'\d+\.xhtml', '', name)
        # Remove hex strings
        name = re.sub(r'\s+[a-f0-9]{8,}$', '', name, flags=re.IGNORECASE)
        if name and name != 'titlepage':
            # Properly capitalize title
            name = capitalize_title(name)
            return name
    
    return f"Chapter {fallback_name}"


def capitalize_title(title):
    """Capitalize title properly (title case)."""
    if not title:
        return title
    
    # Words that should stay lowercase
    lowercase_words = {'a', 'an', 'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by'}
    
    words = title.split()
    capitalized = []
    
    for i, word in enumerate(words):
        # Always capitalize first word
        if i == 0:
            capitalized.append(word.capitalize())
        # Check if word should be lowercase
        elif word.lower() in lowercase_words:
            capitalized.append(word.lower())
        else:
            capitalized.append(word.capitalize())
    
    return ' '.join(capitalized)


def extract_text_content(soup):
    """Extract clean text content from parsed HTML, preserving paragraph structure."""
    # Remove script and style elements
    for script in soup(['script', 'style']):
        script.decompose()
    
    # Remove common navigation elements
    for nav in soup(['nav', 'header', 'footer']):
        nav.decompose()
    
    # Get body content
    body = soup.find('body')
    if body:
        content = body
    else:
        content = soup
    
    # Extract paragraphs and preserve structure
    paragraphs = []
    for para in content.find_all(['p', 'div', 'blockquote']):
        # Only process paragraphs that are direct children or not nested too deep
        text = para.get_text(strip=True)
        if text and len(text.strip()) > 0:
            paragraphs.append(text)
    
    # Join paragraphs with double newlines for proper spacing
    text = '\n\n'.join(paragraphs)
    
    return text


def calculate_word_count(text):
    """Calculate word count from text."""
    return len(text.split())


def estimate_reading_time(word_count, words_per_minute=250):
    """Estimate reading time in minutes."""
    return max(1, word_count // words_per_minute)
