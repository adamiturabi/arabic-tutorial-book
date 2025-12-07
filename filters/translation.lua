Span = function (el)
  if el.classes:includes 'trans' then
    return pandoc.Emph(el.content)
  end
end

