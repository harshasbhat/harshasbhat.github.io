--[[
  search-bar.lua
  Injects a live full-text search bar at the top of the publications page.
  Uses position:fixed so it spans the full viewport width, then JS aligns
  the inner content to exactly match the body's computed left/right edges.
  - Hides non-matching entries and their button rows
  - Hides year headers that have no visible entries beneath them
  - Shows a "N results" count
  - Clears on Escape
  - Run as the LAST --lua-filter so all entries are already in the doc
]]

function Pandoc(doc)
  local widget = pandoc.RawBlock("html", [[
<style>
#pub-search-wrap {
  position:      fixed;
  top:           0;
  left:          0;
  right:         0;
  z-index:       100;
  background:    #fff;
  border-bottom: 1px solid #e0e0e0;
  padding:       10pt 0 8pt;
}
#pub-search-inner {
  display:     flex;
  align-items: center;
  gap:         10px;
  /* left/right padding set by JS to match body computed position */
}
#pub-search {
  flex:          1;
  font-family:   var(--font, inherit);
  font-size:     11pt;
  padding:       6pt 12pt;
  border:        1.5px solid var(--my-gray, #a6a6a6);
  border-radius: 4px;
  outline:       none;
  transition:    border-color 0.15s;
  color:         var(--body-color, #1a1a1a);
  background:    #fff;
}
#pub-search:focus { border-color: var(--groy, #057AB2); }
#pub-search-clear {
  display:     none;
  background:  none;
  border:      none;
  cursor:      pointer;
  font-size:   16px;
  color:       var(--my-gray, #a6a6a6);
  padding:     0 2px;
  line-height: 1;
  flex-shrink: 0;
}
#pub-search-clear:hover { color: #333; }
#pub-search-count {
  font-size:   9pt;
  color:       var(--my-gray, #a6a6a6);
  white-space: nowrap;
  flex-shrink: 0;
  min-width:   6em;
  text-align:  right;
}
@media print { #pub-search-wrap { display: none !important; } }
</style>

<div id="pub-search-wrap">
  <div id="pub-search-inner">
    <input id="pub-search" type="search" placeholder="Search publications…"
           autocomplete="off" spellcheck="false" aria-label="Search publications">
    <button id="pub-search-clear" onclick="pubSearchClear()" title="Clear search">&#x2715;</button>
    <span id="pub-search-count"></span>
  </div>
</div>

<script>
(function () {
  var wrap  = document.getElementById('pub-search-wrap');
  var inner = document.getElementById('pub-search-inner');

  // Align the inner content to the body's actual computed edges,
  // accounting for auto margins when viewport > max-width.
  function alignToBody() {
    var bodyRect = document.body.getBoundingClientRect();
    var L = Math.max(bodyRect.left, 0);
    var R = Math.max(window.innerWidth - bodyRect.right, 0);
    inner.style.paddingLeft  = L + 'px';
    inner.style.paddingRight = R + 'px';
    // Push body content down by the bar's actual rendered height
    document.body.style.paddingTop = wrap.offsetHeight + 'px';
  }

  alignToBody();
  window.addEventListener('resize', alignToBody);

  var searchInput = document.getElementById('pub-search');
  var clearBtn    = document.getElementById('pub-search-clear');
  var countSpan   = document.getElementById('pub-search-count');

  function buildIndex() {
    return Array.from(document.querySelectorAll('.csl-entry')).map(function(el) {
      var siblings = [];
      var next = el.nextElementSibling;
      // Only grab pub-btn-row — never touch bibpop divs
      if (next && next.classList.contains('pub-btn-row')) {
        siblings.push(next);
      }
      return { el: el, siblings: siblings, text: el.textContent.toLowerCase() };
    });
  }

  var index = null;

  function runSearch(q) {
    if (!index) index = buildIndex();
    var headers = Array.from(document.querySelectorAll('.pub-year-header'));
    q = q.trim().toLowerCase();

    var total = 0;
    index.forEach(function(item) {
      var show = q === '' || item.text.indexOf(q) !== -1;
      item.el.style.display = show ? '' : 'none';
      item.siblings.forEach(function(s) { s.style.display = show ? '' : 'none'; });
      if (show) total++;
    });

    headers.forEach(function(hdr) {
      var sibling = hdr.nextElementSibling;
      var hasVisible = false;
      while (sibling) {
        if (sibling.classList.contains('pub-year-header')) break;
        if (sibling.classList.contains('csl-entry') && sibling.style.display !== 'none') {
          hasVisible = true; break;
        }
        sibling = sibling.nextElementSibling;
      }
      hdr.style.display = hasVisible ? '' : 'none';
    });

    countSpan.textContent = q === '' ? '' : total + (total === 1 ? ' result' : ' results');
    clearBtn.style.display = q !== '' ? 'inline' : 'none';
  }

  searchInput.addEventListener('input', function() { runSearch(this.value); });
  searchInput.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') pubSearchClear();
  });

  window.pubSearchClear = function() {
    searchInput.value = '';
    runSearch('');
    searchInput.focus();
  };
})();
</script>
]])

  table.insert(doc.blocks, 1, widget)
  return doc
end