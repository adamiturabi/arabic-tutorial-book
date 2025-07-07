Span = function (el)
  if el.classes:includes 'citex' then
    if FORMAT:match 'latex' then
      table.insert(
        el.content, 1,
        --pandoc.RawInline('latex', '[')
        pandoc.RawInline('latex', '{\\raggedright {\\footnotesize [')
      )
      table.insert(
        el.content,
        pandoc.RawInline('latex', ']}}')
      )
      --return pandoc.Span({"["} .. el.content .. {"]"}, {class="ftsize"})
      return el
    elseif FORMAT:match 'html' then
      return pandoc.Span({"["} .. el.content .. {"]"}, {class="ftsize"})
    end
  end
end

