from BibResource import BibResource

def format_url_for_ar_div(url):
  return "[[" + url + "](" + url + ")]{lang='en'}"

def populate_resource_list():
  resource_list = []

  # Hadith collections
  resource_list.append(BibResource(
    "bukhari"
    , cit_text = "[صحيح البخاري]{.ar}"
    , bib_text = "صحيح البخاري، " + format_url_for_ar_div("https://sunnah.com/bukhari")
    ))

  resource_list.append(BibResource(
    "muslim"
    , cit_text = "[صحيح مسلم]{.ar}"
    , bib_text = "صحيح مسلم، " + format_url_for_ar_div("https://sunnah.com/muslim")
    ))

  resource_list.append(BibResource(
    "nasai"
    , cit_text = "[سنن النسائي]{.ar}"
    , bib_text = "[سنن النسائي]{.ar}، " + format_url_for_ar_div("https://sunnah.com/nasai")
    , sort_key = "سنن النسايي"
    ))
 
  resource_list.append(BibResource(
    "abudawud"
    , cit_text = "[سنن أبي داود]{.ar}"
    , bib_text = "[سنن أبي داود]{.ar}، " + format_url_for_ar_div("https://sunnah.com/abudawud")
    , sort_key = "سنن ابي داود"
    ))
 
  resource_list.append(BibResource(
    "tirmidhi"
    , cit_text = "[جامع الترمذي]{.ar}"
    , bib_text = "[جامع الترمذي]{.ar}، " + format_url_for_ar_div("https://sunnah.com/tirmidhi")
    ))
 
  resource_list.append(BibResource(
    "ibnmajah"
    , cit_text = "[سنن ابن ماجه]{.ar}"
    , bib_text = "[سنن ابن ماجه]{.ar}، " + format_url_for_ar_div("https://sunnah.com/ibnmajah")
    ))
 
  resource_list.append(BibResource(
    "malik"
    , cit_text = "[موطأ مالك]{.ar}"
    , bib_text = "[موطأ مالك]{.ar}، " + format_url_for_ar_div("https://sunnah.com/malik")
    , sort_key = "موطا مالك"
    ))
 
  resource_list.append(BibResource(
    "ahmad"
    , cit_text = "[مسند أحمد]{.ar}"
    , bib_text = "[مسند أحمد]{.ar}، " + format_url_for_ar_div("https://sunnah.com/ahmad")
    , sort_key = "مسند احمد"
    ))
 
  resource_list.append(BibResource(
    "darimi"
    , cit_text = "[سنن الدارمي]{.ar}"
    , bib_text = "[سنن الدارمي]{.ar}، " + format_url_for_ar_div("https://sunnah.com/darimi")
    ))
 
  resource_list.append(BibResource(
    "nawawi40"
    , cit_text = "[الأربعون النووية]{.ar}"
    , bib_text = "[الأربعون النووية]{.ar}، " + format_url_for_ar_div("https://sunnah.com/nawawi40")
    , sort_key = "اربعون النووية"
    ))
 
  resource_list.append(BibResource(
    "riyadussalihin"
    , cit_text = "[رياض الصالحين]{.ar}"
    , bib_text = "[رياض الصالحين]{.ar}، " + format_url_for_ar_div("https://sunnah.com/riyadussalihin")
    ))
 
  resource_list.append(BibResource(
    "adab"
    , cit_text = "[الأدب المفرد]{.ar}"
    , bib_text = "[الأدب المفرد]{.ar}، " + format_url_for_ar_div("https://sunnah.com/adab")
    , sort_key = "ادب المفرد"
    ))
 
  resource_list.append(BibResource(
    "shamail"
    , cit_text = "[الشمائل المحمدية]{.ar}"
    , bib_text = "[الشمائل المحمدية]{.ar}، " + format_url_for_ar_div("https://sunnah.com/shamail")
    , sort_key = "شمايل المحمدية"
    ))
 
  resource_list.append(BibResource(
    "mishkat"
    , cit_text = "[مشكاة المصابيح]{.ar}"
    , bib_text = "[مشكاة المصابيح]{.ar}، " + format_url_for_ar_div("https://sunnah.com/mishkat")
    ))
 
  resource_list.append(BibResource(
    "bulugh"
    , cit_text = "[بلوغ المرام]{.ar}"
    , bib_text = "[بلوغ المرام]{.ar}، " + format_url_for_ar_div("https://sunnah.com/bulugh")
    ))
 
  resource_list.append(BibResource(
    "forty"
    , cit_text = "[الأربعينات]{.ar}"
    , bib_text = "[الأربعينات]{.ar}، " + format_url_for_ar_div("https://sunnah.com/forty")
    , sort_key = "اربعينات"
    ))
 
  resource_list.append(BibResource(
    "hisn"
    , cit_text = "[حصن المسلم]{.ar}"
    , bib_text = "[حصن المسلم]{.ar}، " + format_url_for_ar_div("https://sunnah.com/hisn")
    ))

  # Tafsirs
  resource_list.append(BibResource(
    "albahr-almuheet"
    , cit_text = "[البحر المحيط لأبي حيان]{.ar}"
    , bib_text = "[البحر المحيط، تأليف: أبو حيان]{.ar}، " + format_url_for_ar_div("https://tafsir.app")
    , sort_key = "بحر المحيط"
    ))
 
  resource_list.append(BibResource(
    "ibn-aashoor"
    , cit_text = "[تفسير ابن عاشور]{.ar}"
    , bib_text = "[تفسير التحرير والتنوير، تأليف: ابن عاشور]{.ar}، " + format_url_for_ar_div("https://tafsir.app")
    , sort_key = "تفسير التحرير والتنوير"
    ))
 
  resource_list.append(BibResource(
    "tabari"
    , cit_text = "[تفسير الطبري]{.ar}"
    , bib_text = "[تفسير الطبري]{.ar}، " + format_url_for_ar_div("https://tafsir.app")
    ))
 
  resource_list.append(BibResource(
    "ibn-katheer"
    , cit_text = "[تفسير ابن كثير]{.ar}"
    , bib_text = "[تفسير ابن كثير]{.ar}، " + format_url_for_ar_div("https://tafsir.app")
    ))
 
  resource_list.append(BibResource(
    "ibn-alqayyim"
    , cit_text = "[تفسير ابن القيم]{.ar}"
    , bib_text = "[تفسير ابن القيم]{.ar}، " + format_url_for_ar_div("https://tafsir.app")
    ))
 
  resource_list.append(BibResource(
    "ibn-taymiyyah"
    , cit_text = "[تفسير ابن تيمية]{.ar}"
    , bib_text = "[تفسير ابن تيمية]{.ar}، " + format_url_for_ar_div("https://tafsir.app")
    ))
 
  resource_list.append(BibResource(
    "ibn-uthaymeen"
    , cit_text = "[تفسير ابن عثيمين]{.ar}"
    , bib_text = "[تفسير ابن عثيمين]{.ar}، " + format_url_for_ar_div("https://tafsir.app")
    ))
 
  resource_list.append(BibResource(
    "qurtubi"
    , cit_text = "[تفسير القرطبي]{.ar}"
    , bib_text = "[تفسير القرطبي]{.ar}، " + format_url_for_ar_div("https://tafsir.app")
    ))

  # General
  resource_list.append(BibResource(
    "nahw_wafi"
    , cit_text = "[النحو الوافي]{.ar}"
    , bib_text = "[النحو الوافي، تأليف: عباس حسن، دار المعارف.]{.ar}"
    , sort_key = "[نحو الوافي]{.ar}"
    ))
  
  resource_list.append(BibResource(
    "maani_nahw"
    , cit_text = "[معاني النحو]{.ar}"
    , bib_text = "[معاني النحو، تأليف: فاضل صالح السامرائي. الطبعة الثالثة، دار ابن كثير، 2022\\ م.]{.ar}"
    ))
  
  resource_list.append(BibResource(
    "nahw_arabi"
    , cit_text = "[النحو العربي: أحكام ومعان]{.ar}"
    , bib_text = "[النحو العربي: أحكام ومعان، تأليف: فاضل صالح السامرائي. الطبعة الأولى، دار ابن كثير، 2014\\ م.]{.ar}"
    , sort_key = "[نحو العربي احكام ومعان]{.ar}"
    ))
  
  resource_list.append(BibResource(
    "radiy_kafiyah"
    , cit_text = "[شرح الرضي على الكافية]{.ar}"
    , bib_text = "[شرح الكافية في النحو، تأليف: رضي الدين الأستراباذي (ت: 686\\ هـ).]{.ar}"
    ))
  
  resource_list.append(BibResource(
    "wright"
    , cit_text = "Wright"
    , bib_text = "Wright,\\ W., _Arabic grammar_, 3rd ed."
    ))
  
  resource_list.append(BibResource(
    "fischer"
    , cit_text = "Fischer"
    , bib_text = "Fischer,\\ W., _A grammar of classical Arabic_, 3rd rev. ed., translated by J.\\ Rodgers, Yale University Press."
    ))

  resource_list.append(BibResource(
    "sadan_subj"
    , cit_text = "Sadan,\\ A., _The Subjunctive Mood in Arabic Grammatical Thought_"
    , bib_text = "Sadan,\\ A., _The Subjunctive Mood in Arabic Grammatical Thought_, Brill, 2012. <https://doi.org/10.1163/9789004234239>"
    , sort_key = "Sadan A Subjunctive Mood in Arabic Grammatical Thought"
    ))

  return resource_list
