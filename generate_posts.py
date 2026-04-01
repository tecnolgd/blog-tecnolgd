#!/usr/bin/env python3
"""
Post Generator - Converts posts_data.json into static HTML files
Run this once to generate all post files and update index.html
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

def save_post_file(post, html):
    """Save post HTML file"""
    filename = f"posts/post-{post['id']}.html"
    with open(filename, 'w') as f:
        f.write(html)
    print(f"✓ Generated {filename}")

def generate_index_cards(posts):
    """Generate blog card HTML for index.html"""
    cards = []
    for post in reversed(posts):  # Newest first
        card = f'''            <a href="posts/post-{post['id']}.html" class="blog-post-card">
                <h3>{post['id']}. {post['title']}</h3>
                <p class="post-meta">Published by {post['author']} on {post['date']} | <span id="articleCat">{post['category']}</span></p>
                <p class="post-summary">{post['summary']}</p>
            </a>
'''
        cards.append(card)
    return ''.join(cards)

def update_index(cards_html):
    """Update index.html with new post cards"""
    with open('index.html', 'r') as f:
        index = f.read()
    
    # Find and replace the post-list section
    start_marker = '            <h2>Latest Blog Posts</h2>'
    end_marker = '            </section>'
    
    start_idx = index.find(start_marker)
    end_idx = index.find(end_marker, start_idx)
    
    if start_idx != -1 and end_idx != -1:
        new_index = (
            index[:start_idx] +
            start_marker + '\n' +
            cards_html +
            index[end_idx:]
        )
        with open('index.html', 'w') as f:
            f.write(new_index)
        print("✓ Updated index.html")

def main():
    print("Generating blog posts...")
    posts = load_posts()
    template = load_template()
    
    # Generate individual post files
    for post in posts:
        html = generate_post_html(post, template)
        save_post_file(post, html)
    
    # Update index.html
    cards_html = generate_index_cards(posts)
    update_index(cards_html)
    
    print(f"\nDone. Generated {len(posts)} posts")

if __name__ == '__main__':
    main()
