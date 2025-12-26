#!/usr/bin/env python
"""Regenerate chapters_data.json with improved extraction."""
from web_novel_scraper.epub_extractor import extract_epub_data
import json
from pathlib import Path
import sys

epub_path = '/workspaces/sumthsumthsdw/Shadow Slave Chapters 1 - 2720.epub'

print("📖 Extracting chapter data from EPUB with improved paragraph spacing...")
try:
    data = extract_epub_data(epub_path)
except Exception as e:
    print(f"❌ Error extracting EPUB: {e}")
    sys.exit(1)

print(f"✅ Extracted: {data['metadata']['title']}")
print(f"📚 Total chapters: {len(data['chapters'])}")

# Show first chapter to verify paragraph spacing
print("\n=== Chapter 1 content preview (first 600 chars) ===")
ch1_content = data['chapters'][0]['content']
print(repr(ch1_content[:600]))

# Count paragraphs in chapter 1
double_newlines = ch1_content.count('\n\n')
print(f"\n✓ Chapter 1 has {double_newlines} paragraph breaks")

# Save to JSON
print("\n💾 Saving to chapters_data.json...")
output_path = Path(epub_path).parent / 'chapters_data.json'
try:
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✅ Successfully saved {len(data['chapters'])} chapters to {output_path}")
except Exception as e:
    print(f"❌ Error saving JSON: {e}")
    sys.exit(1)

print("\n🎉 Done! Restart the Flask app to load the updated chapters.")
