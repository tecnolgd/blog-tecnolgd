
<h1 align = "center" style = "font-family: Georgia, serif; font-size: 40px">In the Shadows</h1>

<div align="center">
  <a href="LICENSE.md">
    <img src="https://img.shields.io/github/license/tecnolgd/blog-tecnolgd?color=1a1a1a&style=flat-square" alt="License(MIT)">
  </a>
  <a href="https://github.com/tecnolgd/blog-tecnolgd/releases">
    <img src="https://img.shields.io/github/v/release/tecnolgd/blog-tecnolgd?color=1a1a1a&style=flat-square" alt="Version">
  </a>
  <a href="https://github.com/tecnolgd/blog-tecnolgd/deployments">
    <img src="https://img.shields.io/github/deployments/tecnolgd/blog-tecnolgd/github-pages?color=1a1a1a&label=deployments&style=flat-square" alt="Deployments">
  </a>
  <img src="https://img.shields.io/badge/architecture-static_site-1a1a1a?style=flat-square" alt="Static Site">
  <img src="https://img.shields.io/badge/dependencies-zero-1a1a1a?style=flat-square" alt="Zero Frameworks">
  
</div>

A minimalist blog for devs who value content over frameworks.

## Key Features

- **Zero-Framework Minimalism**: Low-bloat architecture
- **Pure Markdown Content**: Text over Tags
- **Built-in RSS Feed**: Decentralized content syndication
- **Optimized Dark Mode**: Customized theme for tecnical legibility.
- **No-Maintenance Deployment**: Near-Zero config hell, thanks to page native processing via Jekyll.

## Setup

1. Clone the repo.
    ```bash
      git clone https://github.com/tecnolgd/blog-tecnolgd.git
    ```
    ```bash
      cd blog-tecnolgd
    ```
2. Edit `_config.yml` to set your theme.

- My chosen theme
  ```yml
  remote_theme: jekyll/minima

  minima:
  skin: dark
  ```
- Some theme ideas:
  - jekyll-theme-tactile
  - jekyll-theme-hacker
  - jekyll-theme-midnight

3. Write your posts as pure text(`.md` files) inside the `posts/` directory.


## Deployment

Hosted automatically via GitHub Pages using the `architect` theme engine.


## License

[MIT](LICENSE.md)