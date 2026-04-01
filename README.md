
# In the Shadows

A minimalist blog for devs who value content over frameworks.

## What This Is

Pure HTML + CSS. No JavaScript, no frameworks, no bloat. Built to be:
- **Fast** - Single-digit KB files
- **Readable** - Content-focused design
- **Portable** - Works anywhere, owned by you
- **Maintainable** - One Python script to manage posts
- **Free Hosting** - Hosted via GitHub Pages(The Repo needs to be public for free-tier accounts)

## Quick Start

1. Clone the Repo:
```bash
    git clone https://github.com/tecnolgd/blog-tecnolgd
```
2. Navigate to the project directory
```bash
cd blog-tecnolgd
```

**View locally:** Open `index.html` in any browser.

**Add a new post:**

1. Edit `posts_data.json` - Add your post object
2. Run: `python3 generate_posts.py`
3. Commit the new `post-X.html` file

Done. Script handles everything else (template injection, index updates).

## Project Structure

```
index.html          - Home page (post feed, categories, newsletter)
post-*.html         - Individual post pages (generated)
posts/              - Legacy posts (deprecated, clean up as needed)
posts_data.json     - Single source of truth for all posts
post_template.html  - HTML skeleton for post generation
generate_posts.py   - Automation (only generates missing files)
style.css           - All styling (color, layout, typography)
about.html          - About page
projects.html       - Projects showcase
```

## How Posts Are Generated

**posts_data.json** → **generate_posts.py** → **post-*.html**

Post data lives in one file. Script is idempotent (safe to run multiple times).
Only generates files that don't exist yet. Updates `index.html` with new posts.

## Customization

Edit `style.css` for colors, fonts, layout.

Current palette:
- **Background:** `#fafafa` (light)
- **Text:** `#0a0a0a` (near-black)
- **Accent:** `#1a1a1a` (dark)

Everything else flows from these three.

## Why This Approach

- No git noise from regenerated files
- Own your content (can run offline)
- No vendor lock-in (SQL, frameworks, etc.)
- Minimal moving parts = fewer bugs
- HTML files are portable and timeless