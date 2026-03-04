--[[
  year-headers.lua
  Inserts a year header + horizontal rule between publication groups
  in #refs, based on the year extracted from the citekey (ref-NAMEYYYYX).
  Run AFTER refs-by-type.lua and reorder-refs.lua (or the hidden-div approach).
  Does NOT apply to #refs-books or #refs-chapters.
]]

local function extract_year(id)
  -- Match 4-digit year in citekey e.g. "ref-cheng2025" → "2025"
  return id:match("(%d%d%d%d)")
end

local function is_div(el, id)
  return el.t == "Div" and el.attr.identifier == id
end

function Pandoc(doc)
  for i, block in ipairs(doc.blocks) do
    if is_div(block, "refs") then
      local new_content = {}
      local current_year = nil

      for _, entry in ipairs(block.content) do
        local id = entry.attr and entry.attr.identifier or ""
        local year = extract_year(id)

        if year and year ~= current_year then
          current_year = year
          -- Insert year header
          table.insert(new_content,
            pandoc.RawBlock("html",
              '<div class="pub-year-header">' .. year .. '</div>'))
        end

        table.insert(new_content, entry)
      end

      local new_div = block:clone()
      new_div.content = new_content
      doc.blocks[i] = new_div
    end
  end
  return doc
end