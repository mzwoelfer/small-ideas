#!/usr/bin/env python3
"""Scans posts/*.md, parses YAML frontmatter, writes posts/manifest.json sorted by date desc."""

import json
import re
from pathlib import Path

POSTS_DIR = Path(__file__).parent.parent / "posts"


def parse_frontmatter(text):
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return {}
    meta = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip()
        # Parse tag arrays: [a, b, c]
        if val.startswith("[") and val.endswith("]"):
            val = [t.strip().strip("'\"") for t in val[1:-1].split(",") if t.strip()]
        meta[key] = val
    return meta


posts = []
for md_file in POSTS_DIR.glob("*.md"):
    text = md_file.read_text(encoding="utf-8")
    meta = parse_frontmatter(text)
    if not meta.get("title"):
        print(f"  skipping {md_file.name} — no title in frontmatter")
        continue
    posts.append(
        {
            "slug": md_file.stem,
            "title": meta.get("title", md_file.stem),
            "date": meta.get("date", "1970-01-01"),
            "tags": meta.get("tags", []),
            "description": meta.get("description", ""),
        }
    )

posts.sort(key=lambda p: p["date"], reverse=True)

manifest_path = POSTS_DIR / "manifest.json"
manifest_path.write_text(json.dumps(posts, indent=2, ensure_ascii=False) + "\n")
print(f"wrote {manifest_path} with {len(posts)} post(s)")
