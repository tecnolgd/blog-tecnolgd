#!/usr/bin/env python3
"""
Minimalist Blog Post Generator
- Only generates NEW post files (never overwrites existing ones - they're immutable)
- Updates index.html with all posts
- Safe to run multiple times (idempotent)
- Philosophy: Old posts are permanent - write new ones instead of editing
"""

import json
import os

def load_posts():
    """Load posts from posts_data.json"""
    with open('posts_data.json', 'r') as f:
        return json.load(f)['posts']

def load_template():
    """Load the post template"""
    with open('post_template.html', 'r') as f:
        return f.read()

def generate_post_html(post, template):
    """Generate HTML for a single post"""
    html = template
    html = html.replace('{{TITLE}}', post['title'])
    html = html.replace('{{AUTHOR}}', post['author'])
    html = html.replace('{{DATE}}', post['date'])
    html = html.replace('{{CATEGORY}}', post['category'])
    html = html.replace('{{CONTENT}}', post['content'])
    return html

def generate_or_skip_post(post, html):
    """Create post file only if it doesn't exist (immutable)"""
    filename = f"post-{post['id']}.html"
    if os.path.exists(filename):
        print(f"⊘ Skipping post-{post['id']}.html (immutable - already exists)")
        return False
    else:
        with open(filename, 'w') as f:
            f.write(html)
        print(f"✓ Created post-{post['id']}.html")
        return True

def generate_index_cards(posts):
    """Generate blog card HTML for index.html"""
    cards = []
    for post in reversed(posts):  # Newest first
        card = f'''            <a href="post-{post['id']}.html" class="post-card">
                <h3>{post['title']}</h3>
                <p class="post-summary">{post['summary']}</p>
                <p class="post-meta">{post['date']} | <span class="category">{post['category']}</span></p>
            </a>
'''
        cards.append(card)
    return ''.join(cards)

def update_index(cards_html):
    """Update index.html with all post cards"""
    with open('index.html', 'r') as f:
        index = f.read()
    
    # Find and replace between comment markers
    if '<!-- POSTS START -->' in index and '<!-- POSTS END -->' in index:
        start_marker = '<!-- POSTS START -->'
        end_marker = '<!-- POSTS END -->'
        
        start_idx = index.find(start_marker) + len(start_marker)
        end_idx = index.find(end_marker)
        
        new_index = (
            index[:start_idx] + 
            cards_html + '        ' +
            index[end_idx:]
        )
        with open('index.html', 'w') as f:
            f.write(new_index)
        print("✓ Updated index.html with all posts")
    else:
        print("⚠ Warning: Could not find <!-- POSTS START --> and <!-- POSTS END --> in index.html")
        print("  Add these markers to your index.html where you want posts injected")

def main():
    print("=== Minimalist Blog Post Generator ===\n")
    posts = load_posts()
    template = load_template()
    
    created = 0
    skipped = 0
    
    # Generate individual post files (only new ones)
    for post in posts:
        html = generate_post_html(post, template)
        if generate_or_skip_post(post, html):
            created += 1
        else:
            skipped += 1
    
    # Update index.html with all posts
    print()
    cards_html = generate_index_cards(posts)
    update_index(cards_html)
    
    print(f"\n✓ Completed:")
    print(f"  - Created: {created} new posts")
    print(f"  - Skipped: {skipped} existing posts (immutable)")
    print(f"  - Total posts: {len(posts)}")
    print(f"\n💡 Remember: Never edit old posts - write new ones instead!")

if __name__ == '__main__':
    main()
