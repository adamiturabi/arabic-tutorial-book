from surah_names import surah_names

def get_quran_cit_text(end_str):
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
  cit_text = "سورة "
  cit_text += surah_names[int(surah_index_str) - 1] # python index starts from zero

  # if still not split then it is whole surah
  if len(surah_and_ayah) > 1:
    ayah_index_str = surah_and_ayah[1]
    cit_text += ' ' + surah_index_str + ':' + ayah_index_str

  return cit_text

def get_sunnah_com_key_and_cit_text(end_str):
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

  return key, cit_text


def process(key):
  quran_com_url = 'https://quran.com'
  sunnah_com_url = 'https://sunnah.com'
  tafsir_app_url = 'https://tafsir.app'

  new_key = None
  if quran_com_url in key:
    end_str = key.split(quran_com_url)
    assert len(end_str) == 2
    if end_str[1] == '' or end_str[1] == '/':
      return None, '<' + key + '>'
    cit_text = get_quran_cit_text(end_str[1])
  elif sunnah_com_url in key:
    end_str = key.split(sunnah_com_url)
    assert len(end_str) == 2
    if end_str[1] == '' or end_str[1] == '/':
      return None, '<' + key + '>'
    new_key, cit_text = get_sunnah_com_key_and_cit_text(end_str[1])
  elif tafsir_app_url in key:
    new_key = tafsir_app_key

  return new_key, cit_text

