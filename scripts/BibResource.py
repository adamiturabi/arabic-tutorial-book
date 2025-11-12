class BibResource:

  alphabet = "ابتثجحخدذرزسشصضطظعغفقكلمنهةويىabcdefghijklmnopqrstuvwxyz"

  def __init__(self, cit_key, cit_type, cit_text, bib_text=None, sort_key=None):
    if bib_text is None:
      bib_text = cit_text
    if sort_key is None:
      sort_key = cit_text

    assert(cit_type in ["corpus", "ar_ref", "ws_ref"])

    self.cit_key = cit_key
    self.cit_type = cit_type
    self.cit_text = cit_text
    self.bib_text = bib_text
    self.sort_key = self.sanitize_sort_key(sort_key)
    # TODO check that sort_key contains only alphabet

  def sanitize_sort_key(self, s):
    # remove whitespace
    s = "".join(s.split())

    # remove .ar span if enclosed by it
    if s[0] == '[' and len(s) >= 8 and s[-6:] == ']{.ar}':
      s = s[1:-6]

    # make lowercase
    s = s.lower()

    # normalize arabic characters to their canonical basic letter
    import unicodedata
    s = unicodedata.normalize('NFD',s)

    # remove characters not in alphabet
    #f = filter(lambda x: x in self.alphabet, s)

    return s

  def __eq__(self, other):
    return self.cit_key == other.cit_key

  def __lt__(self, other):
    tmp_list = [self.sort_key, other.sort_key]
    out_list = sorted(tmp_list, key=lambda word: [self.alphabet.index(c) for c in word])
    return out_list[0] == tmp_list[0]


