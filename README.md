![Static Badge](https://img.shields.io/badge/made_with-HTML_CSS-blue)
![Static Badge](https://img.shields.io/badge/interface-web-teal)
![Static Badge](https://img.shields.io/badge/version-v1.0.0-red)

# In the Shadows 

### Project Name: blog-tecnolgd
### Status: Production Ready (v1.1.0)

This project is a **minimalist, high-performance blog template** built entirely from scratch using **only HTML and CSS**. It was created to demonstrate complete control over the front-end design, prioritizing speed, readability, and a unique signature aesthetic.

## Signature Features

* **Zero Custom JavaScript:** No frameworks (Bootstrap, Tailwind, etc.), custom JavaScript, or preprocessors. Pure, hand-written HTML and CSS.
* **Blazing Fast:** Designed for minimal file sizes and immediate rendering, resulting in excellent performance.
* **Modern & Sleek Design:** Refined typography, smooth animations, and elegant color palette for a premium feel.
* **Email Subscription System:** Built-in newsletter CTAs on every page to grow your audience (integrates with Formspree).
* **Responsive Layout:** Fully optimized for mobile, tablet, and desktop screens using native CSS Grid and Flexbox.
* **Signature Aesthetic:** Features a distinct color palette and typography (defined in `style.css` variables) to provide a truly unique look.
* **Semantic Structure:** Uses modern HTML5 tags (`<header>`, `<main>`, `<article>`, `<aside>`, `<footer>`) for excellent accessibility and SEO.
* **Smooth Interactions:** Subtle hover effects and transitions for a polished user experience.

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

The blog includes multiple subscription points to help you grow your audience:

- **Homepage banner:** Prominent gradient CTA above recent articles
- **Sidebar newsletter box:** Visible on every page for easy signups
- **Post-article CTA:** Conversion box at the end of articles
- **About page form:** Connect with readers on the about section
- **Updates page banner:** Notify subscribers of new projects

All forms are connected to **Formspree** (a free service that handles email collection with no JavaScript required).

### Setup Email Capture

1. Go to [formspree.io](https://formspree.io) and create a free account
2. Create a new form for your email signups
3. Copy your form ID (e.g., `xyzabc123`)
4. Replace `your-form-id` in all HTML files with your actual Formspree ID

Example in `form action`:
```html
<form class="newsletter-form" action="https://formspree.io/f/xyzabc123" method="POST">
```

---
Your signature is defined by the contents of **`style.css`**.

### 1. Color Scheme

Open `style.css` and modify the CSS variables near the top to instantly change the site's look:

```css
/* 1. CSS Variables for Easy Customization */
:root {
    --primary-color: #2f7276;        /* Main accent color */
    --primary-light: #5cb3b8;        /* Lighter primary for hover states */
    --text-color: #2b2c2d;           /* Main text color */
    --text-light: #666666;           /* Lighter text for meta info */
    --background-color: #f8fafb;     /* Page background */
    --content-bg: #e2e9e9;           /* Card/content background */
    --border-color: #d0d6d6;         /* Subtle borders */
    --font-body: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif;
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



