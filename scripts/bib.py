from BibResource import BibResource

def format_url_ar(url):
  return "[[" + url + "](" + url + ")]{lang='en'}"

def populate_resource_list():
  resource_list = []

  resource_list.append(BibResource(
    "quran"
    , cit_type = "corpus"
    , cit_text = ""
    , bib_text = "القرآن، " + format_url_ar("https://quran.com")
    , sort_key = "اااااا"
    ))

  # Hadith collections
  resource_list.append(BibResource(
    "bukhari"
    , cit_type = "corpus"
    , cit_text = "[صحيح البخاري]{.ar}"
    , bib_text = "صحيح البخاري، " + format_url_ar("https://sunnah.com/bukhari")
    ))

  resource_list.append(BibResource(
    "muslim"
    , cit_type = "corpus"
    , cit_text = "[صحيح مسلم]{.ar}"
    , bib_text = "صحيح مسلم، " + format_url_ar("https://sunnah.com/muslim")
    ))

  resource_list.append(BibResource(
    "nasai"
    , cit_type = "corpus"
    , cit_text = "[سنن النسائي]{.ar}"
    , bib_text = "سنن النسائي، " + format_url_ar("https://sunnah.com/nasai")
    , sort_key = "سنن النسايي"
    ))
 
  resource_list.append(BibResource(
    "abudawud"
    , cit_type = "corpus"
    , cit_text = "[سنن أبي داود]{.ar}"
    , bib_text = "سنن أبي داود، " + format_url_ar("https://sunnah.com/abudawud")
    , sort_key = "سنن ابي داود"
    ))
 
  resource_list.append(BibResource(
    "tirmidhi"
    , cit_type = "corpus"
    , cit_text = "[جامع الترمذي]{.ar}"
    , bib_text = "جامع الترمذي، " + format_url_ar("https://sunnah.com/tirmidhi")
    ))
 
  resource_list.append(BibResource(
    "ibnmajah"
    , cit_type = "corpus"
    , cit_text = "[سنن ابن ماجه]{.ar}"
    , bib_text = "سنن ابن ماجه، " + format_url_ar("https://sunnah.com/ibnmajah")
    ))
 
  resource_list.append(BibResource(
    "malik"
    , cit_type = "corpus"
    , cit_text = "[موطأ مالك]{.ar}"
    , bib_text = "موطأ مالك، " + format_url_ar("https://sunnah.com/malik")
    , sort_key = "موطا مالك"
    ))
 
  resource_list.append(BibResource(
    "ahmad"
    , cit_type = "corpus"
    , cit_text = "[مسند أحمد]{.ar}"
    , bib_text = "مسند أحمد، " + format_url_ar("https://sunnah.com/ahmad")
    , sort_key = "مسند احمد"
    ))
 
  resource_list.append(BibResource(
    "darimi"
    , cit_type = "corpus"
    , cit_text = "[سنن الدارمي]{.ar}"
    , bib_text = "سنن الدارمي، " + format_url_ar("https://sunnah.com/darimi")
    ))
 
  resource_list.append(BibResource(
    "nawawi40"
    , cit_type = "corpus"
    , cit_text = "[الأربعون النووية]{.ar}"
    , bib_text = "الأربعون النووية، " + format_url_ar("https://sunnah.com/nawawi40")
    , sort_key = "اربعون النووية"
    ))
 
  resource_list.append(BibResource(
    "riyadussalihin"
    , cit_type = "corpus"
    , cit_text = "[رياض الصالحين]{.ar}"
    , bib_text = "رياض الصالحين، " + format_url_ar("https://sunnah.com/riyadussalihin")
    ))
 
  resource_list.append(BibResource(
    "adab"
    , cit_type = "corpus"
    , cit_text = "[الأدب المفرد]{.ar}"
    , bib_text = "الأدب المفرد، " + format_url_ar("https://sunnah.com/adab")
    , sort_key = "ادب المفرد"
    ))
 
  resource_list.append(BibResource(
    "shamail"
    , cit_type = "corpus"
    , cit_text = "[الشمائل المحمدية]{.ar}"
    , bib_text = "الشمائل المحمدية، " + format_url_ar("https://sunnah.com/shamail")
    , sort_key = "شمايل المحمدية"
    ))
 
  resource_list.append(BibResource(
    "mishkat"
    , cit_type = "corpus"
    , cit_text = "[مشكاة المصابيح]{.ar}"
    , bib_text = "مشكاة المصابيح، " + format_url_ar("https://sunnah.com/mishkat")
    ))
 
  resource_list.append(BibResource(
    "bulugh"
    , cit_type = "corpus"
    , cit_text = "[بلوغ المرام]{.ar}"
    , bib_text = "بلوغ المرام، " + format_url_ar("https://sunnah.com/bulugh")
    ))
 
  resource_list.append(BibResource(
    "forty"
    , cit_type = "corpus"
    , cit_text = "[الأربعينات]{.ar}"
    , bib_text = "الأربعينات، " + format_url_ar("https://sunnah.com/forty")
    , sort_key = "اربعينات"
    ))
 
  resource_list.append(BibResource(
    "hisn"
    , cit_type = "corpus"
    , cit_text = "[حصن المسلم]{.ar}"
    , bib_text = "حصن المسلم، " + format_url_ar("https://sunnah.com/hisn")
    ))

  resource_list.append(BibResource(
    "ibn_abi_shaybah"
    , cit_type = "corpus"
    , cit_text = "[مصنف ابن أبي شيبة]{.ar}"
    , bib_text = "مصنف ابن أبي شيبة، تقديم وضبط: الحوت " + format_url_ar("https://shamela.ws/book/9944")
    , sort_key = "مصنف ابن ابي شيبة"
    ))

  resource_list.append(BibResource(
    "musnad_ahmad_risalah"
    , cit_type = "corpus"
    , cit_text = "[مسند أحمد ط الرسالة]{.ar}"
    , bib_text = "مسند أحمد، تحقيق: شعيب الأرنؤوط، مؤسسة الرسالة  \n      " + format_url_ar("https://shamela.ws/book/25794")
    , sort_key = "مسند احمد ط الرسالة"
    ))

  # Tafsirs
  resource_list.append(BibResource(
    "albahr-almuheet"
    , cit_type = "ar_ref"
    , cit_text = "[البحر المحيط لأبي حيان]{.ar}"
    , bib_text = "البحر المحيط، تأليف: أبو حيان، " + format_url_ar("https://tafsir.app")
    , sort_key = "بحر المحيط"
    ))
 
  resource_list.append(BibResource(
    "ibn-aashoor"
    , cit_type = "ar_ref"
    , cit_text = "[تفسير ابن عاشور]{.ar}"
    , bib_text = "تفسير التحرير والتنوير، تأليف: ابن عاشور، " + format_url_ar("https://tafsir.app")
    , sort_key = "تفسير التحرير والتنوير"
    ))
 
  resource_list.append(BibResource(
    "tabari"
    , cit_type = "ar_ref"
    , cit_text = "[تفسير الطبري]{.ar}"
    , bib_text = "تفسير الطبري، " + format_url_ar("https://tafsir.app")
    ))
 
  resource_list.append(BibResource(
    "ibn-katheer"
    , cit_type = "ar_ref"
    , cit_text = "[تفسير ابن كثير]{.ar}"
    , bib_text = "تفسير ابن كثير، " + format_url_ar("https://tafsir.app")
    ))
 
  resource_list.append(BibResource(
    "m-sahabah"
    , cit_type = "ar_ref"
    , cit_text = "[القراءات العشر من الشاطبية والدرة — دار الصحابة]{.ar}"
    , bib_text = "القراءات العشر من الشاطبية والدرة — دار الصحابة، " + format_url_ar("https://tafsir.app")
    , sort_key = "قراات العشر من الشاطبية والدرة"
    ))

  resource_list.append(BibResource(
    "ibn-alqayyim"
    , cit_type = "ar_ref"
    , cit_text = "[تفسير ابن القيم]{.ar}"
    , bib_text = "تفسير ابن القيم، " + format_url_ar("https://tafsir.app")
    ))
 
  resource_list.append(BibResource(
    "ibn-taymiyyah"
    , cit_type = "ar_ref"
    , cit_text = "[تفسير ابن تيمية]{.ar}"
    , bib_text = "تفسير ابن تيمية، " + format_url_ar("https://tafsir.app")
    ))
 
  resource_list.append(BibResource(
    "ibn-uthaymeen"
    , cit_type = "ar_ref"
    , cit_text = "[تفسير ابن عثيمين]{.ar}"
    , bib_text = "تفسير ابن عثيمين، " + format_url_ar("https://tafsir.app")
    ))

  resource_list.append(BibResource(
    "kashaf"
    , cit_type = "ar_ref"
    , cit_text = "[الكشاف للزمخشري]{.ar}"
    , bib_text = "الكشاف للزمخشري، " + format_url_ar("https://tafsir.app")
    , sort_key = "كشاف للزمخشري"
    ))
 
  resource_list.append(BibResource(
    "qurtubi"
    , cit_type = "ar_ref"
    , cit_text = "[تفسير القرطبي]{.ar}"
    , bib_text = "تفسير القرطبي، " + format_url_ar("https://tafsir.app")
    ))

  resource_list.append(BibResource(
    "farraa"
    , cit_type = "ar_ref"
    , cit_text = "[معاني القرآن للفراء]{.ar}"
    , bib_text = "معاني القرآن للفراء، " + format_url_ar("https://tafsir.app")
    , sort_key = "معاني القران للفرا"
    ))

  resource_list.append(BibResource(
    "iraab-aldarweesh"
    , cit_type = "ar_ref"
    , cit_text = "[إعراب القرآن للدرويش]{.ar}"
    , bib_text = "إعراب القرآن للدرويش، " + format_url_ar("https://tafsir.app")
    , sort_key = "اعراب القران للدرويش"
    ))

  resource_list.append(BibResource(
    "aldur-almasoon"
    , cit_type = "ar_ref"
    , cit_text = "[الدر المصون للسمين الحلبي]{.ar}"
    , bib_text = "الدر المصون للسمين الحلبي، " + format_url_ar("https://tafsir.app")
    , sort_key = "الدر المصون للسمين الحلبي"
    ))
  resource_list.append(BibResource(
    "iraab-daas"
    , cit_type = "ar_ref"
    , cit_text = "[إعراب القرآن للدعاس]{.ar}"
    , bib_text = "إعراب القرآن للدعاس، " + format_url_ar("https://tafsir.app")
    , sort_key = "اعراب القران للدعاس"
    ))


  # General
  resource_list.append(BibResource(
    "nahw_wafi"
    , cit_type = "ar_ref"
    , cit_text = "[النحو الوافي]{.ar}"
    , bib_text = "النحو الوافي، تأليف: عباس حسن، دار المعارف.  \n      " + format_url_ar("https://shamela.ws/book/10641")
    , sort_key = "نحو الوافي"
    ))
  
  resource_list.append(BibResource(
    "maani_nahw"
    , cit_type = "ar_ref"
    , cit_text = "[معاني النحو]{.ar}"
    , bib_text = "معاني النحو، تأليف: فاضل صالح السامرائي. الطبعة الثالثة، دار ابن كثير، 2022\\ م."
    ))
  
  resource_list.append(BibResource(
    "nahw_arabi"
    , cit_type = "ar_ref"
    , cit_text = "[النحو العربي: أحكام ومعان]{.ar}"
    , bib_text = "النحو العربي: أحكام ومعان، تأليف: فاضل صالح السامرائي. الطبعة الأولى، دار ابن كثير، 2014\\ م."
    , sort_key = "نحو العربي احكام ومعان"
    ))
  
  resource_list.append(BibResource(
    "muqtadab"
    , cit_type = "ar_ref"
    , cit_text = "[المقتضب للمبرد]{.ar}"
    , bib_text = "المقتضب للمبرد، " +format_url_ar("https://shamela.ws/book/6965")
    , sort_key = "مقتضب للمبرد"
    ))

  resource_list.append(BibResource(
    "maani_zajjaj"
    , cit_type = "ar_ref"
    , cit_text = "[معاني القرآن وإعرابه للزجاج]{.ar}"
    , bib_text = "معاني القرآن وإعرابه للزجاج" +format_url_ar("https://shamela.ws/book/922")
    , sort_key = "[معاني القران واعرابه للزجاج]{.ar}"
    ))

  resource_list.append(BibResource(
    "radiy_kafiyah"
    , cit_type = "ar_ref"
    , cit_text = "[شرح الرضي على الكافية]{.ar}"
    , bib_text = "شرح الرضي على الكافية، تأليف: الرضي الأستراباذي، تحقيق يوسف حسن عمر، جامعة قار يونس، ليبيا، 1395\\ هـ/1975\\ م  \n      " +format_url_ar("https://ketabonline.com/ar/books/23090")
    ))

  resource_list.append(BibResource(
    "ibn_ya3ish_mufassal"
    , cit_type = "ar_ref"
    , cit_text = "[شرح ابن يعيش على المفصل]{.ar}"
    , bib_text = "شرح ابن يعيش على المفصل، " + format_url_ar("https://shamela.ws/book/13301")
    ))

  resource_list.append(BibResource(
    "qawa3id_shaykh_zadeh"
    , cit_type = "ar_ref"
    , cit_text = "[شرح شيخ زاده على قواعد الإعراب]{.ar}"
    , bib_text = "شرح قواعد الإعراب، تأليف: محمد بن مصطفى القُوجَوي المعروف بشيخ زاده  \n      " + format_url_ar("https://shamela.ws/book/19236")
    , sort_key = "شرح شيخ زاده على قواعد الاعراب"
    ))

  resource_list.append(BibResource(
    "ibn_aqil_alfiyyah"
    , cit_type = "ar_ref"
    , cit_text = "[شرح ابن عقيل على الألفية]{.ar}"
    , bib_text = "شرح ابن عقيل على الألفية، "+format_url_ar("https://shamela.ws/book/9904")
    , sort_key = "شرح ابن عقيل على الالفية"
    ))

  resource_list.append(BibResource(
    "ibn_hisham_awdah_almasaalik"
    , cit_type = "ar_ref"
    , cit_text = "[أوضح المسالك لابن هشام]{.ar}"
    , bib_text = "أوضح المسالك إلى ألفية ابن مالك لابن هشام  \n      "+format_url_ar("https://shamela.ws/book/11825")
    , sort_key = "اوضح المسالك الى الفية ابن مالك لابن هشام"
    ))

  resource_list.append(BibResource(
    "sarraj_usool"
    , cit_type = "ar_ref"
    , cit_text = "[الأصول في النحو لابن السراج]{.ar}"
    , bib_text = "الأصول في النحو لابن السراج  \n      "+format_url_ar("https://shamela.ws/book/7365")
    , sort_key = "اصول في النحو لابن السراج"
    ))

  resource_list.append(BibResource(
    "sabban"
    , cit_type = "ar_ref"
    , cit_text = "[حاشية الصبان على شرح الأشمونى لألفية ابن مالك]{.ar}"
    , bib_text = "حاشية الصبان على شرح الأشمونى لألفية ابن مالك  \n      "+format_url_ar("https://shamela.ws/book/11539")
    , sort_key = "حاشيه الصبان على شرح الاشمونى لالفية ابن مالك"
    ))

  resource_list.append(BibResource(
    "ibn_jinni_khasaais"
    , cit_type = "ar_ref"
    , cit_text = "[الخصائص لابن جني]{.ar}"
    , bib_text = "الخصائص لابن جني  \n      "+format_url_ar("https://shamela.ws/book/9986")
    , sort_key = "خصايص لابن جني"
    ))

  resource_list.append(BibResource(
    "za3balawi_dirasat"
    , cit_type = "ar_ref"
    , cit_text = "[دراسات في النحو للزعبلاوي]{.ar}"
    , bib_text = "دراسات في النحو، تأليف: صلاح الدين الزعبلاوي، "+format_url_ar("https://shamela.ws/book/2120")
    , sort_key = "دراسات في النحو للزعبلاوي"
    ))

  resource_list.append(BibResource(
    "kafawi_kulliyyaat"
    , cit_type = "ar_ref"
    , cit_text = "[الكليات للكفوي]{.ar}"
    , bib_text = "الكليات، تأليف: أبو البقاء الكفوي "+format_url_ar("https://shamela.ws/book/7037")
    , sort_key = "كليات للكفوي"
    ))

  resource_list.append(BibResource(
    "faysal_mansoor_articles"
    , cit_type = "ar_ref"
    , cit_text = "[مجموع مقالات فيصل المنصور]{.ar}"
    , bib_text = "مجموع مقالات الدكتور فيصل بن علي المنصور في علوم العربية، النسخة الأولى، ١٤٤٢\\ هـ.  \n      "+format_url_ar("https://archive.org/details/riga2")
    , sort_key = "مجموع مقالات فيصل المنصور"
    ))

  resource_list.append(BibResource(
    "zidan_wujoob_waw"
    , cit_type = "ar_ref"
    , cit_text = "[وجوب الربط بالواو لعبد الجبار فتحي زيدان]{.ar}"
    , bib_text = "وجوب الربط بالواو لعبد الجبار فتحي زيدان  \n      " + format_url_ar("https://www.alukah.net/literature_language/0/173870")
    ))

  resource_list.append(BibResource(
    "zidan_haalaat_rabt_waw"
    , cit_type = "ar_ref"
    , cit_text = "[حالات الربط بواو الحال الجبار فتحي زيدان]{.ar}"
    , bib_text = "حالات الربط بواو الحال الجبار فتحي زيدان  \n      " + format_url_ar("https://www.alukah.net/literature_language/0/173759")
    ))

  resource_list.append(BibResource(
    "dalaail_jurjani"
    , cit_type = "ar_ref"
    , cit_text = "[دلائل الإعجاز للجرجاني]{.ar}"
    , bib_text = "دلائل الإعجاز للجرجاني  \n      " + format_url_ar("https://shamela.ws/book/12055")
    , sort_key = "دلايل الاعجاز للجرجاني"
    ))
  resource_list.append(BibResource(
    "jurjani_muqtasid"
    , cit_type = "ar_ref"
    , cit_text = "[المقتصد للجرجاني]{.ar}"
    , bib_text = "المقتصد في شرح الإيضاح للجرجاني  \n      " + format_url_ar("https://archive.org/details/2271pdf_201912")
    , sort_key = "مقتصد في شرح الايضاح للجرجاني"
    ))

  resource_list.append(BibResource(
    "abu_hayyan_tadhyeel"
    , cit_type = "ar_ref"
    , cit_text = "[التذييل والتكميل لأبي حيان]{.ar}"
    , bib_text = "التذييل والتكميل في شرح كتاب التسهيل لأبي حيان الأندلسي  \n      " + format_url_ar("https://shamela.ws/book/17116")
    , sort_key = "تذييل والتكميل لابي حيان"
    ))

  resource_list.append(BibResource(
    "ibn_hisham_mughni"
    , cit_type = "ar_ref"
    , cit_text = "[مغني اللبيب لابن هشام]{.ar}"
    , bib_text = "مغني اللبيب عن كتب الأعاريب لابن هشام  \n      " + format_url_ar("https://shamela.ws/book/6972")
    , sort_key = "مغني اللبيب لابن هشام"
    ))

  resource_list.append(BibResource(
    "tasreeh_hashiyat_yasin"
    , cit_type = "ar_ref"
    , cit_text = "[شرح التصريح وحاشية ياسين]{.ar}"
    , bib_text = "شرح التصريح وحاشية ياسين  \n      " + format_url_ar("https://archive.org/details/hmmt00291/")
    , sort_key = "شرح التصريح وحاشية ياسين"
    ))

  resource_list.append(BibResource(
    "3akbari_tibyan"
    , cit_type = "ar_ref"
    , cit_text = "[التبيان في إعراب القرآن للعكبري]{.ar}"
    , bib_text = "التبيان في إعراب القرآن للعكبري  \n      " + format_url_ar("https://shamela.ws/book/22928")
    , sort_key = "تبيان في اعراب القران للعكبري"
    ))

  resource_list.append(BibResource(
    "anbari_asrar"
    , cit_type = "ar_ref"
    , cit_text = "[أسرار العربية للأنباري]{.ar}"
    , bib_text = "أسرار العربية للأنباري  \n      " + format_url_ar("https://shamela.ws/book/7502")
    , sort_key = "اسرار العربية للانباري"
    ))

  resource_list.append(BibResource(
    "ghalayini_jaami3"
    , cit_type = "ar_ref"
    , cit_text = "[جامع الدروس العربية لمصطفى الغلاييني]{.ar}"
    , bib_text = "جامع الدروس العربية لمصطفى الغلاييني  \n      " + format_url_ar("https://shamela.ws/book/6972")
    , sort_key = "جامع الدروس العربيه لمصطفي الغلاييني"
    ))

  resource_list.append(BibResource(
    "ali_hani_min_ba3d"
    , cit_type = "ar_ref"
    , cit_text = "[من الفرق بين بعد ومن بعد في اللفظ القرآني لعلي هاني]{.ar}"
    , bib_text = "من الفرق بين بعد ومن بعد في اللفظ القرآني لعلي هاني"
    , sort_key = "من الفرق بين بعد ومن بعد في اللفظ القراني لعلي هاني"
    ))

  resource_list.append(BibResource(
    "ali_hani_ta3alluq"
    , cit_type = "ar_ref"
    , cit_text = "[استيفاء حالات تعلق الجار والمجرور و الظرف وأثره في المعنى لعلي هاني]{.ar}"
    , bib_text = "استيفاء حالات تعلق الجار والمجرور و الظرف وأثره في المعنى لعلي هاني"
    , sort_key = "استيفا حالات تعلق الجار والمجرور و الظرف واثره في المعنى لعلي هاني"
    ))
  resource_list.append(BibResource(
    "ibn_qayyim_juyoosh"
    , cit_type = "ar_ref"
    , cit_text = "[اجتماع الجيوش الإسلامية لابن القيم]{.ar}"
    , bib_text = "اجتماع الجيوش الإسلامية لابن القيم  \n      " + format_url_ar("https://shamela.ws/book/18632/80")
    , sort_key = "اجتماع الجيوش الاسلامية لابن القيم"
    ))
  resource_list.append(BibResource(
    "ibn_3usfoor_sharh_jumal"
    , cit_type = "ar_ref"
    , cit_text = "[شرح جمل الزجاجي لابن عصفور]{.ar}"
    , bib_text = "الكتاب : شرح جمل الزجاجي تأليف : ابن عصفور الإشبيلي"
    , sort_key = "شرح جمل الزجاجي لابن عصفور"
    ))
  resource_list.append(BibResource(
    "farisi_idah"
    , cit_type = "ar_ref"
    , cit_text = "[الإيضاح للفارسي]{.ar}"
    , bib_text = """
      الكتاب: الإيضاح العضدي  
      المؤلف: أبو علي الفارسيّ (٢٨٨ - ٣٧٧ هـ)  
      المحقق: د. حسن شاذلي فرهود (كلية الآداب - جامعة الرياض)  
      الطبعة: الأولى، ١٣٨٩ هـ - ١٩٦٩ م.  
      """ + format_url_ar("https://shamela.ws/book/20961")
    , sort_key = "ايضاح للفارسي"
    ))
  resource_list.append(BibResource(
    "shadi_ism_faa3il"
    , cit_type = "ar_ref"
    , cit_text = "[دلالة سياق اسم الفاعل في الحديث النبوي الشريف صحيح مسلم أنموذجًا لشادي محمد جميل عايش]{.ar}"
    , bib_text = """
      الكتاب: دلالة سياق اسم الفاعل في الحديث النبوي الشريف صحيح مسلم أنموذجًا  
      المؤلف: شادي محمد جميل عايش  
      رسالة درجة الماجستر  
      جامعة الشرق الأوسط  
      """
    , sort_key = "دلالة سياق اسم الفاعل في الحديث النبوي الشريف صحيح مسلم"
    ))
  resource_list.append(BibResource(
    "samarrai_jumlah"
    , cit_type = "ar_ref"
    , cit_text = "[الجملة العربية لفاضل السامرائي]{.ar}"
    , bib_text = """
      الكتاب: الجملة العربية تأليفها وأقسامها 
      المؤلف: فاضل السامرائي
      """
    , sort_key = "الجملة العربية لفاضل السامرايي"
    ))
  resource_list.append(BibResource(
    "hamid_ism_faa3il"
    , cit_type = "ar_ref"
    , cit_text = "[تحرير اسم الفاعل من مزاعم المجاراة لحامد علي أبو صعيليك]{.ar}"
    , bib_text = """
      الكتاب: تحرير اسم الفاعل من مزاعم المجاراة  
      المؤلف: د. حامد علي أبو صعيليك  
      الناشر: مجلة مجمع اللغة العربية الأردني، (ص 119 ـ 158)  
      """ + format_url_ar("https://ketabonline.com/ar/books/105878")
    , sort_key = "تحرير اسم الفاعل من مزاعم المجاراة لحامد علي ابو صعيليك"
    ))
  resource_list.append(BibResource(
    "taftazani_mukhtasar_maani"
    , cit_type = "ar_ref"
    , cit_text = "[مختصر المعاني للتفتازاني]{.ar}"
    , bib_text = """
      الكتاب: مختصر المعاني (مختصر لشرح تلخيص المفتاح)  
      المؤلف: سعد الدين مسعود بن عمر بن عبد الله التفتازاني الشافعي (المتوفى: 793 هـ)  
      الناشر: دار الفكر - قم  
      الطبعة: الأولى، 1411 هـ  
      """ + format_url_ar("https://ketabonline.com/ar/books/16360")
    , sort_key = "مختصر المعاني للتفتازاني"
    ))
  resource_list.append(BibResource(
    "suyooti_ashbaah"
    , cit_type = "ar_ref"
    , cit_text = "[الأشباه والنظائر للسيوطي]{.ar}"
    , bib_text = """
      الكتاب: الأشباه والنظائر في في النحو
      المؤلف: جلال الدين عبد الرحمن السيوطي (ت ٩١١ هـ)  
      الناشر: دار الكتب العلمية  
      """ + format_url_ar("https://lib.eshia.ir/71585/1/2")
    , sort_key = "اشباه والنظاير للسيوطي"
    ))
  resource_list.append(BibResource(
    "suyooti_hama3"
    , cit_type = "ar_ref"
    , cit_text = "[الهمع للسيوطي]{.ar}"
    , bib_text = """
      الكتاب: همع الهوامع في شرح جمع الجوامع  
      المؤلف: عبد الرحمن بن أبي بكر، جلال الدين السيوطي (ت ٩١١هـ)  
      المحقق: عبد الحميد هنداوي  
      الناشر: المكتبة التوفيقية - مصر  
      عدد الأجزاء: ٣  
      """ + format_url_ar("https://shamela.ws/book/6975")
    , sort_key = "همع الهوامع في شرح جمع الجوامع للسيوطي"
    ))
  resource_list.append(BibResource(
    "baseet_ibn_abi_rabee3"
    , cit_type = "ar_ref"
    , cit_text = "[البسيط لابن أبي الربيع]{.ar}"
    , bib_text = """
      البسيط في شرح جُمَل الزجاجي
      ابن أبي الربيع
      """ + format_url_ar("https://archive.org/details/0969pdf_201912/")
    , sort_key = "البسيط لابن ابي الربيع"
    ))
  resource_list.append(BibResource(
    "su3ood_dameer_mustatir"
    , cit_type = "ar_ref"
    , cit_text = "[الضمير المستتر لسعود بن عبيد الله الصاعدي]{.ar}"
    , bib_text = """
      الكتاب: الضمير المستتر في الدرس النحوي  
      المؤلف: سعود بن عبيد الله بن عابد الصاعدي  
      رسالة دكتوراة  
      جامعة أم القرى  
      ١٤٣٠ هـ - ٢٠٠٩ م
      """
    , sort_key = "ضمير المستتر لسعود بن عبيد الله الصاعدي"
    ))

  resource_list.append(BibResource(
    "ibn_malik_sharh_tasheel"
    , cit_type = "ar_ref"
    , cit_text = "[شرح التسهيل لابن مالك]{.ar}"
    , bib_text = """
      الكتاب: شرح تسهيل الفوائد  
      المؤلف: محمد بن عبد الله، ابن مالك الطائي الجياني، أبو عبد الله، جمال الدين (ت ٦٧٢ هـ)  
      المحقق: د. عبد الرحمن السيد - د. محمد بدوي المختون  
      الناشر: هجر للطباعة والنشر والتوزيع والإعلان  
      الطبعة: الأولى (١٤١٠ هـ - ١٩٩٠ م)  
      عدد الأجزاء: ٤  
      """ + format_url_ar("https://shamela.ws/book/13257")
    , sort_key = "شرح التسهيل لابن مالك"
    ))
  resource_list.append(BibResource(
    "ibn_aqil_musaa3id"
    , cit_type = "ar_ref"
    , cit_text = "[المساعد على تسهيل الفوائد لابن عقيل]{.ar}"
    , bib_text = """
      الكتاب: المساعد على تسهيل الفوائد  
      المؤلف: بهاء الدين بن عقيل  
      المحقق: د. محمد كامل بركات  
      الناشر: جامعة أم القرى (دار الفكر، دمشق - دار المدني، جدة)  
      الطبعة: الأولى، (١٤٠٠ - ١٤٠٥ هـ)  
      عدد الأجزاء: ٤  
      """ + format_url_ar("https://shamela.ws/book/133358")
    , sort_key = "مساعد على تسهيل الفوايد لابن عقيل"
    ))
  resource_list.append(BibResource(
    "sibawayhi"
    , cit_type = "ar_ref"
    , cit_text = "[الكتاب لسيبويه]{.ar}"
    , bib_text = """
      الكتاب: الكتاب  
      المؤلف: عمرو بن عثمان بن قنبر الحارثي بالولاء، أبو بشر، الملقب سيبويه (ت ١٨٠هـ)  
      المحقق: عبد السلام محمد هارون  
      الناشر: مكتبة الخانجي، القاهرة  
      الطبعة: الثالثة، ١٤٠٨ هـ - ١٩٨٨ م  
      عدد الأجزاء: ٤  
      """ + format_url_ar("https://shamela.ws/book/23018")
    , sort_key = "كتاب سيبويه"
    ))
  resource_list.append(BibResource(
    "sirafi_sibawayhi"
    , cit_type = "ar_ref"
    , cit_text = "[شرح كتاب سيبويه للسيرافي]{.ar}"
    , bib_text = """
      الكتاب: شرح كتاب سيبويه  
      المؤلف: أبو سعيد السيرافي الحسن بن عبد الله بن المرزبان (ت ٣٦٨ هـ)  
      المحقق: أحمد حسن مهدلي، علي سيد علي  
      الناشر: دار الكتب العلمية، بيروت - لبنان  
      الطبعة: الأولى، ٢٠٠٨ م  
      عدد الأجزاء: ٥  
      """ + format_url_ar("https://shamela.ws/book/17726")
    , sort_key = "شرح كتاب سيبويه للسيرافي"
    ))
  resource_list.append(BibResource(
    "azhari_sharh_tasreeh"
    , cit_type = "ar_ref"
    , cit_text = "[شرح التصريح على التوضيح]{.ar}"
    , bib_text = """
      الكتاب: شرح التصريح على التوضيح أو التصريح بمضمون التوضيح في النحو  
      المؤلف: خالد بن عبد الله بن أبي بكر بن محمد الجرجاويّ الأزهري، زين الدين المصري، وكان يعرف بالوقاد (ت ٩٠٥هـ)  
      الناشر: دار الكتب العلمية -بيروت-لبنان  
      الطبعة: الأولى ١٤٢١هـ- ٢٠٠٠م  
      عدد الأجزاء: ٢  
      """ + format_url_ar("https://shamela.ws/book/9985")
    , sort_key = "شرح التصريح على التوضيح"
    ))
  resource_list.append(BibResource(
    "shatibi_sharf_alfiyyah"
    , cit_type = "ar_ref"
    , cit_text = "[شرح ألفية ابن مالك للشاطبي]{.ar}"
    , bib_text = """
      الكتاب: المقاصد الشافية في شرح الخلاصة الكافية (شرح ألفية ابن مالك)  
      المؤلف: أبو إسحق إبراهيم بن موسى الشاطبي (المتوفى ٧٩٠ هـ)  
      الناشر: معهد البحوث العلمية وإحياء التراث الإسلامي بجامعة أم القرى - مكة المكرمة  
      الطبعة: الأولى، ١٤٢٨ هـ - ٢٠٠٧ م.  
      عدد الأجزاء: ١٠ (الأخير فهارس)  
      """ + format_url_ar("https://shamela.ws/book/20562")
    , sort_key = "شرح الفية ابن مالك للشاطبي"
    ))
  resource_list.append(BibResource(
    "sharh_shudhoor_aldhahab"
    , cit_type = "ar_ref"
    , cit_text = "[شرح شذور الذهب للجوجري]{.ar}"
    , bib_text = """
      الكتاب: شرح شذور الذهب في معرفة كلام العرب  
      المؤلف: شمس الدين محمد بن عبد المنعم بن محمد الجَوجَري القاهري الشافعي (ت ٨٨٩ هـ)  
      المحقق: نواف بن جزاء الحارثي  
      أصل التحقيق: رسالة ماجستير للمحقق  
      الناشر: عمادة البحث العلمي بالجامعة الإسلامية، المدينة المنورة، المملكة العربية السعودية  
      الطبعة: الأولى، ١٤٢٣ هـ/٢٠٠٤ م  
      عدد الأجزاء: ٢  
      """ + format_url_ar("https://shamela.ws/book/9134")
    , sort_key = "شرح شذور الذهب للجوجري"
    ))
  resource_list.append(BibResource(
    "sharh_ibn_naazim_alfiyyah"
    , cit_type = "ar_ref"
    , cit_text = "[شرح ابن الناظم على ألفية ابن مالك]{.ar}"
    , bib_text = """
      الكتاب: شرح ابن الناظم على ألفية ابن مالك  
      المؤلف: بدر الدين محمد ابن الإمام جمال الدين محمد بن مالك (ت ٦٨٦ هـ)  
      المحقق: محمد باسل عيون السود  
      الناشر: دار الكتب العلمية  
      الطبعة: الأولى، ١٤٢٠ هـ - ٢٠٠٠ م  
      عدد الصفحات: ٦٢١  
      """ + format_url_ar("https://shamela.ws/book/18115")
    , sort_key = "شرح ابن الناظم على الفية ابن مالك"
    ))
  resource_list.append(BibResource(
    "sharh_qatr_alnada"
    , cit_type = "ar_ref"
    , cit_text = "[شرح قطر الندى وبل الصدى]{.ar}"
    , bib_text = """
      الكتاب: شرح قطر الندى وبل الصدى
      المؤلف: أبو محمد، عبد الله، جمال الدين بن هشام الأنصاري (ت ٧٦١ هـ)
      المحقق: محمد محيى الدين عبد الحميد [ت ١٣٩٢ هـ]
      الطبعة: الحادية عشرة للمحقق ١٣٨٣ هـ- ١٩٦٣ م تمتاز بدقة الضبط والزيادة في الشروح والتحقيقات
      الناشر: المكتبة التجارية الكبرى بمصر
      طبع: مطبعة السعادة بمصر
      عدد الصفحات: ٣٣٥
      """ + format_url_ar("https://shamela.ws/book/6970")
    , sort_key = "شرح قطر الندى وبل الصدى"
    ))
  resource_list.append(BibResource(
    "ibn_malik_sharh_alkafiya"
    , cit_type = "ar_ref"
    , cit_text = "[شرح الكافية الشافية لابن مالك]{.ar}"
    , bib_text = """
      الكتاب: شرح الكافية الشافية  
      المؤلف: جمال الدين أبو عبد الله محمد بن عبد الله بن مالك الطائي الجياني  
      حققه وقدم له: عبد المنعم أحمد هريدي  
      الناشر: جامعة أم القرى مركز البحث العلمي وإحياء التراث الإسلامي كلية الشريعة والدراسات الإسلامية مكة المكرمة  
      الطبعة: الأولى، ١٤٠٢ هـ - ١٩٨٢ م  
      عدد الأجزاء: ٥ (متسلسلة الترقيم) (الأخير فهارس)  
      """ + format_url_ar("https://shamela.ws/book/12024")
    , sort_key = "شرح الكافية الشافية لابن مالك"
    ))
  resource_list.append(BibResource(
    "ibn_alanbaari_mudhakkar"
    , cit_type = "ar_ref"
    , cit_text = "[المذكر والمؤنث لابن الأنباري]{.ar}"
    , bib_text = """
      الكتاب: المذكر والمؤنث  
      المؤلف: أبو بكر، محمد بن القاسم بن محمد بن بشار بن الحسن بن بيان بن سماعة بن فَروة بن قَطَن بن دعامة الأنباري (ت ٣٢٨ هـ)  
      المحقق: محمد عبد الخالق عضيمة  
      مراجعة: د. رمضان عبد التواب  
      الناشر: جمهورية مصر العربية - وزارة الأوقاف - المجلس الأعلى للشؤون الإسلامية - لجنة إحياء التراث  
      سنة النشر: ١٤٠١ هـ - ١٩٨١ م  
      عدد الأجزاء: ٢  
      """ + format_url_ar("https://shamela.ws/book/17819")
    , sort_key = "مذكر والمونث لابن الانباري"
    ))
  resource_list.append(BibResource(
    "maghazi_waqidi"
    , cit_type = "corpus"
    , cit_text = "[مغازي الواقدي]{.ar}"
    , bib_text = """
      الكتاب: المغازي  
      المؤلف: محمد بن عمر بن واقد [الواقدي] (ت ٢٠٧ هـ)  
      تحقيق: د مارسدن جونس  
      الناشر: جامعة أكسفورد - لندن، ١٩٦٦ م  
      (وصورته دور نشر مثل دار الأعلمي، وعالم الكتب)  
      عدد الأجزاء: ٣ (متسلسلة الترقيم)  
      """ + format_url_ar("https://shamela.ws/book/23680")
    , sort_key = "مغازي الواقدي"
    ))
  resource_list.append(BibResource(
    "tarikh_tabari"
    , cit_type = "corpus"
    , cit_text = "[تاريخ الطبري]{.ar}"
    , bib_text = """
      الكتاب: تاريخ الطبري = تاريخ الرسل والملوك  
      المؤلف: أبو جعفر، محمد بن جرير الطبري (٢٢٤ - ٣١٠ هـ)  
      ويليه بالجزء ١١: «صلة تاريخ الطبري» لعريب بن سعد القرطبي [ت ٣٦٩ هـ]  
      ويليه: «تكملة تاريخ الطبري» لمحمد بن عبد الملك الهمذاني [ت ٥٢١ هـ]  
      ويليه: «المنتخب من كتاب ذيل المذيل من تاريخ الصحابة والتابعين لمحمد بن جرير الطبري» لأحد العلماء  
      المحقق: محمد أبو الفضل إبراهيم [ت ١٤٠١ هـ]  
      الناشر: دار المعارف بمصر  
      الطبعة: الثانية ١٣٨٧ هـ - ١٩٦٧ م  
      عدد الأجزاء: ١١  
      """ + format_url_ar("https://shamela.ws/book/9783")
    , sort_key = "تاريخ الطبري"
    ))
  resource_list.append(BibResource(
    "sharh_ashmooni"
    , cit_type = "ar_ref"
    , cit_text = "[شرح الأشمونى لألفية ابن مالك]{.ar}"
    , bib_text = """
      الكتاب: شرح الأشموني على ألفية ابن مالك  
      المؤلف: علي بن محمد بن عيسى، أبو الحسن، نور الدين الأُشْمُوني الشافعي (ت ٩٠٠هـ)  
      الناشر: دار الكتب العلمية بيروت- لبنان  
      الطبعة: الأولى ١٤١٩هـ- ١٩٩٨مـ  
      عدد الأجزاء: ٤  
      """ + format_url_ar("https://shamela.ws/book/11742")
    , sort_key = "شرح الاشمونى لافية ابن مالك"
    ))
  resource_list.append(BibResource(
    "aljani_aldani"
    , cit_type = "ar_ref"
    , cit_text = "[الجنى الداني]{.ar}"
    , bib_text = """
      الكتاب: الجنى الداني في حروف المعاني  
      المؤلف: أبو محمد بدر الدين حسن بن قاسم بن عبد الله بن عليّ المرادي المصري المالكي (ت ٧٤٩هـ)  
      المحقق: د فخر الدين قباوة -الأستاذ محمد نديم فاضل  
      الناشر: دار الكتب العلمية، بيروت - لبنان  
      الطبعة: الأولى، ١٤١٣ هـ - ١٩٩٢ م  
    """ + format_url_ar("https://shamela.ws/book/26099")
    , sort_key = "جنى الداني"
    ))
  resource_list.append(BibResource(
    "irtishaaf"
    , cit_type = "ar_ref"
    , cit_text = "[ارتشاف الضرب من لسان العرب]{.ar}"
    , bib_text = """
      الكتاب: ارتشاف الضرب من لسان العرب
      المؤلف: أبو حيان محمد بن يوسف بن علي بن يوسف بن حيان أثير الدين الأندلسي (ت ٧٤٥ هـ)
      تحقيق وشرح ودراسة: رجب عثمان محمد
      مراجعة: رمضان عبد التواب
      الناشر: مكتبة الخانجي بالقاهرة
      الطبعة: الأولى، ١٤١٨ هـ - ١٩٩٨ م
      عدد الأجزاء: ٥ (متسلسلة الترقيم)
    """ + format_url_ar("https://shamela.ws/book/16595")
    , sort_key = "ارتشاف الضرب من لسان العرب"
    ))
  resource_list.append(BibResource(
    "mu3allimi"
    , cit_type = "ar_ref"
    , cit_text = "[تحقيق الكلام في المسائل الثلاث ضمن آثار المعلمي]{.ar}"
    , bib_text = """
      الكتاب: تحقيق الكلام في المسائل الثلاث
      [آثار عبد الرحمن بن يحيى المعلمي اليماني (٤)]
      المؤلف: عبد الرحمن بن يحيى المُعَلِّمي اليماني (١٣١٣ - ١٣٨٦ هـ)
      المحقق: علي بن محمد العمران - محمد عزير شمس
      راجعه: عبد الرحمن بن صالح السُديس - سليمان بن عبد الله العُمير
      الناشر: دار عالم الفوائد للنشر والتوزيع
      الطبعة: الأولى، ١٤٣٤ هـ
      """ + format_url_ar("https://shamela.ws/book/328")
    , sort_key = "تحقيق الكلام في المسايل الثلاث ضمن اثار المعلمي"
    ))
  resource_list.append(BibResource(
    "utheymeen_alfiyyah"
    , cit_type = "ar_ref"
    , cit_text = "[شرح ألفية ابن مالك للعثيمين]{.ar}"
    , bib_text = """
      الكتاب: شرح ألفية ابن مالك  
      المؤلف: محمد بن صالح بن محمد العثيمين (ت ١٤٢١هـ)  
      مصدر الكتاب: دروس صوتية قام بتفريغها موقع الشبكة الإسلامية  
      http://www.islamweb.net  
      """ + format_url_ar("https://shamela.ws/book/36954")
    , sort_key = "شرح الفية ابن مالك للعثيمين"
    ))
  resource_list.append(BibResource(
    "afghani"
    , cit_type = "ar_ref"
    , cit_text = "[من تاريخ النحو العربي لسعيد الأفعاني]{.ar}"
    , bib_text = """
      الكتاب: من تاريخ النحو العربي  
      المؤلف: سعيد بن محمد بن أحمد الأفغاني (ت ١٤١٧هـ)  
      الناشر: مكتبة الفلاح  
      عدد الصفحات: ٢١٤  
      """ + format_url_ar("https://shamela.ws/book/9937")
    , sort_key = "من تاريخ النحو العربي لسعيد الافعاني"
    ))
  resource_list.append(BibResource(
    "haazimi"
    , cit_type = "ar_ref"
    , cit_text = "[شرح ألفية ابن مالك للحازمي]{.ar}"
    , bib_text = """
      الكتاب: شرح ألفية ابن مالك  
      المؤلف: أبو عبد الله، أحمد بن عمر بن مساعد الحازمي  
      """ + format_url_ar("https://shamela.ws/book/36130")
    , sort_key = "شرح الفية ابن مالك للحازمي"
    ))
  resource_list.append(BibResource(
    "hayyani_jam3_masdar"
    , cit_type = "ar_ref"
    , cit_text = "[جمع المصدر وأحكامه لحياني]{.ar}"
    , bib_text = """
      المقالة: جمع المصدر وأحكامه  
      المؤلف: عبد الله محمد عبد الله حياني  
      الناشر: مجلة العلوم العربية، العدد ٧٥، ١٤٤٦هـ، الجزء الثاني  
      """ + format_url_ar("https://imamjournals.org/index.php/jas/article/view/3160")
    , sort_key = "جمع المصدر واحكامه لحياني"
    ))
  resource_list.append(BibResource(
    "faaridi_alfiyyah"
    , cit_type = "ar_ref"
    , cit_text = "[شرح الفارضي على ألفية ابن مالك]{.ar}"
    , bib_text = """
      الكتاب: شرح الإمام الفارضي على ألفية ابن مالك  
      المؤلف: العلامة شمس الدين محمد الفارضي الحنبلي (ت ٩٨١ هـ)  
      المحقق: أبو الكميت، محمد مصطفى الخطيب  
      الناشر: دار الكتب العلمية، لبنان - بيروت  
      الطبعة: الأولى، ١٤٣٩ هـ - ٢٠١٨ م  
      عدد الأجزاء: ٤  
      """ + format_url_ar("https://shamela.ws/book/174")
    , sort_key = "شرح الفارضي على الفية ابن مالك"
    ))
  resource_list.append(BibResource(
    "qiyaas_amsha"
    , cit_type = "ar_ref"
    , cit_text = "[القياس النحو لخالد حسين أبو عمشة]{.ar}"
    , bib_text = """
      الكتاب: القياس النحو  
      المؤلف: لخالد حسين ابو عمشة  
      """ + format_url_ar("https://ketabonline.com/ar/books/97698")
    , sort_key = "القياس النحو لخالد حسين ابو عمشة"
    ))
  resource_list.append(BibResource(
    "qiyaas_husain"
    , cit_type = "ar_ref"
    , cit_text = "[القياس في اللغة العربية لحسين محمد الخضر]{.ar}"
    , bib_text = """
      الكتاب: القياس في اللغة العربية  
      المؤلف: حسين محمد الخضر  
      الناشر: المطبعة السلفية، القاهرة  
      الطبعة: ١٣٥٣ هـ - ١٩٣٥ م  
      """
    , sort_key = "القياس في اللغة العربية لحسين محمد الخضر"
    ))

  # Western

  resource_list.append(BibResource(
    "wright"
    , cit_type = "ws_ref"
    , cit_text = "Wright"
    , bib_text = "Wright,\\ W., _A grammar of the Arabic language_, 3rd ed., Cambridge University Press, 1896--1898. <https://archive.org/details/AGrammarOfTheArabicLanguageV1>"
    ))
  
  resource_list.append(BibResource(
    "fischer"
    , cit_type = "ws_ref"
    , cit_text = "Fischer"
    , bib_text = "Fischer,\\ W., _A grammar of Classical Arabic_, 3rd rev. ed., translated by J.\\ Rodgers, Yale University Press, 2001."
    ))

  resource_list.append(BibResource(
    "sadan_subj"
    , cit_type = "ws_ref"
    , cit_text = "Sadan,\\ A., _The subjunctive mood in Arabic grammatical thought_"
    , bib_text = "Sadan,\\ A., _The subjunctive mood in Arabic grammatical thought_, Brill, 2012. <https://doi.org/10.1163/9789004234239>"
    , sort_key = "Sadan A Subjunctive Mood in Arabic Grammatical Thought"
    ))

  resource_list.append(BibResource(
    "jallad_wawation"
    , cit_type = "ws_ref"
    , cit_text = 'Al-Jallad,\\ A., "One wāw to rule them all: The origins and fate of wawation in Arabic and its orthography"'
    , bib_text = 'Al-Jallad,\\ A., "One wāw to rule them all: The origins and fate of wawation in Arabic and its orthography," in: _Scripts and scripture: Writing and religion in Arabia circa 500--700\\ [ce]{.smallcaps}_, pp.\\ 87--104. The Oriental Institute of the University of Chicago, 2022. <https://www.academia.edu/33017695>'
    , sort_key = "Jallad A One waw to rule them all"
    ))

  resource_list.append(BibResource(
    "hallberg_thesis"
    , cit_type = "ws_ref"
    , cit_text = 'Hallberg,\\ A., _Case endings in Spoken Standard Arabic_'
    , bib_text = 'Hallberg,\\ A., _Case endings in Spoken Standard Arabic_. Doctoral thesis, Lund University, 2016. <https://lup.lub.lu.se/record/8524489>'
    , sort_key = "Hallberg A Case endings in Spoken Standard Arabic"
    ))

  resource_list.append(BibResource(
    "cantarino_smap"
    , cit_type = "ws_ref"
    , cit_text = 'Cantarino,\\ V., _Syntax of modern Arabic prose_'
    , bib_text = 'Cantarino,\\ V., _Syntax of modern Arabic prose_, Indiana University Press, 1974--1975.'
    , sort_key = 'Cantarino V Syntax of modern Arabic prose'
    ))

  #resource_list.append(BibResource(
  #  "brock_grund"
    #, cit_type = "ws_ref"
  #  , cit_text = 'Brockelmann,\\ C., _Grundriss der vergleichenden Grammatik der semitischen Sprachen_'
  #  , bib_text = 'Brockelmann,\\ C., _Grundriss der vergleichenden Grammatik der semitischen Sprachen_, Verlag von Reuther & Reichard, 1908--1913.'
  #  , sort_key = 'Brockelmann C Grundriss der vergleichenden Grammatik der semitischen Sprachen'
  #  ))

  resource_list.append(BibResource(
    "liheibi_sentence"
    , cit_type = "ws_ref"
    , cit_text = 'Al-Liheibi,\\ F.\\ M.\\ M.\\, _Aspects of sentence analysis in the Arabic linguistic tradition_'
    , bib_text = 'Al-Liheibi,\\ F.\\ M.\\ M.\\, _Aspects of sentence analysis in the Arabic linguistic tradition, with particular reference to ellipsis_, Doctoral dissertation, Durham University, 1999. <https://etheses.dur.ac.uk/1494/>'
    , sort_key = 'Liheibi F M M Aspects of sentence analysis in the Arabic linguistic tradition'
    ))

  resource_list.append(BibResource(
    "owens_foundations_grammar"
    , cit_type = "ws_ref"
    , cit_text = 'Owens,\\ J., _The foundations of grammar_'
    , bib_text = 'Owens,\\ J., _The foundations of grammar: An introduction to medieval Arabic grammatical theory_, John Benjamins Publishing, 1988.'
    , sort_key = 'Owens J The foundations of grammar'
    ))

  resource_list.append(BibResource(
    "kasher_intransitive_verb"
    , cit_type = "ws_ref"
    , cit_text = 'Kasher,\\ A., "The term _al-fiʿl al-mutaʿaddī bi-ḥarf jarr_"'
    , bib_text = 'Kasher,\\ A., "The term _al-fiʿl al-mutaʿaddī bi-ḥarf jarr_ (lit. “the verb which ‘passes over’ through a preposition”) in medieval Arabic grammatical tradition", in _Journal of Arabic and Islamic Studies_, 13, pp. 115--145, 2013. <https://doi.org/10.5617/jais.4630>'
    , sort_key = 'Kasher A The term alfil almutaaddi biharf jarr'
    ))

  resource_list.append(BibResource(
    "peled_sentence_types"
    , cit_type = "ws_ref"
    , cit_text = 'Peled, _Sentence types_'
    , bib_text = 'Peled,\\ Y., _Sentence types and word-order patterns in written Arabic: Medieval and modern perspectives_, Brill, 2008. <https://doi.org/10.1163/ej.9789004170629.i-250>'
    , sort_key = 'Peled Y Sentence types and word order patterns in written Arabic'
    ))

  resource_list.append(BibResource(
    "marmor_tense"
    , cit_type = "ws_ref"
    , cit_text = 'Marmorstein,\\ M., _Tense and text in Classical Arabic_'
    , bib_text = 'Marmorstein,\\ M., _Tense and text in Classical Arabic_, Brill, 2016. <https://doi.org/10.1163/9789004310483>'
    , sort_key = 'marmorstein m tense and text in classical arabic'
    ))
  resource_list.append(BibResource(
    "odilavadze_participle"
    , cit_type = "ws_ref"
    , cit_text = """Odilavadze, N., _Western scholars' opinions on rendering the tense by means of the participle in Arabic_"""
    , bib_text = """Odilavadze, N., "Western scholars' opinions on rendering the tense by means of the participle in Arabic", _IBSU Scientific Journal_ 2010, 4(1), 63-80. <https://journal.ibsu.edu.ge/index.php/ibsusj/article/download/143/120/0>"""
    , sort_key = 'odilavadze n western scholars opinions on rendering the tense by means of the participle in arabic'
    ))
  resource_list.append(BibResource(
    "putten_participles"
    , cit_type = "ws_ref"
    , cit_text = 'van Putten, M., _The morphosyntax of objects to participles in the Qurʾān_'
    , bib_text = 'van Putten, M., "The morphosyntax of objects to participles in the Qurʾān," _Journal of Semitic Studies LXIX/1 Spring 2024_ <https://doi.org/10.1093/jss/fgad029>'
    , sort_key = 'van putten m the morphosyntax of objects to participles in the quran'
    ))
  resource_list.append(BibResource(
    "kinberg_participal"
    , cit_type = "ws_ref"
    , cit_text = 'Kinberg, N., _Semi-imperfectives and imperfectives: A case study of aspect and tense in Arabic participal clauses_'
    , bib_text = 'Kinberg, N., "Semi-imperfectives and imperfectives: A case study of aspect and tense in Arabic participal clauses," _Lingua 86_ (1992) pp.\\ 301--330'
    , sort_key = 'kinberg n semiimperfectives and imperfectives a case study of aspect and tense in arabic participal clauses'
    ))
  resource_list.append(BibResource(
    "waltisberg_satzkomplex"
    , cit_type = "ws_ref"
    , cit_text = 'Waltisberg, M., _Satzkomplex und funktion_'
    , bib_text = 'Waltisberg, M., _Satzkomplex und funktion: Syndese und asyndese im Althocharabischen_, Harrassowitz Verlag, 2009. <https://doi.org/10.2307/j.ctvbnm2b2>'
    , sort_key = 'waltisberg m satzkomplex und funktion'
    ))
  resource_list.append(BibResource(
    "owens_participle"
    , cit_type = "ws_ref"
    , cit_text = 'Owens, J., and M. Yavrumyan,  _The participle_'
    , bib_text = 'Owens, J., and M. Yavrumyan,  "The participle" in _Encyclopedia of Arabic language and linguistics_, (2007) pp.\\ 541-46, Brill.'
    , sort_key = 'owens j and m yavrumyan the participle'
    ))
  resource_list.append(BibResource(
    "youssef_partizip"
    , cit_type = "ws_ref"
    , cit_text = 'Youssef, Z., _Das partizip im Arabischen_'
    , bib_text = 'Youssef, Z., _Das partizip im Arabischen_, Ph.D. diss., University Erlangen-Nürnberg, 1990.'
    , sort_key = 'youssef z das partizip im arabischen'
    ))
  resource_list.append(BibResource(
    "lane"
    , cit_type = "ws_ref"
    , cit_text = "Lane's Lexicon"
    , bib_text = 'Lane, E.\\ W., _An Arabic-English Lexicon_, <https://ejtaal.net/aa>'
    , sort_key = 'lanes lexicon'
    ))
  resource_list.append(BibResource(
    "zarabozo_approach"
    , cit_type = "ws_ref"
    , cit_text = "Zarabozo, _How to approach and understand the Quran_"
    , bib_text = "Zarabozo, J. M., _How to approach and understand the Quran_, Al-Basheer Company, 1999."
    , sort_key = 'zarabozo how to approach'
    ))
  resource_list.append(BibResource(
    "ibn_kathir_english"
    , cit_type = "ws_ref"
    , cit_text = "Al-Mubarakpuri, _Tafsir ibn Kathir_ (abridged, English translation), Darussalam, 2nd edition, 2003"
    , bib_text = "Al-Mubarakpuri, _Tafsir ibn Kathir_ (abridged, English translation), Darussalam, 2nd edition, 2003"
    , sort_key = 'tafsir ibn kathir english'
    ))
  resource_list.append(BibResource(
    "baalbaki_intro"
    , cit_type = "ws_ref"
    , cit_text = "Baalbaki, Introduction to _The early Islamic grammatical tradition_"
    , bib_text = "Baalbaki, R., Introduction to _The early Islamic grammatical tradition_, Routledge, 2016."
    , sort_key = 'baalbaki introduction early islamic grammatical tradition'
    ))
  resource_list.append(BibResource(
    "suleiman_ta3leel"
    , cit_type = "ws_ref"
    , cit_text = "Suleiman, _The Arabic Grammatical Tradition: A study in ta‘līl_"
    , bib_text = "Suleiman, Y., _The Arabic Grammatical Tradition: A study in ta‘līl_. Edinburgh University Press, 1999."
    , sort_key = "suleiman arabic grammatical tradition A study in talil"
    ))



  return resource_list

