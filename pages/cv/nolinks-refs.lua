--[[
  nolinks-refs.lua
  Inside every .csl-entry div:
    - Replaces DOI links with plain "· 10.xxxx/yyyy" text
    - Replaces arXiv links with plain "arXiv: 2xxx.xxxxx" text
    - Ensures a space before the token if needed
  The injected DOI extension buttons are stripped by the MutationObserver
  in letterhead.lua.
]]

local function process_link(el)
  local url = el.target

  local doi = url:match("https?://doi%.org/(.+)")
  if doi then
    return pandoc.Str("DOI: " .. doi), true
  end

  local arxiv = url:match("https?://arxiv%.org/abs/(.+)")
             or url:match("https?://arxiv%.org/pdf/(.+)")
  if arxiv then
    return pandoc.Str("arXiv: " .. arxiv), true
  end

  return pandoc.Str(pandoc.utils.stringify(el)), false
end

local function strip_links(inlines)
  local result = {}
  for _, el in ipairs(inlines) do
    if el.t == "Link" then
      local replacement, needs_space = process_link(el)
      if needs_space then
        local prev = result[#result]
        if prev and prev.t == "Str" then
          table.insert(result, pandoc.Space())
        end
      end
      table.insert(result, replacement)
    else
      table.insert(result, el)
    end
  end
  return result
end

function Div(el)
  local found = false
  for _, c in ipairs(el.attr.classes) do
    if c == "csl-entry" then found = true; break end
  end
  if not found then return el end

  local new_blocks = {}
  for _, block in ipairs(el.content) do
    if block.t == "Para" or block.t == "Plain" then
      local nb = block:clone()
      nb.content = strip_links(block.content)
      table.insert(new_blocks, nb)
    else
      table.insert(new_blocks, block)
    end
  end
  el.content = new_blocks
  return el
end
