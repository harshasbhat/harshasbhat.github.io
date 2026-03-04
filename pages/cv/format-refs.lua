--[[
  format-refs.lua
  Inside every .csl-entry div (produced by --citeproc):
    - Bolds "Bhat" surname token wherever it appears
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
        -- Bold+italic title
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
          table.insert(result, el)
          state = "done"
        elseif t:sub(-1) == "." and t ~= "Int." and not t:match("^[A-Z]") then
          -- Publisher (e.g. "Wiley.") — don't color
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
          -- volume:page token — flush journal, DROP this token
          flush_journal()
          -- remove trailing space before vol:page
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
        -- absorbed into journal_words join

      elseif el.t == "Link" then
        -- DOI with no volume:page (under-review)
        if #journal_words > 0 then
          local last = journal_words[#journal_words]
          if last:sub(-1) == "." then
            journal_words[#journal_words] = last:sub(1, -2)
          end
        end
        flush_journal()
        -- ensure space before link
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
        -- Drop any remaining vol:page tokens
        if result[#result] and result[#result].t == "Space" then
          table.remove(result)
        end
      elseif el.t == "Link" then
        -- Ensure space before DOI link
        if result[#result] and result[#result].t ~= "Space" then
          table.insert(result, pandoc.Space())
        end
        table.insert(result, el)
      else
        table.insert(result, el)
      end
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
