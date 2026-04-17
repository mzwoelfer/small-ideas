# Blog

Minimal static blog. No build step, no framework. Just HTML + [marked.js](https://marked.js.org/) + Tailwind CDN.

Hosted via GitHub Pages at [mzwoelfer.github.io/small-ideas](https://mzwoelfer.github.io/small-ideas).

## Structure

```
├── index.html                  # Homepage.
├── post.html                   # renders posts (reads ?slug= param)
├── .nojekyll                   # GitHub Pages: serve .md files as-is
├── posts/
│   ├── manifest.json           # Auto-generated post index (do not edit manually)
│   └── *.md                    # Post content
├── assets/                     # Images and other static files
└── .github/
    ├── generate-manifest.py    # Manifest generator script
    ├── hooks/
    │   ├── pre-commit          # Slugifies filenames before commit
    │   └── install.sh          # Run once after cloning
    └── workflows/
        └── generate-manifest.yml  # CI: regenerates manifest, then deploys Pages
```

## Adding a Post

Just drop a `.md` file into `posts/` and push. The CI pipeline handles the rest:

1. Detects the new/changed `.md` file
2. Regenerates `manifest.json` from frontmatter
3. Commits the updated manifest back to `main`
4. Deploys to GitHub Pages

**Do not edit `manifest.json` manually** — it gets overwritten on every push to `posts/`.

### Frontmatter

The script works with Obsidian notes directly. All fields are optional:

```markdown
---
📅 created: 10.03.2026 13:02
tags:
  - libreoffice
  - linux
author: "Martin"
---

## My Post Title

First paragraph becomes the description on the homepage.
```

| Field               | Required | Notes                                                                                                          |
| ------------------- | -------- | -------------------------------------------------------------------------------------------------------------- |
| `title`             | No       | Falls back to first heading, then filename                                                                     |
| `created` or `date` | No       | Accepts `DD.MM.YYYY`, `YYYY-MM-DD`, with or without time. Falls back to `1970-01-01`                           |
| `tags`              | No       | Block list (`- tag`) or inline (`[a, b]`). Obsidian date tags like `March 2026` are filtered out automatically |
| `description`       | No       | Falls back to first paragraph of the post body                                                                 |
| `aliases`, `author` | No       | Parsed but ignored                                                                                             |

Emoji prefixes on keys (e.g. `📅 created`) are handled.

### Filename conventions

Filenames must be kebab-case. The filename becomes the URL slug:

```
posts/my-post-title.md  →  /post.html?slug=my-post-title
```

The pre-commit hook (see below) renames automatically.

## Linking Between Posts

Standard Markdown links:

```markdown
[See also: SSH hardening](post.html?slug=setting-up-ssh-hardening)
```

Wiki-style links (Obsidian compatible). Auto-converted at render time:

```markdown
[[SSH Hardening on Linux]]
```

The slug is derived by lowercasing and hyphenating the link text, so `[[SSH Hardening on Linux]]` resolves to `post.html?slug=ssh-hardening-on-linux`. This must match the `.md` filename exactly.

## Images

Put images in `assets/` and reference them with a relative path:

```markdown
![alt text](assets/my-image.png)
```

Filenames with spaces will break the URL.
Use the pre-commit hook or rename manually to kebab-case.

## Pre-commit Hook

Renames files to kebab-case.
ALl files in `posts/` and `assets/`.

Install once after cloning:

```bash
bash .github/hooks/install.sh
```

If a file gets renamed, the commit is aborted so you can review the changes. Just commit again and it goes through.

> Git hooks are local only. After cloning the repo needs run `install.sh`.

## CI Pipeline

The GitHub Actions workflow in `.github/workflows/generate-manifest.yml` runs two jobs sequentially when a `posts/*.md` file changes:

```
push (posts/*.md changed)
  └── generate   — runs generate-manifest.py, commits manifest.json back to main
        └── deploy — checks out main (with the fresh manifest), deploys to Pages
```

The two jobs are chained with `needs: generate` to avoid a race condition where Pages deploys before the manifest is updated.

**Required GitHub settings:**

- Settings → Actions → General → Workflow permissions → **Read and write permissions**
- Settings → Pages → Source → **GitHub Actions**

## Local Development

The site uses `fetch()` which does not work over `file://`. Serve it locally with:

```bash
python3 -m http.server
```

Then open `http://localhost:8000`.

## Tests

A minimal unit test exists for the pre-commit hook slugification logic. Run it with:

```bash
python3 -m unittest tests/test_pre_commit.py
```
