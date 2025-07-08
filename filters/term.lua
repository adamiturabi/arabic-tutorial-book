package.path = package.path .. ';../_extensions/arabic-support/?.lua'
local romanize = require("romanize")
local ar_span = require("ar_span")

local map_table = {}

-- phrases
map_table["ia"] = {"if Allāh wills", nil}

-- diacritics
map_table["amark"] = {"fatHah", "trn2"}
map_table["imark"] = {"kasrah", "trn2"}
map_table["umark"] = {"Dammah", "trn2"}
map_table["0mark"] = {"sukUn", "trn2"}
map_table["shaddah"] = {"caddah", "trn2"}
map_table["tanwin"] = {"tanwIn", "trn2"}

-- person
map_table["first"] = {"speaker", nil}
map_table["second"] = {"adressee", nil}
map_table["third"] = {"absentee", nil}

-- mabny and mutasarrif
map_table["mabny"] = {"rigid", nil}
map_table["diptote"] = {"semi-flexible", nil}
map_table["triptote"] = {"fully-flexible", nil}
map_table["tote"] = {"flexible", nil}

-- alphabetical
map_table["badal"] = {"replacement", nil}

map_table["fail"] = {"doer", nil}

map_table["idafa"] = {"annexation", nil}
map_table["indir_mafulb"] = {"indirect doee", nil}
map_table["ishara"] = {"pointing noun", nil}
map_table["ismfail"] = {"doer participle", nil}
map_table["ismkn"] = {"subject", nil}
map_table["ismmaful"] = {"doee participle", nil}
map_table["ismmarrah"] = {"one-time noun", nil}

map_table["lazim"] = {"intransitive", nil}
map_table["lnj"] = {"لا النافية للجنس", "ar"}

map_table["madi"] = {"past", nil}
map_table["maful"] = {"doee", nil}
map_table["mafulb"] = {"direct doee", nil}
map_table["manut"] = {"describee", nil}
map_table["masdar"] = {"maSdar", "trn2"}
map_table["mawsul"] = {"connected noun", nil}
map_table["mmutlaq"] = {"absolute doee", nil}
map_table["mubdalb"] = {"replacee", nil}
map_table["mubtada"] = {"topic", nil}
map_table["mudaf"] = {"annexe noun", nil}
map_table["mudafil"] = {"base noun", nil}
map_table["mudarie"] = {"muDArie", "trn2"}
map_table["mutaddi"] = {"transitive", nil}

map_table["naib"] = {"deputy", nil}
map_table["naat"] = {"describer", nil}

map_table["passive"] = {"passive", nil}

map_table["sifah"] = {"adjectival noun", nil}
map_table["silah"] = {"connecting sentence", nil}

map_table["xabar"] = {"comment", nil}


function get_map_table_value(input_text)
  return map_table[input_text]
end

function get_output_text(input_text)
  -- Check if to capitalize first letter
  local capitalize = false
  --if string.match(input_text:sub(1,1), "%u") then
  --  capitalize = true
  --end
  --input_text = string.lower(input_text)
  if string.match(input_text:sub(1,1), "_") then
    capitalize = true
    input_text = input_text:sub(2)
  end
  --local mapped = map_table[input_text]
  local mapped = get_map_table_value(input_text)
  if not mapped then
    print("bad term input text: " .. input_text)
    error()
  end
  if mapped[2] == nil then
    if capitalize then
      return string.upper(mapped[1]:sub(1,1)) .. mapped[1]:sub(2)
    end
    return mapped[1]
  end
  if mapped[2] == "trn2" then
    if capitalize then
      --mapped[1] = "_" .. mapped[1]
      return romanize.RomanizeMapping("_" .. mapped[1], false)
    end
    return romanize.RomanizeMapping(mapped[1], false)
  elseif mapped[2] == "ar" then
    return ar_span.ArabicSpan(pandoc.Span(mapped[1], {class="ar"}))
  end
  --return pandoc.Span(mapped[1], {class=mapped[2]})
end
function Span(el)
  if el.classes:includes 'term' then
    local input_text = pandoc.utils.stringify(el)
    return get_output_text(input_text)
  end
end

