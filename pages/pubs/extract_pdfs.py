#!/usr/bin/env python3
"""
extract_pdfs.py  —  Extract citekey → PDF URL mappings from MasterBibliography.bib
Reads bdsk-file-* fields (BibDesk bookmarks), decodes the UTF-16 BE relativePathXbookmark
field from the binary plist to get the correct filename (case + accents preserved).
Output: pdf_links.json  { "citekey": "https://filedn.eu/..." }

Usage: python3 extract_pdfs.py MasterBibliography.bib [pdf_links.json]
"""
import sys, re, base64, json, unicodedata

BASE_URL = "https://filedn.eu/lg5rE6ReEB4XtX4pGFBGRh4/CollectedPapers"

FOLDER_RE = re.compile(
    r'(article|book|incollection|inproceedings|phdthesis|mastersthesis|'
    r'techreport|misc|unpublished|conference|proceedings)'
    r'/(.+?\.pdf)',
    re.IGNORECASE
)

# UTF-16 BE markers for each known folder name
FOLDER_MARKERS = [
    b'\x00a\x00r\x00t\x00i\x00c\x00l\x00e',   # article
    b'\x00b\x00o\x00o\x00k',                    # book
    b'\x00i\x00n\x00c\x00o\x00l\x00l',          # incollection
    b'\x00i\x00n\x00p\x00r\x00o\x00c',          # inproceedings
    b'\x00p\x00h\x00d\x00t',                    # phdthesis
    b'\x00m\x00a\x00s\x00t\x00e\x00r',          # mastersthesis
    b'\x00t\x00e\x00c\x00h\x00r',               # techreport
    b'\x00m\x00i\x00s\x00c',                    # misc
    b'\x00u\x00n\x00p\x00u\x00b',               # unpublished
    b'\x00c\x00o\x00n\x00f',                    # conference
    b'\x00p\x00r\x00o\x00c\x00e',               # proceedings
]

def extract_bdsk_path(b64_str):
    """Decode BibDesk bookmark blob; return (folder, filename) with correct case/accents.

    BibDesk stores the relativePathXbookmark value in one of two ways:
      1. ASCII bplist short-string  (newer/simpler entries, no accents):
         The path bytes sit directly in the blob as ASCII, preceded by a
         single-byte length tag (0x5f = '_' for short strings, or 0x10 NN
         for strings up to 255 bytes).  We locate 'article/', 'book/', etc.
         directly as ASCII and read until a NUL or non-printable byte.
      2. UTF-16 BE  (older BibDesk bookmarks, entries with accented names):
         The original decoder below handles this case.
    """
    b64 = re.sub(r'\s+', '', b64_str)
    b64 += '=' * (-len(b64) % 4)
    try:
        raw = base64.b64decode(b64)

        # ── Strategy 1: ASCII path embedded directly in bplist ──────────
        ASCII_FOLDERS = [
            b'article/', b'book/', b'incollection/', b'inproceedings/',
            b'phdthesis/', b'mastersthesis/', b'techreport/', b'misc/',
            b'unpublished/', b'conference/', b'proceedings/',
        ]
        best_idx = len(raw) + 1
        for marker in ASCII_FOLDERS:
            idx = raw.find(marker)
            if 0 <= idx < best_idx:
                best_idx = idx
        if best_idx <= len(raw):
            end = best_idx
            while end < len(raw) and raw[end] >= 0x20 and raw[end] < 0x7f:
                end += 1
            path_ascii = raw[best_idx:end].decode('ascii', errors='replace')
            path_ascii = unicodedata.normalize('NFC', path_ascii)
            m = FOLDER_RE.match(path_ascii)
            if m:
                return m.group(1).lower(), m.group(2)

        # ── Strategy 2: UTF-16 BE (accented filenames) ──────────────────
        best_idx = len(raw) + 1
        for marker in FOLDER_MARKERS:
            idx = raw.find(marker)
            if 0 <= idx < best_idx:
                best_idx = idx
        if best_idx > len(raw):
            return None, None
        path_chars = []
        i = best_idx
        while i + 1 < len(raw):
            hi = raw[i]
            lo = raw[i + 1]
            cp = (hi << 8) | lo
            if cp == 0:
                break
            if cp < 0x20:
                break
            path_chars.append(chr(cp))
            i += 2
        path = unicodedata.normalize('NFC', ''.join(path_chars))
        m = FOLDER_RE.match(path)
        if m:
            return m.group(1).lower(), m.group(2)
    except Exception:
        pass
    return None, None

def url_encode_path(filename):
    """pCloud stores filenames in NFD; percent-encode the UTF-8 bytes of the NFD form."""
    import urllib.parse
    nfd = unicodedata.normalize('NFD', filename)
    safe = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.-_~'
    return urllib.parse.quote(nfd, safe=safe)

def parse_bib(path):
    txt = open(path, encoding='utf-8', errors='replace').read()
    results = {}
    entry_re = re.compile(r'@(\w+)\s*\{\s*([^,\s]+)\s*,', re.MULTILINE)
    for em in entry_re.finditer(txt):
        etype = em.group(1).lower()
        if etype in ('string', 'preamble', 'comment'):
            continue
        key   = em.group(2)
        start = em.end()
        depth = 1
        i     = start
        while i < len(txt) and depth > 0:
            if   txt[i] == '{': depth += 1
            elif txt[i] == '}': depth -= 1
            i += 1
        body = txt[start:i-1]
        for fm in re.finditer(r'bdsk-file-\d+\s*=\s*\{([^}]+(?:\}[^}]*)*?)\}',
                               body, re.DOTALL):
            folder, filename = extract_bdsk_path(fm.group(1))
            if folder and filename:
                url = f"{BASE_URL}/{folder}/{url_encode_path(filename)}"
                results[key] = url
                break
    return results

if __name__ == '__main__':
    bib  = sys.argv[1] if len(sys.argv) > 1 else 'MasterBibliography.bib'
    out  = sys.argv[2] if len(sys.argv) > 2 else 'pdf_links.json'
    links = parse_bib(bib)
    json.dump(links, open(out, 'w'), indent=2, ensure_ascii=False)
    print(f"Found {len(links)} PDF links → {out}", file=sys.stderr)