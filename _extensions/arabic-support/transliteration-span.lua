-- Reformat all heading text 
-- 0331 macron below
-- 0323 dot below
function RomanizeMapping(text2, is_italic)
  dhal_lc = "ð"
  dhal_uc = "Ð"
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
  mylcase["p"] = dhal_lc -- "d" .. utf8.char(0x0331)  -- "ḏ" -- dhal
  mylcase["c"] = "š" -- sheen
  mylcase["S"] = "ṣ"
  mylcase["D"] = "ḍ"
  mylcase["T"] = "ṭ"
  mylcase["P"] = dhal_lc .. utf8.char(0x0323)  --"ḏ̣" -- DHaa
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
  myucase["p"] = dhal_uc --  "Ḏ"
  myucase["c"] = "Š"
  myucase["S"] = "Ṣ"
  myucase["D"] = "Ḍ"
  myucase["T"] = "Ṭ"
  myucase["P"] = dhal_uc .. utf8.char(0x0323) --Ḏ̣"
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
    mylcase["v"] = "t" .. utf8.char(0x0361) .. "h"
    myucase["v"] = "T" .. utf8.char(0x0361) .. "h"
    mylcase["c"] = "s" .. utf8.char(0x0361) .. "h"
    myucase["c"] = "S" .. utf8.char(0x0361) .. "h"
    mylcase["x"] = "k" .. utf8.char(0x0361) .. "h"
    myucase["x"] = "K" .. utf8.char(0x0361) .. "h"
    mylcase["g"] = "g" .. utf8.char(0x0361) .. "h"
    myucase["g"] = "G" .. utf8.char(0x0361) .. "h"
    mylcase["p"] = "d" .. utf8.char(0x0361) .. "h"
    myucase["p"] = "D" .. utf8.char(0x0361) .. "h"
    mylcase["P"] = "d" .. utf8.char(0x0323) .. utf8.char(0x0361) .. "h"
    myucase["P"] = "D" .. utf8.char(0x0323) .. utf8.char(0x0361) .. "h"

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

  -- if not is_italic then
  --   mylcase["e"] = "ʿ" -- 3ayn
  --   myucase["e"] = "ʿ"
  -- end

  local text3 = ''
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
        if digraph_en and (charv == 'h' or charv == 'H') and prev_charv ~= '=' and (prev_charv == 't' or prev_charv == 's' or prev_charv == 'k' or prev_charv == 'd' or prev_charv == 'p' or prev_charv == 'P' or prev_charv == 'D' or prev_charv == 'c' or prev_charv == 'v' or prev_charv == 'x' or prev_charv == 'g') then
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
--function Span (el)
--  if el.classes:includes 'trn' then
--    input_text = pandoc.utils.stringify(el)
--    output_text = RomanizeMapping(input_text, true)
--    contents = {pandoc.Str(output_text)}
--    return pandoc.Span(contents, {class='trnital'})
--  end
--end
function Span (el)
  if el.classes:includes 'trn' 
  or el.classes:includes 'trn2' then
    input_text = pandoc.utils.stringify(el)
    output_text = RomanizeMapping(input_text, true)
    contents = {pandoc.Str(output_text)}
    if el.classes:includes 'trn' then
      contents = pandoc.Span(pandoc.Emph(contents), {class='trn'})
    end
    return pandoc.Span(contents, {class='trn2'})
  end
end

