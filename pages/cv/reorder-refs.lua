--[[
  reorder-refs.lua
  Reorders bibliography entries in #refs to match the explicit key order
  defined in DESIRED_ORDER below. Entries not in the list go at the end.
  Run this AFTER refs-by-type.lua so that books/chapters are already split out.
]]

-- Exact desired order for PUBLICATIONS (matches PDF/LaTeX nocite order)
local DESIRED_ORDER = {
  "ref-kheirdast2026",
  "ref-garagash2026",
  "ref-gupta2026",
  "ref-cheng2026",
  "ref-zhou2026",
  "ref-wang2026",
  "ref-almakari2026",
  "ref-melkior2025b",
  "ref-michel2026",
  "ref-latour2025",
  "ref-cheng2025",
  "ref-momoh2025",
  "ref-ferry2025",
  "ref-petit2024",
  "ref-jeandet2023a",
  "ref-marty2022",
  "ref-amlani2022",
  "ref-jara2021",
  "ref-elbanna2021",
  "ref-bhat2021",
  "ref-jeandet2020",
  "ref-jolivet2020",
  "ref-okubo2020",
  "ref-okubo2019",
  "ref-marty2019",
  "ref-aubry2018",
  "ref-klinger2018",
  "ref-cruz2018",
  "ref-thomas2018a",
  "ref-romanet2018",
  "ref-gabuchian2017",
  "ref-thomas2017b",
  "ref-passelegue2017",
  "ref-perol2016",
  "ref-passelegue2016b",
  "ref-mello2016",
  "ref-vallage2015",
  "ref-frank2015",
  "ref-siriki2015",
  "ref-mello2014",
  "ref-passelegue2013",
  "ref-bhat2012",
  "ref-bhat2011a",
  "ref-bhat2010a",
  "ref-biegel2010",
  "ref-mello2010",
  "ref-templeton2010",
  "ref-harris2009",
  "ref-sammis2009",
  "ref-templeton2009",
  "ref-dunham2008a",
  "ref-bhat2007a",
  "ref-bhat2007b",
  "ref-bhat2007c",
  "ref-fliss2005",
  "ref-bhat2004",
}

-- Also define order for books and chapters
local BOOKS_ORDER = {
  "ref-thomas2017a",
  "ref-bizzarri2012",
}

local CHAPTERS_ORDER = {
  "ref-thomas2022a",
  "ref-thomas2022b",
}

local function reorder_div(blocks, div_id, order)
  for i, block in ipairs(blocks) do
    if block.t == "Div" and block.attr.identifier == div_id then
      -- Index existing entries by id
      local by_id = {}
      for _, entry in ipairs(block.content) do
        if entry.attr and entry.attr.identifier ~= "" then
          by_id[entry.attr.identifier] = entry
        end
      end
      -- Rebuild in desired order
      local ordered = {}
      for _, id in ipairs(order) do
        if by_id[id] then
          table.insert(ordered, by_id[id])
          by_id[id] = nil
        end
      end
      -- Append any remaining entries not in the order list
      for _, entry in ipairs(block.content) do
        local id = entry.attr and entry.attr.identifier or ""
        if by_id[id] then
          table.insert(ordered, entry)
        end
      end
      -- Replace div content
      local new_div = block:clone()
      new_div.content = ordered
      blocks[i] = new_div
      return
    end
  end
end

function Pandoc(doc)
  reorder_div(doc.blocks, "refs",          DESIRED_ORDER)
  reorder_div(doc.blocks, "refs-books",    BOOKS_ORDER)
  reorder_div(doc.blocks, "refs-chapters", CHAPTERS_ORDER)
  return doc
end
