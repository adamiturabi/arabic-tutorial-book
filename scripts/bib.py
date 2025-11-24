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
      الكتاب: الأشباه والنظائر في قواعد وفروع فقه الشافعية
      المؤلف: جلال الدين عبد الرحمن السيوطي (ت ٩١١ هـ)
      الناشر: دار الكتب العلمية
      الطبعة: الأولى، ١٤٠٣ هـ - ١٩٨٣ م
      """ + format_url_ar("https://archive.org/details/ashbhnzer1/ashbhnzer0/")
    , sort_key = "اشباه والنظاير للسيوطي"
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
  return resource_list

