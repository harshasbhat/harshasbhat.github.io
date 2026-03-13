# ── Paths ────────────────────────────────────────────────────────
PUB_DIR  = .
PUB_MD   = $(PUB_DIR)/pubs.md
PUB_HTML = $(PUB_DIR)/pubs.html
BIB      = $(HOME)/PcloudPublicFolder/CollectedPapers/MasterBibliography.bib
PDF_JSON = $(PUB_DIR)/pdf_links.json

PANDOC_FLAGS = \
  --standalone \
  --citeproc \
  --from markdown+native_spans \
  --css    $(PUB_DIR)/pubs.css \
  --csl    $(PUB_DIR)/author-year.csl \
  --bibliography $(BIB) \
  --lua-filter $(PUB_DIR)/refs-by-type.lua \
  --lua-filter $(PUB_DIR)/year-headers.lua \
  --lua-filter $(PUB_DIR)/format-refs.lua \
  --lua-filter $(PUB_DIR)/pub-buttons.lua\
  --lua-filter $(PUB_DIR)/search-bar.lua

.PHONY: all clean

all: $(PUB_HTML)

$(PDF_JSON): $(BIB)
	python3 $(PUB_DIR)/extract_pdfs.py $(BIB) $(PDF_JSON)

$(PUB_HTML): $(PUB_MD) $(PUB_DIR)/pubs.css $(PUB_DIR)/*.lua $(PDF_JSON)
	pandoc $(PUB_MD) -o $(PUB_HTML) \
	  $(PANDOC_FLAGS) \
	  --embed-resources

clean:
	rm -f $(PUB_HTML) $(PDF_JSON)