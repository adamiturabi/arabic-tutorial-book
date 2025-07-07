package.path = package.path .. ';../_extensions/arabic-support/?.lua'
local romanize = require("romanize")
local ar_span = require("ar_span")

function get_output_text(input_text)
  -- Check if first letter upper case
  local map_table = {}
  map_table["mtl"] = {"absolute doee", nil}
  map_table["msd"] = {"maSdar", "trn2"}
  map_table["lnj"] = {"لا النافية للجنس", "ar"}
  local capitalize = false
  if string.match(input_text:sub(1,1), "%u") then
    capitalize = true
  end
  input_text = string.lower(input_text)
  local mapped = map_table[input_text]
  if mapped[2] == nil then
    if capitalize then
      return string.upper(mapped[1]:sub(1,1)) .. mapped[1]:sub(2)
    end
    return mapped[1]
  end
  if mapped[2] == "trn2" then
    if capitalize then
      mapped[1] = "#" .. mapped[1]
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

