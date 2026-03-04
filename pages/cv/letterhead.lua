--[[
  letterhead.lua
  Injects a letterhead at the top of the document.

  Set the image path in one of two ways:

  1. In cv.md YAML front matter:
       letterhead-image: "/path/to/combinedlogoEN.png"

  2. On the Pandoc command line (overrides YAML):
       --metadata letterhead-image="/path/to/combinedlogoEN.png"

  If the path is empty or not set, a styled text header is shown instead.
]]

function Pandoc(doc)
  -- Safely read the meta value
  local img_path = ""
  local raw = doc.meta["letterhead-image"]
  if raw then
    img_path = pandoc.utils.stringify(raw)
  end
  -- Trim whitespace
  img_path = img_path:match("^%s*(.-)%s*$")

  local header_html

  if img_path ~= "" then
    -- Image letterhead — full page width, exactly like \includegraphics[width=\textwidth]
    header_html =
      '<div class="letterhead">' ..
        '<img src="' .. img_path .. '" alt="Letterhead" style="width:100%;display:block;" />' ..
      '</div>'
  else
    -- Text fallback: name + titles + address + website
    header_html =
      '<div class="cv-text-header">' ..
        '<span class="cv-name">Harsha S. Bhat</span>' ..
        '<div class="cv-titles">' ..
          'Director of Research at CNRS &nbsp;·&nbsp; ' ..
          'Teaching Professor, École Polytechnique' ..
        '</div>' ..
        '<div class="cv-address">' ..
          'Laboratoire de Géologie, 24 Rue Lhomond, 75005 Paris, France' ..
        '</div>' ..
        '<div class="cv-web">' ..
          '<a href="https://harshasbhat.github.io">harshasbhat.github.io</a>' ..
        '</div>' ..
      '</div>'
  end

  -- PDF button (fixed position, hidden on print)
  local btn_html = '<a class="cv-pdf-btn" href="cv.pdf" target="_blank">View PDF</a>'
  table.insert(doc.blocks, pandoc.RawBlock("html", btn_html))



  -- Script to strip DOI extension injections (runs after page load)
  local anti_ext = [[
<script>
(function() {
  // Freeze the text content of every .csl-entry by replacing its
  // innerHTML with a locked shadow copy after the page loads.
  // Any extension that injects <a> or buttons afterwards is undone
  // by the MutationObserver which restores the frozen snapshot.

  function freezeEntries() {
    document.querySelectorAll('.csl-entry').forEach(function(entry) {
      // Save the clean HTML (no extension injections yet)
      var frozen = entry.innerHTML;
      entry._frozenHTML = frozen;

      var obs = new MutationObserver(function() {
        // Suppress observer while we restore
        obs.disconnect();
        entry.innerHTML = entry._frozenHTML;
        // Re-attach after restore
        obs.observe(entry, {childList: true, subtree: true, characterData: true});
      });
      obs.observe(entry, {childList: true, subtree: true, characterData: true});
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', freezeEntries);
  } else {
    freezeEntries();
  }
})();
</script>]]

  table.insert(doc.blocks, pandoc.RawBlock("html", anti_ext))
  table.insert(doc.blocks, 1, pandoc.RawBlock("html", header_html))

  -- Remove the default Pandoc title/subtitle block (replaced by our header)
  doc.meta["title"]    = nil
  doc.meta["subtitle"] = nil

  return doc
end