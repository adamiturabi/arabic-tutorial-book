Span = function (el)
  if el.classes:includes 'citex' then
    --if FORMAT:match 'latex' then
    --  table.insert(
    --    el.content, 1,
    --    pandoc.RawInline('latex', '[')
    --  )
    --  table.insert(
    --    el.content,
    --    pandoc.RawInline('latex', ']')
    --  )
    --  return pandoc.Span({"["} .. el.content .. {"]"}, {class="ftsize"})
    --elseif FORMAT:match 'html' then
      return pandoc.Span({"["} .. el.content .. {"]"}, {class="ftsize"})
    --end
  end
end

