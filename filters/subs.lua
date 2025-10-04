package.path = package.path .. ';../_extensions/arabic-support/?.lua'
local romanize = require("romanize")
local ar_span = require("ar_span")

local map_table = {}

-- text terms
map_table["ia"] = {"if Allāh wills", nil}
map_table["quran"] = {"Qurʾān", nil}
map_table["ayah"] = {"Ayah", "trn2"}
map_table["surah"] = {"sUrah", "trn2"}
map_table["tafsir"] = {"tafsIr", "trn2"}

-- states
map_table["ustate"] = {"raised-state", nil}
map_table["astate"] = {"propped-state", nil}
map_table["istate"] = {"lowered-state", nil}
map_table["0state"] = {"clipped-state", nil}

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

-- active and passive voice
map_table["active"] = {"active", nil} -- "known-doer" verb?
map_table["passive"] = {"passive", nil} -- "unknown-doer" verb?

-- government
map_table["3aamil"] = {"governor", nil}
map_table["ma3mul"] = {"governee", nil}
map_table["3amal"] = {"government", nil}
map_table["3umdah"] = {"indispensable", nil} -- indispensable, foundational, basic
map_table["fadlah"] = {"dispensable", nil} -- dispensable, redundant, extra

-- jumlah khabariyyah and inshaa'iyyah
map_table["xabari"] = {"truth-evaluable", nil} -- falsifiable
map_table["inshai"] = {"non-truth-evaluable", nil} -- non-falsifiable

-- idaafah types
map_table["ma3nawi"] = {"real", nil} 
map_table["lafzi"] = {"fake", nil} 

-- alphabetical
map_table["3aaid"] = {"refer-back pronoun", nil}
map_table["3atf"] = {"conjunction", nil}
map_table["3atf_bayan"] = {"clarifying follower", nil}

map_table["adat_istifham"] = {"question word", nil}
map_table["af3al"] = {"comparative noun", nil}
map_table["af3aal_quloob"] = {"verbs of the heart", nil}

map_table["badal"] = {"replacement", nil}

map_table["dharf_makan"] = {"adverb of place", nil}
map_table["dharf_zaman"] = {"adverb of time", nil}

map_table["faa3il"] = {"doer", nil}

map_table["hal"] = {"HAl", "trn2"}

map_table["idaafah"] = {"annexation", nil}
map_table["indir_mafulb"] = {"indirect doee", nil}
map_table["ism_fail"] = {"doer participle", nil}
map_table["ism_isharah"] = {"pointing noun", nil}
map_table["ism_of"] = {"subject", nil}
map_table["ism_maful"] = {"doee participle", nil}
map_table["ism_marrah"] = {"one-time noun", nil}
map_table["ism_hay2ah"] = {"noun of kind", nil}
map_table["ism_makan"] = {"noun of place", nil}
map_table["ism_masdar"] = {"quasi-maṣdar", nil}
map_table["ism_mawsul"] = {"connected noun", nil}
map_table["ism_zaman"] = {"noun of time", nil}
map_table["isnaad"] = {"sentence-completion", nil}

map_table["jamid"] = {"underived", nil}
map_table["jawab"] = {"consequence", nil}
map_table["j_ism"] = {"nominal sentence", nil}
map_table["j_f3l"] = {"verbal sentence", nil}

map_table["lazim"] = {"intransitive", nil}
map_table["lnj"] = {"لا النافية للجنس", "ar"}

map_table["ma3toof"] = {"conjunctee", nil}  -- "stateless" verb?
map_table["madi"] = {"past", nil}  -- "stateless" verb?
map_table["maful"] = {"doee", nil}
map_table["mafulb"] = {"direct doee", nil}
map_table["mafull"] = {"adverb of reason", nil}
map_table["mafulm"] = {"accompanying doee", nil}
map_table["manut"] = {"describee", nil}
map_table["masdar"] = {"maSdar", "trn2"}
map_table["mmutlaq"] = {"absolute doee", nil}
map_table["mubdalb"] = {"replacee", nil}
map_table["mubtada"] = {"subject", nil}
map_table["mudaf"] = {"annexe noun", nil}
map_table["mudafil"] = {"base noun", nil}
map_table["mudarie"] = {"resembling", nil} -- {"muDArie", "trn2"} -- "stateful" verb?
map_table["mushar_il"] = {"pointed-to noun", nil} -- {"muDArie", "trn2"}
map_table["mushtaqq"] = {"deverbal", nil} -- deverbal, derived
map_table["musnad"] = {"leaned element", nil} -- complement
map_table["musnadi"] = {"leaned-to element", nil} -- rock, mainstay, anchor
map_table["mustatir"] = {"latent", nil} -- assumed, hidden, invisible, implied
map_table["muxbar3"] = {"leaned-to element", nil} -- theme,rock, mainstay, anchor, subject, keystone, cornerstone, post, mast, pillar
map_table["muxbar"] = {"leaned element", nil} -- rheme, complement, predicate, cornerstone, keystone, capstone, rafter, beam
map_table["mutaddi"] = {"transitive", nil}

map_table["naib"] = {"deputy", nil}
map_table["na3t"] = {"describer", nil}
map_table["nidaa"] = {"vocative", nil}
map_table["nasix"] = {"canceling", nil}

map_table["pbuh"] = {"ﷺ", "aralt" }

map_table["rabt"] = {"link", nil}

map_table["sababi"] = {"sababi", nil} -- takeover
map_table["sahib_hal"] = {"person of ḥāl", nil}
map_table["sahibs_hal"] = {"persons of ḥāl", nil}
map_table["sifah"] = {"adjectival noun", nil}
map_table["sifah_mush"] = {"participle-like noun", nil} -- {"participlish adjectival noun", nil} -- "participle-like"?
map_table["sighah_mub"] = {"emphatic noun", nil} -- {"participlish adjectival noun", nil} -- "participle-like"?
map_table["silah"] = {"connecting sentence", nil}
map_table["shart"] = {"condition", nil}
map_table["shibh_fi3l"] = {"quasi-verb", nil}
map_table["shibh_jumlah"] = {"quasi-sentence", nil}
map_table["shibh_jumlah"] = {"quasi-sentence", nil}

map_table["tabi3"] = {"follower", nil}
map_table["tamyiz"] = {"tamyIz", "trn2"}
map_table["tawkeed"] = {"emphatic follower", nil}

map_table["x"] = {"✗", nil}
map_table["xabar"] = {"remark", nil} -- newsworthy expression, information, comment, remark, info, report, news, expression

map_table["zaaid"] = {"redundant", nil}


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
  if string.match(input_text:sub(1,1), "#") then
    capitalize = true
    input_text = input_text:sub(2)
  end
  --local mapped = map_table[input_text]
  local mapped = get_map_table_value(input_text)
  if not mapped then
    print("bad subs input text: " .. input_text)
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
      return romanize.RomanizeMapping("#" .. mapped[1], false)
    end
    return romanize.RomanizeMapping(mapped[1], false)
  elseif mapped[2] == "ar" then
    return ar_span.ArabicSpan(pandoc.Span(mapped[1], {class="ar"}))
  elseif mapped[2] == "aralt" then
    return ar_span.ArabicSpan(pandoc.Span(mapped[1], {class="aralt"}))
  else
    return pandoc.Span(mapped[1], {class=mapped[2]})
  end
  --return pandoc.Span(mapped[1], {class=mapped[2]})
end
function Span(el)
  if el.classes:includes 'subs' then
    local input_text = pandoc.utils.stringify(el)
    return get_output_text(input_text)
  end
end

