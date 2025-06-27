Span = function (el)
  if el.classes:includes 'ftsize' then
    if FORMAT:match 'latex' then
      --text = pandoc.utils.stringify(el)
      contents = el.content
      table.insert(
        contents, 1,
        pandoc.RawInline('latex', '{\\raggedright {\\footnotesize ')
      )
      table.insert(
        contents,
        pandoc.RawInline('latex', '}}')
      )
    end
    --return pandoc.Span(contents, {})
    return contents
  end
end

