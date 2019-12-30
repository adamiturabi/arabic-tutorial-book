function Span (elem)
  if elem.classes[1] == 'trn' then
    for index,text in pairs(elem.content) do
      for index2,text2 in pairs(text) do
        text2 = string.gsub(text2, "v", "th")
        text2 = string.gsub(text2, "x", "kh")
        text2 = string.gsub(text2, "p", "dh")
        text2 = string.gsub(text2, "c", "sh")
        text2 = string.gsub(text2, "P", "Dh")
        text2 = string.gsub(text2, "e", "ɛ")
        text2 = string.gsub(text2, "g", "gh")
        text2 = string.gsub(text2, "'", "ʾ")
        text2 = string.gsub(text2, "A", "aa")
        text2 = string.gsub(text2, "I", "ee")
        text2 = string.gsub(text2, "U", "oo")
	text[index2] = text2
      end
      elem.content[index] = text
    end
    return pandoc.Emph (elem.content)
  elseif elem.classes[1] == 'ar' then
    attrs = pandoc.Attr("", {}, {{"lang", "ar"},{"dir","rtl"}})
    return pandoc.Span(elem.content, attrs)
  else
    return elem
  end
end
