function Span (elem)
  if elem.classes[1] == 'trn' then
    for index,text in pairs(elem.content) do
      for index2,text2 in pairs(text) do
        --text2 = string.gsub(text2, "v", "th")
        --text2 = string.gsub(text2, "x", "kh")
        --text2 = string.gsub(text2, "p", "dh")
        --text2 = string.gsub(text2, "c", "sh")
        --text2 = string.gsub(text2, "P", "Dh")
        --text2 = string.gsub(text2, "e", "ɛ")
        --text2 = string.gsub(text2, "g", "gh")
        --text2 = string.gsub(text2, "E", "ʾ")
        --text2 = string.gsub(text2, "'", "X")
        --text2 = string.gsub(text2, "A", "aa")
        --text2 = string.gsub(text2, "I", "ee")
        --text2 = string.gsub(text2, "U", "oo")
        text2 = string.gsub(text2, "E", "ʾ")
        text2 = string.gsub(text2, "A", "ā")
        text2 = string.gsub(text2, "v", "ṯ")
        text2 = string.gsub(text2, "j", "ǧ")
        text2 = string.gsub(text2, "H", "ḥ")
        text2 = string.gsub(text2, "p", "ḏ")
        text2 = string.gsub(text2, "c", "š")
        text2 = string.gsub(text2, "S", "ṣ")
        text2 = string.gsub(text2, "D", "ḍ")
        text2 = string.gsub(text2, "T", "ṭ")
        text2 = string.gsub(text2, "P", "ḏ̣")
        text2 = string.gsub(text2, "e", "ɛ")
        text2 = string.gsub(text2, "g", "ġ")
        text2 = string.gsub(text2, "o", "ḧ")
        text2 = string.gsub(text2, "O", "ẗ")
        text2 = string.gsub(text2, "I", "ī")
        text2 = string.gsub(text2, "U", "ū")

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
