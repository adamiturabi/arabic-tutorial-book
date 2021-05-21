function RomanizeMapping(text2)
  -- use digraphs sh, th, etc for some characters
  digraph_en = true

  -- lower case mapping
  mylcase = {}
  mylcase["E"] = "ʾ" -- hamza
  mylcase["A"] = "ā"
  mylcase["v"] = "ṯ" -- thaa
  mylcase["j"] = "j" -- "ǧ" -- jeem
  mylcase["H"] = "ḥ"
  mylcase["x"] = "ḵ" -- Khaa
  mylcase["p"] = "ḏ" -- dhal
  mylcase["c"] = "š" -- sheen
  mylcase["S"] = "ṣ"
  mylcase["D"] = "ḍ"
  mylcase["T"] = "ṭ"
  mylcase["P"] = "ḏ̣" -- DHaa
  mylcase["e"] = "ɛ" -- 3ayn
  mylcase["g"] = "ġ" -- ghayn
  mylcase["o"] = "ḧ" -- for taa marbuta in pausa non-construct
  mylcase["O"] = "ẗ" -- for taa marbuta in pausa construct
  mylcase["I"] = "ī"
  mylcase["U"] = "ū"
  mylcase["="] = "·" -- to insert middot explicitly. middot is automatically inserted before 'h' if digraph_en=true

  -- upper case mapping. use hash '#' before desired uppercase character
  myucase = {}
  myucase["E"] = "ʾ"
  myucase["A"] = "Ā"
  myucase["v"] = "Ṯ"
  myucase["j"] = "J" -- "Ǧ"
  myucase["H"] = "Ḥ"
  myucase["x"] = "Ḵ"
  myucase["p"] = "Ḏ"
  myucase["c"] = "Š"
  myucase["S"] = "Ṣ"
  myucase["D"] = "Ḍ"
  myucase["T"] = "Ṭ"
  myucase["P"] = "Ḏ̣"
  myucase["e"] = "Ɛ"
  myucase["g"] = "Ġ"
  myucase["I"] = "Ī"
  myucase["U"] = "Ū"
  myucase["a"] = "A"
  myucase["i"] = "I"
  myucase["u"] = "U"
  myucase["b"] = "B"
  myucase["t"] = "T"
  myucase["d"] = "D"
  myucase["r"] = "R"
  myucase["z"] = "Z"
  myucase["s"] = "S"
  myucase["f"] = "F"
  myucase["q"] = "Q"
  myucase["k"] = "K"
  myucase["l"] = "L"
  myucase["m"] = "M"
  myucase["n"] = "N"
  myucase["h"] = "H"
  myucase["w"] = "W"
  myucase["y"] = "Y"

  if digraph_en then
    mylcase["v"] = "t͟h"
    myucase["v"] = "T͟h"
    mylcase["c"] = "s͟h"
    myucase["c"] = "S͟h"
    mylcase["x"] = "k͟h"
    myucase["x"] = "K͟h"
    mylcase["g"] = "g͟h"
    myucase["g"] = "G͟h"
    mylcase["p"] = "d͟h"
    myucase["p"] = "D͟h"
    mylcase["P"] = "d".. utf8.char(0x035f) .. utf8.char(0x034f) .. utf8.char(0x0323) .. "h"
    myucase["P"] = "D".. utf8.char(0x035f) .. utf8.char(0x034f) .. utf8.char(0x0323) .. "h"
    --mylcase["P"] = "d͟͏̣h"
    --myucase["P"] = "D͟͏̣h"

    --mylcase["v"] = "ṯ͡h"
    --myucase["v"] = "Ṯ͡h"
    --mylcase["c"] = "š͡h" -- sheen
    --myucase["c"] = "Š͡h"
    --mylcase["x"] = "ḵ͡h"
    --myucase["x"] = "Ḵ͡h"
    --mylcase["g"] = "ġ͡h" -- ghayn
    --myucase["g"] = "Ġ͡h"
    --mylcase["p"] = "ḏ͡h" -- dhal
    --myucase["p"] = "Ḏ͡h"
    --mylcase["P"] = "ḏ̣͡h"
    --myucase["P"] = "Ḏ̣͡h"
  end

  text3 = ''
  local caps = false
  local prev_charv = ''
  for index3 = 1, #text2 do
    local charv = text2:sub(index3, index3)
    if charv == "#" then
      caps = true
    else
      if caps then
        if myucase[charv] == nil then
          text3 = text3 .. charv
        else
          text3 = text3 .. myucase[charv]
        end
        caps = false
      else
        if digraph_en and charv == 'h' and prev_charv ~= '=' and (prev_charv == 't' or prev_charv == 's' or prev_charv == 'k' or prev_charv == 'd' or prev_charv == 'p' or prev_charv == 'P' or prev_charv == 'D' or prev_charv == 'c' or prev_charv == 'v' or prev_charv == 'x' or prev_charv == 'g') then
          text3 = text3 .. "·"
        end
        if mylcase[charv] == nil then
          text3 = text3 .. charv
        else
          text3 = text3 .. mylcase[charv]
        end
      end
    end
    prev_charv = charv
  end
  return text3
end
function Romanize (elem)
  for index,text in pairs(elem.content) do
    for index2,text2 in pairs(text) do
      text3 = RomanizeMapping(text2)
      text[index2] = text3
    end
    elem.content[index] = text
  end
  return (elem.content)
end
function Span (elem)
  if elem.classes[1] == 'trn' then
    return pandoc.Emph (Romanize(elem))
  elseif elem.classes[1] == 'trn2' then
    return (Romanize(elem))
  elseif elem.classes[1] == 'ar' then
    attrs = pandoc.Attr("", {}, {{"lang", "ar"},{"dir","rtl"}})
    return pandoc.Span(elem.content, attrs)
  elseif elem.classes[1] == 'smallcaps' then
    attrs = pandoc.Attr("", {}, {{"style", "font-variant:small-caps;"}})
    return pandoc.Span(elem.content, attrs)
  else
    return elem
  end
end

