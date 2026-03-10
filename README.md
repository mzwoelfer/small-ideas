# Blog

A minimal static blog. No build step, no framework. Just HTML + [marked.js](https://marked.js.org/) + Tailwind CDN.

Hosted via GitHub Pages.

## Structure

```
├── index.html           # Homepage — post list + search
├── post.html            # Post renderer (reads ?slug= param)
├── posts/
│   ├── manifest.json    # Post metadata (title, date, tags, description)
│   └── *.md             # Post content with YAML frontmatter
└── assets/              # Images and other static files
```

## Adding a Post

1. Create `posts/your-post-slug.md` with frontmatter:

```markdown
---
title: Your Post Title
date: 2025-04-01
tags: [tag1, tag2]
description: One-line summary shown on the homepage.
---

# Your Post Title

Content here...
```

2. Add an entry to `posts/manifest.json`:

```json
{
  "slug": "your-post-slug",
  "title": "Your Post Title",
  "date": "2025-04-01",
  "tags": ["tag1", "tag2"],
  "description": "One-line summary shown on the homepage."
}
```

## Linking Between Posts

Standard Markdown links work:

```markdown
[See also: SSH hardening](post.html?slug=setting-up-ssh-hardening)
```

Wiki-style links also work and auto-convert:

```markdown
[[SSH Hardening on Linux]]
```

The slug is derived by lowercasing and hyphenating the text.

## Images

Put images in `assets/` and reference them as:

```markdown
![alt text](assets/your-image.png)
```

## GitHub Pages Setup

1. Push to a repo.
2. Go to **Settings → Pages**.
3. Set source to `main` branch, `/ (root)`.
4. Done — no Actions needed.

> The site uses `fetch()` to load posts, which requires a real HTTP server.  
> **It will not work when opened as a local `file://` URL** — use `python3 -m http.server` for local dev.
