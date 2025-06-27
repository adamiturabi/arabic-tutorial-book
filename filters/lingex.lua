ex_counter = 1

Div = function (el)
  if el.classes:includes 'lingex' then
    ex_counter_str = tostring(ex_counter)
    ex_counter = ex_counter + 1

    local has_ref = false
    for i, item in ipairs(el.content) do
      if item.identifier ~= nil and item.identifier == "lingexref" then
        has_ref = true
        if FORMAT:match 'latex' then
          table.insert(
            item.content, 1,
            pandoc.RawInline('latex', '\\raggedright {\\footnotesize ')
          )
          table.insert(
            item.content,
            pandoc.RawInline('latex', '}')
          )
        end
      end
    end
        
    if FORMAT:match 'latex' then
      local num_div = pandoc.Div(pandoc.RawInline('latex', '\\stepcounter{mycounter}(\\themycounter)') , {"num"})
      --num_div.attributes['layout-valign'] = 'top' -- does not work: https://github.com/quarto-dev/quarto-cli/issues/9109
      table.insert(
        el.content, 1,
        num_div
      )
    else
      table.insert(
        el.content, 1,
        pandoc.Div("(" .. ex_counter_str .. ")", {"num"})
      )
    end
    if not has_ref then
      table.insert(
        el.content, 
        pandoc.Div("", {"lingexref"})
      )
    end

    local return_div = pandoc.Div(el.content, {layout='[0.1, 0.6, -0.1, 0.2]'})
    return_div.attributes['fig-pos'] = 'H'
    return return_div
  end
end

