package.path = package.path .. ';../_extensions/arabic-support/?.lua'
local ar_span = require("ar_span")


function Link(el)
  stringify = pandoc.utils.stringify
  if #el.content == 1 then
    local ft = stringify(el.content[1])
    if not string.find(ft, " ") then -- only use this filter if the link comprises the entire footnote
      local i, j = string.find(ft, "https://quran.com/")
      if i ~= nil then
        local surah_and_verse = string.sub(ft, j+1, -1)
        local sep_loc = string.find(surah_and_verse, ":")
        if sep_loc == nil then
          sep_loc = string.find(surah_and_verse, "/")
        end
        local surah_index = string.sub(surah_and_verse, 1, sep_loc-1)
        local verse_index = string.sub(surah_and_verse, sep_loc+1, -1)
        local surah_names = {
[1] = "الفاتحة",
[2] = "البقرة",
[3] = "آل عمران",
[4] = "النساء",
[5] = "المائدة",
[6] = "الأنعام",
[7] = "الأعراف",
[8] = "الأنفال",
[9] = "التوبة",
[10] = "يونس",
[11] = "هود",
[12] = "يوسف",
[13] = "الرعد",
[14] = "إبراهيم",
[15] = "الحجر",
[16] = "النحل",
[17] = "الإسراء",
[18] = "الكهف",
[19] = "مريم",
[20] = "طه",
[21] = "الأنبياء",
[22] = "الحج",
[23] = "المؤمنون",
[24] = "النور",
[25] = "الفرقان",
[26] = "الشعراء",
[27] = "النمل",
[28] = "القصص",
[29] = "العنكبوت",
[30] = "الروم",
[31] = "لقمان",
[32] = "السجدة",
[33] = "الأحزاب",
[34] = "سبأ",
[35] = "فاطر",
[36] = "يس",
[37] = "الصافات",
[38] = "ص",
[39] = "الزمر",
[40] = "غافر",
[41] = "فصلت",
[42] = "الشورى",
[43] = "الزخرف",
[44] = "الدخان",
[45] = "الجاثية",
[46] = "الأحقاف",
[47] = "محمد",
[48] = "الفتح",
[49] = "الحجرات",
[50] = "ق",
[51] = "الذاريات",
[52] = "الطور",
[53] = "النجم",
[54] = "القمر",
[55] = "الرحمن",
[56] = "الواقعة",
[57] = "الحديد",
[58] = "المجادلة",
[59] = "الحشر",
[60] = "الممتحنة",
[61] = "الصف",
[62] = "الجمعة",
[63] = "المنافقون",
[64] = "التغابن",
[65] = "الطلاق",
[66] = "التحريم",
[67] = "الملك",
[68] = "القلم",
[69] = "الحاقة",
[70] = "المعارج",
[71] = "نوح",
[72] = "الجن",
[73] = "المزمل",
[74] = "المدثر",
[75] = "القيامة",
[76] = "الإنسان",
[77] = "المرسلات",
[78] = "النبأ",
[79] = "النازعات",
[80] = "عبس",
[81] = "التكوير",
[82] = "الانفطار",
[83] = "المطففين",
[84] = "الانشقاق",
[85] = "البروج",
[86] = "الطارق",
[87] = "الأعلى",
[88] = "الغاشية",
[89] = "الفجر",
[90] = "البلد",
[91] = "الشمس",
[92] = "الليل",
[93] = "الضحى",
[94] = "الشرح",
[95] = "التين",
[96] = "العلق",
[97] = "القدر",
[98] = "البينة",
[99] = "الزلزلة",
[100] = "العاديات",
[101] = "القارعة",
[102] = "التكاثر",
[103] = "العصر",
[104] = "الهمزة",
[105] = "الفيل",
[106] = "قريش",
[107] = "الماعون",
[108] = "الكوثر",
[109] = "الكافرون",
[110] = "النصر",
[111] = "المسد",
[112] = "الإخلاص",
[113] = "الفلق",
[114] = "الناس",


        }
        local arabic_text = "سورة " .. surah_names[tonumber(surah_index)]
        local index_text = " " .. surah_index .. ":" .. verse_index
        --local arabic_span
        --if FORMAT:match 'latex' then
        --  arabic_span = pandoc.Span(surah_name, {class="reg-ar-span", lang='ar'})
        --elseif FORMAT:match 'html' then
        --  arabic_span = pandoc.Span(surah_name, {class="reg-ar-span", lang='ar', dir='rtl'})
        --end
        --return pandoc.Link({arabic_span, index_text}, ft)
        return pandoc.Link({ar_span.ArabicSpan(pandoc.Span(arabic_text, {class="ar"})), index_text}, ft)
      end
      local i, j = string.find(ft, "https://sunnah.com/")
      if i ~= nil then
        local book_and_hadith = string.sub(ft, j+1, -1)
        local sep_loc = string.find(book_and_hadith, ":")
        if sep_loc == nil then
          sep_loc = string.find(book_and_hadith, "/")
        end
        local book_index = string.sub(book_and_hadith, 1, sep_loc-1)
        local hadith_index = string.sub(book_and_hadith, sep_loc+1, -1)
        local book_names = {
["bukhari"] = "صحيح البخاري",
["muslim"] = "صحيح مسلم",
["nasai"] = "سنن النسائي",
["abudawud"] = "سنن أبي داود",
["tirmidhi"] = "جامع الترمذي",
["ibnmajah"] = "سنن ابن ماجه",
["malik"] = "موطأ مالك",
["ahmad"] = "مسند أحمد",
["darimi"] = "سنن الدارمي",
["nawawi40"] = "الأربعون النووية",
["riyadussalihin"] = "رياض الصالحين",
["adab"] = "الأدب المفرد",
["shamail"] = "الشمائل المحمدية",
["mishkat"] = "مشكاة المصابيح",
["bulugh"] = "بلوغ المرام",
["forty"] = "الأربعينات",
["hisn"] = " حصن المسلم",
        }
        local arabic_text = book_names[book_index]
        local index_text = " :" .. hadith_index
        --local arabic_span
        --if FORMAT:match 'latex' then
        --  arabic_span = pandoc.Span(book_name, {class="reg-ar-span", lang='ar'})
        --elseif FORMAT:match 'html' then
        --  arabic_span = pandoc.Span(book_name, {class="reg-ar-span", lang='ar', dir='rtl'})
        --end
        --return pandoc.Link({arabic_span, index_text}, ft)
        return pandoc.Link({ar_span.ArabicSpan(pandoc.Span(arabic_text, {class="ar"})), index_text}, ft)
      end
    end
  end
end

