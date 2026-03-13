#!/usr/bin/env python3
"""
sync_mypubs.py
--------------
Reads mypubs.txt (one citekey per line, section headers like
"# ── Books / Chapters") and rewrites two files:

  1. pages/cv/cv.md          — the <div style="display:none"> nocite block
  2. pages/cv/refs-by-type.lua — the book_keys and chapter_keys tables

Run from the repo root:
    python3 pages/cv/sync_mypubs.py

The workflow runs this automatically before pandoc.
"""

import re
import sys
from pathlib import Path

# ── Paths: work whether run from repo root or from pages/cv/ ─────────────────
_here  = Path(__file__).resolve().parent   # directory containing this script
_root  = _here.parent.parent               # repo root  (pages/cv/ → pages/ → root)

MYPUBS = _root / "mypubs.txt"
CV_MD  = _here / "cv.md"
LUA    = _here / "refs-by-type.lua"

# ── Section classifier ────────────────────────────────────────────────────────
def classify_section(header: str) -> str:
    h = header.lower()
    if "book" in h or "chapter" in h:
        return "book_chapter"
    if "conference" in h:
        return "conference"
    if "thesis" in h or "theses" in h:
        return "thesis"
    if "other" in h or "misc" in h:
        return "other"
    return "article"   # default / "Articles"

# ── Parse mypubs.txt ──────────────────────────────────────────────────────────
def parse_mypubs(path: Path):
    books, chapters, articles, theses, conferences, others = [], [], [], [], [], []
    current_section = "article"

    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("#"):
            # Section header lines look like:  # ── Books / Chapters ──
            # Plain comments (no section keywords) are just ignored.
            candidate = classify_section(line)
            # Only switch if the comment contains a section keyword
            keywords = ["article", "book", "chapter", "conference",
                        "thesis", "theses", "other", "misc"]
            if any(k in line.lower() for k in keywords):
                current_section = candidate
            continue

        key = line.split()[0]   # ignore anything after whitespace

        if current_section == "book_chapter":
            # Distinguish books from chapters by explicit tag or heuristic
            # (use #book / #chapter inline tags if present, else bucket together)
            if "#chapter" in raw.lower():
                chapters.append(key)
            elif "#book" in raw.lower():
                books.append(key)
            else:
                # No tag — put in a combined list; refs-by-type.lua will handle
                # them as chapters by default (edit tags in mypubs.txt to split)
                chapters.append(key)
        elif current_section == "conference":
            conferences.append(key)
        elif current_section == "thesis":
            theses.append(key)
        elif current_section == "other":
            others.append(key)
        else:
            articles.append(key)

    return dict(books=books, chapters=chapters, articles=articles,
                theses=theses, conferences=conferences, others=others)

# ── 1. Rewrite cv.md nocite block ────────────────────────────────────────────
NOCITE_RE = re.compile(
    r'(<div style="display:none">).*?(</div>)',
    re.DOTALL
)

def rewrite_cv_md(keys: dict, path: Path):
    text = path.read_text(encoding="utf-8")

    all_keys = (
        keys["books"] + keys["chapters"] +
        keys["articles"] + keys["theses"] +
        keys["conferences"] + keys["others"]
    )

    lines = []
    for k in all_keys:
        lines.append(f"@{k}")

    block_content = "\n".join(lines)
    new_div = f'<div style="display:none">\n{block_content}\n</div>'

    if not NOCITE_RE.search(text):
        print("ERROR: could not find <div style=\"display:none\"> block in cv.md", file=sys.stderr)
        sys.exit(1)

    new_text = NOCITE_RE.sub(new_div, text, count=1)
    path.write_text(new_text, encoding="utf-8")
    print(f"  cv.md: updated nocite block ({len(all_keys)} keys)")

# ── 2. Rewrite refs-by-type.lua ───────────────────────────────────────────────
BOOK_TABLE_RE    = re.compile(r'(local book_keys\s*=\s*\{)[^}]*(\})', re.DOTALL)
CHAPTER_TABLE_RE = re.compile(r'(local chapter_keys\s*=\s*\{)[^}]*(\})', re.DOTALL)

def lua_table(keys: list) -> str:
    if not keys:
        return ""
    rows = [f'  ["ref-{k}"] = true,' for k in keys]
    return "\n" + "\n".join(rows) + "\n"

def rewrite_lua(keys: dict, path: Path):
    text = path.read_text(encoding="utf-8")

    book_all = keys["books"] + keys["chapters"]   # both routed through book_keys / chapter_keys
    # Split: if user tagged #book / #chapter we have them split; otherwise chapters bucket holds all
    book_keys_list    = keys["books"]
    chapter_keys_list = keys["chapters"]

    if not BOOK_TABLE_RE.search(text):
        print("ERROR: could not find 'local book_keys' table in refs-by-type.lua", file=sys.stderr)
        sys.exit(1)
    if not CHAPTER_TABLE_RE.search(text):
        print("ERROR: could not find 'local chapter_keys' table in refs-by-type.lua", file=sys.stderr)
        sys.exit(1)

    text = BOOK_TABLE_RE.sub(
        lambda m: m.group(1) + lua_table(book_keys_list) + m.group(2),
        text, count=1
    )
    text = CHAPTER_TABLE_RE.sub(
        lambda m: m.group(1) + lua_table(chapter_keys_list) + m.group(2),
        text, count=1
    )

    path.write_text(text, encoding="utf-8")
    print(f"  refs-by-type.lua: {len(book_keys_list)} books, {len(chapter_keys_list)} chapters")

# ── Main ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    for p in [MYPUBS, CV_MD, LUA]:
        if not p.exists():
            print(f"ERROR: {p} not found (run from repo root)", file=sys.stderr)
            sys.exit(1)

    keys = parse_mypubs(MYPUBS)
    print(f"Parsed mypubs.txt: {sum(len(v) for v in keys.values())} keys total")

    rewrite_cv_md(keys, CV_MD)
    rewrite_lua(keys, LUA)

    print("Done.")