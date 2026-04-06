
# In the Shadows

A minimalist blog template for devs who value content over frameworks.

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

1. Edit `posts_data.json` - Add your post data  here
2. Run: `python3 generate_posts.py`
3. Commit the new `post-X.html` file

Done. Script handles everything else (template injection, index updates).

## Project Structure

```
index.html          - Home page (post feed, categories, newsletter)
posts/              - Folder under which posts are created
post-X.html         - Individual post pages (generated)
posts_data.json     - Single source of truth for all posts
post_template.html  - HTML skeleton for post generation
generate_posts.py   - Automation (only generates new files)
style.css           - All styling (color, layout, typography)
about.html          - About page
projects.html       - Projects showcase
```

## How Posts Are Generated

**posts_data.json** → **generate_posts.py** → **post-X.html**

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

## Editing already created post files (Not recommended)

- Edit the contents of the **individual** post-X.html file available in `/posts` as needed.
- Edit the `posts_data.json` file  to match the contents of `post-X.html` file for maintaining consistency.(*Note: This step could be skipped since the live site doesn't depend on what is present in the `posts_data.json` file as it's just used as data for **generating new posts, not updating old ones**.)
- Commit the changes

**Pro Tips:**      
> Make sure to write the post with enough planning to avoid this editing mess. For casual posts or updates which may need/undergo multiple changes, it's recommended to use `projects.html` file.         

> Use simple indexing(e.g., "#1" for post-1 of topic 'X' and so on) for subsequent posts regarding the same topic or domain for a clear flow of posts for improved readability.  