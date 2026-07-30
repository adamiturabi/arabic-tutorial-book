Span = function (el)
  if el.classes:includes 'trans' then
    -- return pandoc.Emph(el.content)
    --return {"« "} .. el.content .. {" »"} -- no-break-spaces with guillemets
    return {"« "} .. el.content .. {" »"} -- narrow no-break-spaces with guillemets
  end
end

