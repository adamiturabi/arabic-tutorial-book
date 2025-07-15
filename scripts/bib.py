from BibResource import BibResource

def populate_resource_list():
  resource_list = []

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
    , bib_text = "[شرح الكافية في النحو، تأليف: رضي الدين محمد بن الحسن الاستراباذي (ت: 686\\ هـ).]{.ar}"
    , sort_key = "شرح الرضي على الكافية"
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
