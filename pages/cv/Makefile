# ── Paths ────────────────────────────────────────────────────────
CV_DIR   = .
CV_MD    = $(CV_DIR)/cv.md
CV_HTML  = $(CV_DIR)/cv.html
CV_PDF   = $(CV_DIR)/cv.pdf
BIB      = $(HOME)/PcloudPublicFolder/CollectedPapers/MasterBibliography.bib
SYNC     = $(CV_DIR)/sync_mypubs.py

PANDOC_FLAGS = \
  --standalone \
  --citeproc \
  --from markdown+native_spans \
  --css    $(CV_DIR)/cv.css \
  --csl    $(CV_DIR)/author-year.csl \
  --bibliography $(BIB) \
  --lua-filter $(CV_DIR)/letterhead.lua \
  --lua-filter $(CV_DIR)/refs-by-type.lua \
  --lua-filter $(CV_DIR)/year-headers.lua \
  --lua-filter $(CV_DIR)/format-refs.lua \

CHROME = /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome

# ── Targets ──────────────────────────────────────────────────────
.PHONY: all cv pdf clean sync

all: cv pdf

sync:
	python3 $(SYNC)

cv: sync $(CV_HTML)

$(CV_HTML): $(CV_MD) $(CV_DIR)/cv.css $(CV_DIR)/*.lua $(SYNC)
	pandoc $(CV_MD) -o $(CV_HTML) \
	  $(PANDOC_FLAGS) \
	  --embed-resources

pdf: $(CV_PDF)

$(CV_PDF): $(CV_HTML)
	$(CHROME) --headless --disable-gpu \
  --print-to-pdf=$(CV_PDF) \
  --no-margins \
  --virtual-time-budget=5000 \
  "$(CV_HTML)"

clean:
	rm -f $(CV_HTML) $(CV_PDF)