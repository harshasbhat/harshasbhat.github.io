--[[
  refs-by-type.lua
  Routes bibliography entries into #refs-books, #refs-theses, #refs-chapters, #refs
  by matching the div id (which is "ref-<citekey>") against explicit key sets.
  Edit the sets below to match your bib keys.
]]

local book_keys = {
  ["ref-thomas2017a"] = true,
  ["ref-bizzarri2012"] = true,
}

local chapter_keys = {
  ["ref-thomas2022a"] = true,
  ["ref-thomas2022b"] = true,
}

local thesis_keys = {
  ["ref-cheng2024c"]     = true,
  ["ref-florescuba2023"] = true,
  ["ref-bhat2021"]      = true,
  ["ref-marty2020"]     = true,
  ["ref-okubo2018h"]    = true,
  ["ref-romanet2017b"]  = true,
  ["ref-bhat2007c"]     = true,
}

local function is_div(el, id)
  return el.t == "Div" and el.attr.identifier == id
end

function Pandoc(doc)
  -- Harvest all entries from #refs
  local all_entries = {}
  for i, block in ipairs(doc.blocks) do
    if is_div(block, "refs") then
      for _, entry in ipairs(block.content) do
        table.insert(all_entries, entry)
      end
      -- Clear the main refs div; we'll refill it with articles/etc only
      doc.blocks[i] = pandoc.Div({}, pandoc.Attr("refs", {"references"}, {}))
    end
  end

  if #all_entries == 0 then return doc end

  local books, chapters, theses, rest = {}, {}, {}, {}
  for _, entry in ipairs(all_entries) do
    local id = entry.attr and entry.attr.identifier or ""
    if book_keys[id] then
      table.insert(books, entry)
    elseif chapter_keys[id] then
      table.insert(chapters, entry)
    elseif thesis_keys[id] then
      table.insert(theses, entry)
    else
      table.insert(rest, entry)
    end
  end

  local function fill(blocks, target_id, entries)
    for i, block in ipairs(blocks) do
      if is_div(block, target_id) then
        blocks[i] = pandoc.Div(entries,
          pandoc.Attr(target_id, {"references"}, {}))
        return
      end
    end
  end

  fill(doc.blocks, "refs-books",    books)
  fill(doc.blocks, "refs-chapters", chapters)
  fill(doc.blocks, "refs-theses",   theses)
  fill(doc.blocks, "refs",          rest)

  return doc
end