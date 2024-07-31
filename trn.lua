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
function Romanize (elem, is_italic)
  --local retstr = ""
  for index,val in pairs(elem.content) do
    local text = val.text
    if type(text) == "string" then
      local new_text = RomanizeMapping(text, is_italic)
      --retstr = retstr .. new_text
      val.text = new_text
      elem.content[index] = val
    --else
    --  retstr = retstr .. " "
    end
  end
  return elem
end
function TxtSub (elem)
  --local retstr = ""
  for index,val in pairs(elem.content) do
    local text = val.text
    if type(text) == "string" then
      local new_text = ''
      for index3 = 1, #text do
        local charv = text:sub(index3, index3)
        if charv == '0' then
          new_text = new_text .. 'ø'
        else
          new_text = new_text .. charv
        end
      end
      --retstr = retstr .. new_text
      val.text = new_text
      elem.content[index] = val
    --else
    --  retstr = retstr .. " "
    end
  end
  return elem
end
function ArTxtReplace(text2)
  local text3 = ''
  text3 = text2:gsub("ك", "ک")
  return text3
end

function ArTxtProc(elem)
  for index,val in pairs(elem.content) do
    local text = val.text
    if type(text) == "string" then
      local new_text = ArTxtReplace(text)
      val.text = new_text
      elem.content[index] = val
    end
  end
  return elem
end
function RootFmt (elem)
  for index,val in pairs(elem.content) do
    local text = val.text
    if type(text) == "string" then
      local new_text = "«" .. text .. "»"
      val.text = new_text
      elem.content[index] = val
    end
  end
  return elem
end
function Span (elem)
  if elem.classes[1] == 'trn' then
    return pandoc.Emph(Romanize(elem, true).content)
  elseif elem.classes[1] == 'trn2' then
    return Romanize(elem, false).content
  elseif elem.classes[1] == 'ar' then
    local new_elem = ArTxtProc(elem)
    if FORMAT:match 'latex' then
      -- no dir needed for babel and throws error if it sees dir attribute. was previously needed for polyglossia
      return pandoc.Span(new_elem.content, {lang='ar'})
    elseif FORMAT:match 'html' then
      -- dir needed for html otherwise punctuation gets messed up
      return pandoc.Span(new_elem.content, {lang='ar', dir='rtl'})
    else
      return elem
    end
  elseif elem.classes[1] == 'tradar' then
    local new_elem = ArTxtProc(elem)
    if FORMAT:match 'latex' then
      -- no dir needed for babel and throws error if it sees dir attribute. was previously needed for polyglossia
      --return pandoc.Span("\\tradarab{"..new_elem.content.."}", {})
      table.insert(
        new_elem.content, 1,
        pandoc.RawInline('latex', '\\tradarab{')
      )
       table.insert(
        new_elem.content,
        pandoc.RawInline('latex', '}')
      )
      return pandoc.Span(new_elem.content, {})
    elseif FORMAT:match 'html' then
      -- dir needed for html otherwise punctuation gets messed up
      return pandoc.Span(new_elem.content, {lang='ar', dir='rtl', style="font-family: Amiri;"})
    else
      return elem
    end
  elseif elem.classes[1] == 'arroot' then
    elem = ArTxtProc(elem)
    if FORMAT:match 'latex' then
      -- no dir needed for babel and throws error if it sees dir attribute. was previously needed for polyglossia
      return pandoc.Span(RootFmt(elem).content, {lang='ar'})
    elseif FORMAT:match 'html' then
      -- dir needed for html otherwise punctuation gets messed up
      return pandoc.Span(RootFmt(elem).content, {lang='ar', dir='rtl'})
    else
      return elem
    end
  elseif elem.classes[1] == 'trnroot' then
    return pandoc.Emph (RootFmt(Romanize(elem, true)).content)
  elseif elem.classes[1] == 'txt' then
    -- text substitutions
    return TxtSub(elem).content
  else
    return elem
  end
end

