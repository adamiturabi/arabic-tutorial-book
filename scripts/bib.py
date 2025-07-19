from BibResource import BibResource

def format_url_ar(url):
  return "[[" + url + "](" + url + ")]{lang='en'}"

def populate_resource_list():
  resource_list = []

  # Hadith collections
  resource_list.append(BibResource(
    "bukhari"
    , cit_text = "[صحيح البخاري]{.ar}"
    , bib_text = "صحيح البخاري، " + format_url_ar("https://sunnah.com/bukhari")
    ))

  resource_list.append(BibResource(
    "muslim"
    , cit_text = "[صحيح مسلم]{.ar}"
    , bib_text = "صحيح مسلم، " + format_url_ar("https://sunnah.com/muslim")
    ))

  resource_list.append(BibResource(
    "nasai"
    , cit_text = "[سنن النسائي]{.ar}"
    , bib_text = "سنن النسائي، " + format_url_ar("https://sunnah.com/nasai")
    , sort_key = "سنن النسايي"
    ))
 
  resource_list.append(BibResource(
    "abudawud"
    , cit_text = "[سنن أبي داود]{.ar}"
    , bib_text = "سنن أبي داود، " + format_url_ar("https://sunnah.com/abudawud")
    , sort_key = "سنن ابي داود"
    ))
 
  resource_list.append(BibResource(
    "tirmidhi"
    , cit_text = "[جامع الترمذي]{.ar}"
    , bib_text = "جامع الترمذي، " + format_url_ar("https://sunnah.com/tirmidhi")
    ))
 
  resource_list.append(BibResource(
    "ibnmajah"
    , cit_text = "[سنن ابن ماجه]{.ar}"
    , bib_text = "سنن ابن ماجه، " + format_url_ar("https://sunnah.com/ibnmajah")
    ))
 
  resource_list.append(BibResource(
    "malik"
    , cit_text = "[موطأ مالك]{.ar}"
    , bib_text = "موطأ مالك، " + format_url_ar("https://sunnah.com/malik")
    , sort_key = "موطا مالك"
    ))
 
  resource_list.append(BibResource(
    "ahmad"
    , cit_text = "[مسند أحمد]{.ar}"
    , bib_text = "مسند أحمد، " + format_url_ar("https://sunnah.com/ahmad")
    , sort_key = "مسند احمد"
    ))
 
  resource_list.append(BibResource(
    "darimi"
    , cit_text = "[سنن الدارمي]{.ar}"
    , bib_text = "سنن الدارمي، " + format_url_ar("https://sunnah.com/darimi")
    ))
 
  resource_list.append(BibResource(
    "nawawi40"
    , cit_text = "[الأربعون النووية]{.ar}"
    , bib_text = "الأربعون النووية، " + format_url_ar("https://sunnah.com/nawawi40")
    , sort_key = "اربعون النووية"
    ))
 
  resource_list.append(BibResource(
    "riyadussalihin"
    , cit_text = "[رياض الصالحين]{.ar}"
    , bib_text = "رياض الصالحين، " + format_url_ar("https://sunnah.com/riyadussalihin")
    ))
 
  resource_list.append(BibResource(
    "adab"
    , cit_text = "[الأدب المفرد]{.ar}"
    , bib_text = "الأدب المفرد، " + format_url_ar("https://sunnah.com/adab")
    , sort_key = "ادب المفرد"
    ))
 
  resource_list.append(BibResource(
    "shamail"
    , cit_text = "[الشمائل المحمدية]{.ar}"
    , bib_text = "الشمائل المحمدية، " + format_url_ar("https://sunnah.com/shamail")
    , sort_key = "شمايل المحمدية"
    ))
 
  resource_list.append(BibResource(
    "mishkat"
    , cit_text = "[مشكاة المصابيح]{.ar}"
    , bib_text = "مشكاة المصابيح، " + format_url_ar("https://sunnah.com/mishkat")
    ))
 
  resource_list.append(BibResource(
    "bulugh"
    , cit_text = "[بلوغ المرام]{.ar}"
    , bib_text = "بلوغ المرام، " + format_url_ar("https://sunnah.com/bulugh")
    ))
 
  resource_list.append(BibResource(
    "forty"
    , cit_text = "[الأربعينات]{.ar}"
    , bib_text = "الأربعينات، " + format_url_ar("https://sunnah.com/forty")
    , sort_key = "اربعينات"
    ))
 
  resource_list.append(BibResource(
    "hisn"
    , cit_text = "[حصن المسلم]{.ar}"
    , bib_text = "حصن المسلم، " + format_url_ar("https://sunnah.com/hisn")
    ))

  resource_list.append(BibResource(
    "ibn_abi_shaybah"
    , cit_text = "[مصنف ابن أبي شيبة]{.ar}"
    , bib_text = "مصنف ابن أبي شيبة، تقديم وضبط: الحوت " + format_url_ar("https://shamela.ws/book/9944")
    , sort_key = "مصنف ابن ابي شيبة"
    ))

  resource_list.append(BibResource(
    "musnad_ahmad_risalah"
    , cit_text = "[مسند أحمد ط الرسالة]{.ar}"
    , bib_text = "مسند أحمد، تحقيق: شعيب الأرنؤوط، مؤسسة الرسالة  \n      " + format_url_ar("https://shamela.ws/book/25794")
    , sort_key = "مسند احمد ط الرسالة"
    ))

  # Tafsirs
  resource_list.append(BibResource(
    "albahr-almuheet"
    , cit_text = "[البحر المحيط لأبي حيان]{.ar}"
    , bib_text = "البحر المحيط، تأليف: أبو حيان، " + format_url_ar("https://tafsir.app")
    , sort_key = "بحر المحيط"
    ))
 
  resource_list.append(BibResource(
    "ibn-aashoor"
    , cit_text = "[تفسير ابن عاشور]{.ar}"
    , bib_text = "تفسير التحرير والتنوير، تأليف: ابن عاشور، " + format_url_ar("https://tafsir.app")
    , sort_key = "تفسير التحرير والتنوير"
    ))
 
  resource_list.append(BibResource(
    "tabari"
    , cit_text = "[تفسير الطبري]{.ar}"
    , bib_text = "تفسير الطبري، " + format_url_ar("https://tafsir.app")
    ))
 
  resource_list.append(BibResource(
    "ibn-katheer"
    , cit_text = "[تفسير ابن كثير]{.ar}"
    , bib_text = "تفسير ابن كثير، " + format_url_ar("https://tafsir.app")
    ))
 
  resource_list.append(BibResource(
    "ibn-alqayyim"
    , cit_text = "[تفسير ابن القيم]{.ar}"
    , bib_text = "تفسير ابن القيم، " + format_url_ar("https://tafsir.app")
    ))
 
  resource_list.append(BibResource(
    "ibn-taymiyyah"
    , cit_text = "[تفسير ابن تيمية]{.ar}"
    , bib_text = "تفسير ابن تيمية، " + format_url_ar("https://tafsir.app")
    ))
 
  resource_list.append(BibResource(
    "ibn-uthaymeen"
    , cit_text = "[تفسير ابن عثيمين]{.ar}"
    , bib_text = "تفسير ابن عثيمين، " + format_url_ar("https://tafsir.app")
    ))
 
  resource_list.append(BibResource(
    "qurtubi"
    , cit_text = "[تفسير القرطبي]{.ar}"
    , bib_text = "تفسير القرطبي، " + format_url_ar("https://tafsir.app")
    ))

  # General
  resource_list.append(BibResource(
    "nahw_wafi"
    , cit_text = "[النحو الوافي]{.ar}"
    , bib_text = "النحو الوافي، تأليف: عباس حسن، دار المعارف.  \n      " + format_url_ar("https://shamela.ws/book/10641")
    , sort_key = "نحو الوافي"
    ))
  
  resource_list.append(BibResource(
    "maani_nahw"
    , cit_text = "[معاني النحو]{.ar}"
    , bib_text = "معاني النحو، تأليف: فاضل صالح السامرائي. الطبعة الثالثة، دار ابن كثير، 2022\\ م."
    ))
  
  resource_list.append(BibResource(
    "nahw_arabi"
    , cit_text = "[النحو العربي: أحكام ومعان]{.ar}"
    , bib_text = "النحو العربي: أحكام ومعان، تأليف: فاضل صالح السامرائي. الطبعة الأولى، دار ابن كثير، 2014\\ م."
    , sort_key = "نحو العربي احكام ومعان"
    ))
  
  resource_list.append(BibResource(
    "radiy_kafiyah"
    , cit_text = "[شرح الرضي على الكافية]{.ar}"
    , bib_text = "شرح الرضي على الكافية، تأليف: الرضي الأستراباذي، تحقيق يوسف حسن عمر، جامعة قار يونس، ليبيا، 1395\\ هـ/1975\\ م  \n      " +format_url_ar("https://ketabonline.com/ar/books/23090")
    ))

  resource_list.append(BibResource(
    "ibn_ya3ish_mufassal"
    , cit_text = "[شرح ابن يعيش على المفصل]{.ar}"
    , bib_text = "شرح ابن يعيش على المفصل، " + format_url_ar("https://shamela.ws/book/13301")
    ))

  resource_list.append(BibResource(
    "qawa3id_shaykh_zadeh"
    , cit_text = "[شرح شيخ زاده على قواعد الإعراب]{.ar}"
    , bib_text = "شرح قواعد الإعراب، تأليف: محمد بن مصطفى القُوجَوي المعروف بشيخ زاده  \n      " + format_url_ar("https://shamela.ws/book/19236")
    , sort_key = "شرح شيخ زاده على قواعد الاعراب"
    ))

  resource_list.append(BibResource(
    "ibn_aqil_alfiyyah"
    , cit_text = "[شرح ابن عقيل على الألفية]{.ar}"
    , bib_text = "شرح ابن عقيل على الألفية، "+format_url_ar("https://shamela.ws/book/9904")
    , sort_key = "شرح ابن عقيل على الالفية"
    ))

  resource_list.append(BibResource(
    "za3balawi_dirasat"
    , cit_text = "[دراسات في النحو للزعبلاوي]{.ar}"
    , bib_text = "دراسات في النحو، تأليف: صلاح الدين الزعبلاوي، "+format_url_ar("https://shamela.ws/book/2120")
    , sort_key = "دراسات في النحو للزعبلاوي"
    ))

  resource_list.append(BibResource(
    "kafawi_kulliyyaat"
    , cit_text = "[الكليات للكفوي]{.ar}"
    , bib_text = "الكليات، تأليف: أبو البقاء الكفوي "+format_url_ar("https://shamela.ws/book/7037")
    , sort_key = "كليات للكفوي"
    ))

  resource_list.append(BibResource(
    "faysal_mansoor_articles"
    , cit_text = "[مجموع مقالات فيصل المنصور]{.ar}"
    , bib_text = "مجموع مقالات الدكتور فيصل بن علي المنصور في علوم العربية، النسخة الأولى، ١٤٤٢\\ هـ.  \n      "+format_url_ar("https://archive.org/details/riga2")
    , sort_key = "مجموع مقالات فيصل المنصور"
    ))

  # Western

  resource_list.append(BibResource(
    "wright"
    , cit_text = "Wright"
    , bib_text = "Wright,\\ W., _A grammar of the Arabic language_, 3rd ed., Cambridge University Press, 1896--1898. <https://archive.org/details/AGrammarOfTheArabicLanguageV1>"
    ))
  
  resource_list.append(BibResource(
    "fischer"
    , cit_text = "Fischer"
    , bib_text = "Fischer,\\ W., _A grammar of Classical Arabic_, 3rd rev. ed., translated by J.\\ Rodgers, Yale University Press, 2001."
    ))

  resource_list.append(BibResource(
    "sadan_subj"
    , cit_text = "Sadan,\\ A., _The subjunctive mood in Arabic grammatical thought_"
    , bib_text = "Sadan,\\ A., _The subjunctive mood in Arabic grammatical thought_, Brill, 2012. <https://doi.org/10.1163/9789004234239>"
    , sort_key = "Sadan A Subjunctive Mood in Arabic Grammatical Thought"
    ))

  resource_list.append(BibResource(
    "jallad_wawation"
    , cit_text = 'Al-Jallad,\\ A., "One wāw to rule them all: The origins and fate of wawation in Arabic and its orthography"'
    , bib_text = 'Al-Jallad,\\ A., "One wāw to rule them all: The origins and fate of wawation in Arabic and its orthography," in: _Scripts and scripture: Writing and religion in Arabia circa 500--700\\ [ce]{.smallcaps}_, pp.\\ 87--104. The Oriental Institute of the University of Chicago, 2022. <https://www.academia.edu/33017695>'
    , sort_key = "Jallad A One waw to rule them all"
    ))

  resource_list.append(BibResource(
    "hallberg_thesis"
    , cit_text = 'Hallberg,\ A., _Case endings in Spoken Standard Arabic_'
    , bib_text = 'Hallberg,\\ A., _Case endings in Spoken Standard Arabic_. Doctoral thesis, Lund University, 2016. <https://lup.lub.lu.se/record/8524489>'
    , sort_key = "Hallberg A Case endings in Spoken Standard Arabic"
    ))

  resource_list.append(BibResource(
    "cantarino_smap"
    , cit_text = 'Cantarino,\\ V., _Syntax of modern Arabic prose_'
    , bib_text = 'Cantarino,\\ V., _Syntax of modern Arabic prose_, Indiana University Press, 1974.'
    , sort_key = 'Cantarino V Syntax of modern Arabic prose'
    ))
  resource_list.append(BibResource(
    "brock_grund"
    , cit_text = 'Brockelmann,\\ C., _Grundriss der vergleichenden Grammatik der semitischen Sprachen_'
    , bib_text = 'Brockelmann,\\ C., _Grundriss der vergleichenden Grammatik der semitischen Sprachen_, Verlag von Reuther & Reichard, 1908--1913.'
    , sort_key = 'Brockelmann C Grundriss der vergleichenden Grammatik der semitischen Sprachen'
    ))
  return resource_list

