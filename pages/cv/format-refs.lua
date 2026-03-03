--[[
  format-refs.lua
  Inside every .csl-entry div (produced by --citeproc):
    - Bolds "Bhat" surname token wherever it appears
    - Makes the article/book title (the Emph block) bold+italic
    - Colors the journal name in Harvard crimson (#C90016)

  Journal name detection:
    The journal name is the text run between (title Emph + ". ") and
    the first token that contains ":" (volume:page) or a Link (DOI).
    It ends at the last comma-terminated token before volume:page.
    If no volume:page exists (under-review entries), collect until Link or end.
    Books ("in ...") and book publishers are not colored.
]]

local harvard = "#C90016"

local function raw(html)
  return pandoc.RawInline("html", html)
end

local function process_inlines(inlines)
  local result = {}
  local state = "authors"
  local journal_words = {}

  local function flush_journal()
    if #journal_words > 0 then
      local text = table.concat(journal_words, " ")
      table.insert(result,
        raw('<span style="color:' .. harvard .. '">' .. text .. '</span>'))
      journal_words = {}
    end
  end

  for _, el in ipairs(inlines) do

    -- Bold Bhat anywhere
    if el.t == "Str" and el.text:match("^Bhat[,.]?$") then
      table.insert(result, raw("<strong>" .. el.text .. "</strong>"))

    elseif state == "authors" then
      if el.t == "Emph" then
        -- Bold+italic the title
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
      -- Absorb ". " after title before journal name starts
      table.insert(result, el)
      if el.t == "Space" then state = "maybe_journal" end

    elseif state == "maybe_journal" then
      if el.t == "Str" then
        local t = el.text
        if t == "in" then
          -- Book chapter — no journal coloring
          table.insert(result, el)
          state = "done"
        else
          -- Start accumulating journal name
          table.insert(journal_words, t)
          if t:sub(-1) == "," then
            -- Single-word journal ending in comma (e.g. "Nature,")
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
          -- volume:page — flush journal accumulated so far (strip trailing comma if any)
          flush_journal()
          table.insert(result, el)
          state = "done"
        elseif t:sub(-1) == "," then
          -- Last word of journal name ends with comma
          table.insert(journal_words, t)
          flush_journal()
          state = "done"
        else
          -- Could be mid-journal word (e.g. "J.", "Geophys.", "Res.")
          -- or a publisher. Keep accumulating.
          table.insert(journal_words, t)
        end
      elseif el.t == "Space" then
        -- absorbed into journal_words join

      elseif el.t == "Link" then
        -- DOI link reached with no volume:page — under-review entry.
        -- Flush whatever we have as journal (strip trailing period if present).
        if #journal_words > 0 then
          local last = journal_words[#journal_words]
          if last:sub(-1) == "." then
            journal_words[#journal_words] = last:sub(1, -2)
          end
        end
        flush_journal()
        table.insert(result, el)
        state = "done"
      else
        flush_journal()
        table.insert(result, el)
        state = "done"
      end

    else -- done
      table.insert(result, el)
    end

  end

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
