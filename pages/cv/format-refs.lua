--[[
  format-refs.lua
  Inside every .csl-entry div (produced by --citeproc):
    - Bolds and underlines "Bhat, H. S." wherever it appears
    - Renders title in bold+italic
    - Colors journal name in Harvard crimson (#C90016)
    - Drops volume:page tokens (e.g. "126:1-20.")
    - Ensures a space before the DOI link
]]

local harvard = "#C90016"

local function raw(html)
  return pandoc.RawInline("html", html)
end

local function process_inlines(inlines)
  local result = {}
  local state = "authors"
  local journal_words = {}
  local bhat_state = nil   -- nil | "bhat" | "H"
  local bhat_tokens = {}   -- accumulate raw tokens for possible rollback
  local suffix = ""        -- trailing comma after "S." if any

  local function flush_journal()
    if #journal_words > 0 then
      local text = table.concat(journal_words, " ")
      table.insert(result,
        raw('<strong><span style="color:' .. harvard .. '">' .. text .. '</span></strong>'))
      journal_words = {}
    end
  end

  local function flush_bhat_plain()
    for _, t in ipairs(bhat_tokens) do
      table.insert(result, t)
    end
    bhat_state = nil
    bhat_tokens = {}
    suffix = ""
  end

  local function emit_bhat()
    -- Emit bold+underline span, then trailing comma if present
    table.insert(result, raw('<strong style="text-decoration:underline;">Bhat, H. S.</strong>'))
    if suffix ~= "" then
      table.insert(result, raw(suffix))
    end
    bhat_state = nil
    bhat_tokens = {}
    suffix = ""
  end

  -- Process each token through the main state machine
  local function process_main(el)
    if state == "authors" then
      if el.t == "Emph" then
        table.insert(result, raw("<strong><em>"))
        for _, child in ipairs(el.content) do
          if child.t == "Str" then
            table.insert(result, raw(child.text))
          elseif child.t == "Space" then
            table.insert(result, raw(" "))
          else
            table.insert(result, child)
          end
        end
        table.insert(result, raw("</em></strong>"))
        state = "post_emph"
      else
        table.insert(result, el)
      end

    elseif state == "post_emph" then
      table.insert(result, el)
      if el.t == "Space" then state = "maybe_journal" end

    elseif state == "maybe_journal" then
      if el.t == "Str" then
        local t = el.text
        if t == "in" then
          table.insert(result, el)
          state = "done"
        elseif t:sub(-1) == "." and t ~= "Int." and not t:match("^[A-Z]") then
          table.insert(result, el)
          state = "done"
        else
          table.insert(journal_words, t)
          if t:sub(-1) == "," then
            flush_journal()
            state = "done"
          else
            state = "journal"
          end
        end
      else
        table.insert(result, el)
        state = "done"
      end

    elseif state == "journal" then
      if el.t == "Str" then
        local t = el.text
        if t:find(":") then
          flush_journal()
          if result[#result] and result[#result].t == "Space" then
            table.remove(result)
          end
          state = "done"
        elseif t:sub(-1) == "," then
          table.insert(journal_words, t)
          flush_journal()
          state = "done"
        else
          table.insert(journal_words, t)
        end
      elseif el.t == "Space" then
        -- absorbed
      elseif el.t == "Link" then
        if #journal_words > 0 then
          local last = journal_words[#journal_words]
          if last:sub(-1) == "." then
            journal_words[#journal_words] = last:sub(1, -2)
          end
        end
        flush_journal()
        if result[#result] and result[#result].t ~= "Space" then
          table.insert(result, pandoc.Space())
        end
        table.insert(result, el)
        state = "done"
      else
        flush_journal()
        table.insert(result, el)
        state = "done"
      end

    else -- done
      if el.t == "Str" and el.text:find(":") then
        if result[#result] and result[#result].t == "Space" then
          table.remove(result)
        end
      elseif el.t == "Link" then
        if result[#result] and result[#result].t ~= "Space" then
          table.insert(result, pandoc.Space())
        end
        table.insert(result, el)
      else
        table.insert(result, el)
      end
    end
  end

  for _, el in ipairs(inlines) do

    -- ── Bhat, H. S. detection ─────────────────────────────────
    if bhat_state == nil then
      if el.t == "Str" and el.text == "Bhat," then
        bhat_state = "bhat"
        bhat_tokens = {el}
      else
        process_main(el)
      end

    elseif bhat_state == "bhat" then
      if el.t == "Space" then
        table.insert(bhat_tokens, el)
      elseif el.t == "Str" and el.text == "H." then
        bhat_state = "H"
        table.insert(bhat_tokens, el)
      else
        -- not a match
        flush_bhat_plain()
        process_main(el)
      end

    elseif bhat_state == "H" then
      if el.t == "Space" then
        table.insert(bhat_tokens, el)
      elseif el.t == "Str" and (el.text == "S." or el.text == "S.,") then
        -- Full match — "S." (last author) or "S.," (mid-list)
        suffix = el.text == "S.," and "," or ""
        emit_bhat()
      else
        flush_bhat_plain()
        process_main(el)
      end
    end

  end

  -- Flush any dangling bhat tokens
  if bhat_state then flush_bhat_plain() end

  flush_journal()
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
      nb.content = process_inlines(block.content)
      table.insert(new_blocks, nb)
    else
      table.insert(new_blocks, block)
    end
  end
  el.content = new_blocks
  return el
end