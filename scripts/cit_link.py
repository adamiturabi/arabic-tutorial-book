from surah_names import surah_names

def get_quran_cit_text(end_str, link):
  # remove begin slash
  assert(end_str[0] == '/')
  end_str = end_str[1:]

  # remove end slash if any
  if end_str[-1] == '/':
    end_str = end_str[:-1]

  # try splitting with slash
  surah_and_ayah = end_str.split('/')

  if len(surah_and_ayah) == 1:
    # try splitting with colon
    surah_and_ayah = end_str.split(':')

  #print("surah_and_ayah= ", surah_and_ayah)

  surah_index_str = surah_and_ayah[0]
  cit_text = "[سورة "
  cit_text += surah_names[int(surah_index_str) - 1] # python index starts from zero
  cit_text += "]{.ar}"

  # if still not split then it is whole surah
  if len(surah_and_ayah) > 1:
    ayah_index_str = surah_and_ayah[1]
    cit_text += ' ' + surah_index_str + ':' + ayah_index_str

  return "quran", "[" + cit_text + "](" + link + ")", True

def get_tafsir_app_key_and_cit_text(end_str, link):
  # remove begin slash
  assert(end_str[0] == '/')
  end_str = end_str[1:]

  ret_surah_and_ayah = True

  # remove end slash if any, but use it to determine whether to append surah and ayah
  if end_str[-1] == '/':
    end_str = end_str[:-1]
    ret_surah_and_ayah = False

  # try splitting with slash
  book_and_surah_and_ayah = end_str.split('/')

  #if len(surah_and_ayah) == 1:
  #  # try splitting with colon
  #  surah_and_ayah = end_str.split(':')

  #print("surah_and_ayah= ", surah_and_ayah)

  assert(len(book_and_surah_and_ayah) == 3)
  book_str = book_and_surah_and_ayah[0]
  surah_index_str = book_and_surah_and_ayah[1]
  ayah_index_str = book_and_surah_and_ayah[2]

  key = book_str
  cit_text = ''

  if ret_surah_and_ayah:
    cit_text = " for [سورة "
    cit_text += surah_names[int(surah_index_str) - 1] # python index starts from zero
    cit_text += "]{.ar}"

    cit_text += ' ' + surah_index_str + ':' + ayah_index_str

  return key, cit_text, False

def get_sunnah_com_key_and_cit_text(end_str, link):
  # remove begin slash
  assert(end_str[0] == '/')
  end_str = end_str[1:]

  # remove end slash if any
  if end_str[-1] == '/':
    end_str = end_str[:-1]

  # try splitting with slash
  book_and_hadithnum = end_str.split('/')

  if len(book_and_hadithnum) == 1:
    # try splitting with colon
    book_and_hadithnum = end_str.split(':')

  #print("book_and_hadithnum= ", book_and_hadithnum)

  book_str = book_and_hadithnum[0]
  key = book_str
  cit_text = ''

  # if still not split then it is whole book
  if len(book_and_hadithnum) > 1:
    hadith_index_str = book_and_hadithnum[1]
    cit_text += ' :' + hadith_index_str

  return key, cit_text, False


def process(key, link):
  quran_com_url = 'https://quran.com'
  sunnah_com_url = 'https://sunnah.com'
  tafsir_app_url = 'https://tafsir.app'

  new_key = None
  cit_text = ''
  link_added = False
  if quran_com_url in key:
    end_str = key.split(quran_com_url)
    assert len(end_str) == 2
    if end_str[1] == '' or end_str[1] == '/':
      return None, '<' + key + '>', True
    new_key, cit_text, link_added = get_quran_cit_text(end_str[1], link)
  elif sunnah_com_url in key:
    end_str = key.split(sunnah_com_url)
    assert len(end_str) == 2
    if end_str[1] == '' or end_str[1] == '/':
      return None, '<' + key + '>', True
    new_key, cit_text, link_added = get_sunnah_com_key_and_cit_text(end_str[1], link)
  elif tafsir_app_url in key:
    end_str = key.split(tafsir_app_url)
    assert len(end_str) == 2
    if end_str[1] == '' or end_str[1] == '/':
      return None, '<' + key + '>', True
    new_key, cit_text, link_added = get_tafsir_app_key_and_cit_text(end_str[1], link)

  return new_key, cit_text, link_added

