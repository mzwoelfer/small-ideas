#!/usr/bin/env python3
"""Scans posts/*.md, parses YAML frontmatter, writes posts/manifest.json sorted by date desc.

Handles Obsidian-style frontmatter:
- title: falls back to first H1 in the document, then filename
- date: accepts ISO (2026-03-10), German (10.03.2026), and datetime (2026-03-10 13:02) formats
- tags: accepts YAML block lists (- tag) and inline lists ([a, b, c])
- aliases: ignored (Obsidian metadata)
- description: falls back to first non-heading paragraph
"""

import json
import re
from pathlib import Path

POSTS_DIR = Path(__file__).parent.parent / "posts"


def parse_tags(val, lines, start_index):
    val = val.strip()
    if val.startswith("[") and val.endswith("]"):
        return [t.strip().strip("'\"") for t in val[1:-1].split(",") if t.strip()]
    tags = []
    if not val:
        for line in lines[start_index:]:
            m = re.match(r"^\s+-\s+(.+)", line)
            if m:
                tags.append(m.group(1).strip())
            elif line.strip() and not line.startswith(" "):
                break
    return tags


def parse_date(val):
    val = val.strip()
    val = re.split(r"[ T]", val)[0]
    m = re.match(r"^(\d{2})\.(\d{2})\.(\d{4})$", val)
    if m:
        return f"{m.group(3)}-{m.group(2)}-{m.group(1)}"
    if re.match(r"^\d{4}-\d{2}-\d{2}$", val):
        return val
    return "1970-01-01"


def first_heading(text):
    for line in text.splitlines():
        m = re.match(r"^#+\s+(.+)", line)
        if m:
            title = m.group(1).strip()
            title = re.sub(r"\[\[(.+?)\]\]", r"\1", title)
            return title
    return ""


def first_paragraph(text):
    para = []
    for line in text.splitlines():
        if line.startswith("#"):
            if para:
                break
            continue
        if line.strip() == "":
            if para:
                break
            continue
        para.append(line.strip())
    return " ".join(para)[:200]


def parse_frontmatter(text):
    match = re.match(r"^---\n(.*?)\n---\n?([\s\S]*)", text, re.DOTALL)
    if not match:
        return {}, text
    fm_text = match.group(1)
    body = match.group(2)
    lines = fm_text.splitlines()
    meta = {}
    i = 0
    while i < len(lines):
        line = lines[i]
        if ":" not in line:
            i += 1
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        key = re.sub(r"^[^\w]+", "", key).strip()  # strip leading emoji/non-word chars
        val = val.strip()
        if key == "tags":
            meta["tags"] = parse_tags(val, lines, i + 1)
        else:
            meta[key] = val
        i += 1
    return meta, body


def slugify(name):
    slug = name.lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "-", slug)
    slug = re.sub(r"-+", "-", slug)
    return slug.strip("-")


posts = []
for md_file in POSTS_DIR.glob("*.md"):
    text = md_file.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(text)

    title = meta.get("title") or first_heading(body) or md_file.stem
    raw_date = meta.get("created") or meta.get("date") or ""
    date = parse_date(raw_date) if raw_date else "1970-01-01"
    tags = [t for t in meta.get("tags", []) if not re.match(r"^[A-Z][a-z]+ \d{4}$", t)]
    description = meta.get("description") or first_paragraph(body)
    slug = slugify(md_file.stem)

    posts.append(
        {
            "slug": slug,
            "title": title,
            "date": date,
            "tags": tags,
            "description": description,
        }
    )
    print(f"  + {md_file.name} → slug={slug}, date={date}, title={title}")

posts.sort(key=lambda p: p["date"], reverse=True)

manifest_path = POSTS_DIR / "manifest.json"
manifest_path.write_text(json.dumps(posts, indent=2, ensure_ascii=False) + "\n")
print(f"\nwrote {manifest_path} with {len(posts)} post(s)")
