![Static Badge](https://img.shields.io/badge/made_with-HTML_CSS-blue)
![Static Badge](https://img.shields.io/badge/interface-web-teal)
![Static Badge](https://img.shields.io/badge/version-v1.0.0-red)

# In the Shadows 

### Project Name: blog-tecnolgd
### Status: Production Ready (v1.1.0)

This project is a **minimalist, high-performance blog template** built entirely from scratch using **only HTML and CSS**. It was created to demonstrate complete control over the front-end design, prioritizing content, readability, and clean simplicity for technical blogs.

## Signature Features

* **Zero Fluff:** No frameworks, custom JavaScript, or bloated styling. Pure HTML and CSS.
* **Blazing Fast:** Minimal file sizes and immediate rendering for excellent performance.
* **Content-First Design:** Clean typography and layout that keeps focus on your writing, not flashy effects.
* **Responsive Layout:** Works perfectly on mobile, tablet, and desktop using CSS Grid and Flexbox.
* **Subtle Interactions:** Minimal, functional hover effects and transitions—professional, not distracting.
* **Semantic Structure:** Uses modern HTML5 semantics for excellent accessibility and SEO.
* **Easy Integration:** Simple email subscription forms (Formspree) for building an audience without complexity.

## Getting Started
This repository consists of simple static files. To run it, you just need a web browser.

### Prerequisites
* A modern web browser (Chrome, Firefox, Safari, Edge).
* A code editor (VS Code, Sublime Text, etc.).

### Installation

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/tecnolgd/blog-tecnolgd

    cd blogLgd #to open the folder
    ```

2.  **Open the Template:**
    * To view the website: Double-click **`index.html`** in your file explorer.
    * And same tip applies for the other `.html` files.

### Template Files
The repository contains the following core files:

| File Name | Purpose |
| :--- | :--- |
| **`index.html`** | The main blog landing page listing recent articles with newsletter subscription banner. |
| **`post.html`** | Template for viewing a single full article with email subscription CTA. |
| **`about.html`** | About page with author bio and newsletter signup form. |
| **`update.html`** | Projects/updates page with subscription options. |
| **`style.css`** | The complete, hand-written stylesheet for the entire site. **(Customization starts here!)** |

---

## Newsletter Integration

The blog includes optional email subscription forms to help you build an audience:

- **Sidebar newsletter box:** Quiet subscription option on every page
- **Post-article section:** Low-key signup after reading
- **About page:** Simple email capture form

All forms use **Formspree** (free, no JavaScript required). This is optional—remove if you prefer no email collection.

### Setup Email Capture (Optional)

1. Go to [formspree.io](https://formspree.io) and create a free account
2. Create a new form for your email signups
3. Copy your form ID (e.g., `xyzabc123`)
4. Replace `your-form-id` in HTML files: `action="https://formspree.io/f/xyzabc123"`

To remove email forms entirely, just delete the newsletter boxes from the HTML.

---
Your signature is defined by the contents of **`style.css`**.

### 1. Color Scheme

Open `style.css` and modify the CSS variables at the top:

```css
:root {
    --primary-color: #2f7276;        /* Main accent color */
    --primary-light: #5cb3b8;        /* Hover state */
    --text-color: #2b2c2d;           /* Main text */
    --text-light: #666666;           /* Secondary text */
    --background-color: #f8fafb;     /* Page background */
    --content-bg: #e2e9e9;           /* Card background */
    --border-color: #d0d6d6;         /* Borders */
    --font-body: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
    --font-heading: 'Georgia', 'Garamond', serif;
}
```

### 2. Typography
Customize fonts by changing the `--font-body` and `--font-heading` variables. The default uses system fonts for speed and a classic serif heading font for elegance.

### 3. Layout (Content vs. Sidebar)
The main layout uses CSS Grid for the two-column structure (Section 4 in style.css):

```css
.content-container {
    grid-template-columns: 2.5fr 1fr;  /* 2.5 parts Content, 1 part Sidebar */
    /* Adjust these fractions to change the width balance. */
    gap: 48px;
}
```

## Value this repo ?
* If this repository added value to your learning or dev flow ,consider dropping a *⭐*or hitting *fork*.
* Open for recieving feedback and knowledge exchange.

## Credits
Author: ***tecnolgd***
Built with: Boring HTML and CSS with ambition to control every damn pixel 💀.



