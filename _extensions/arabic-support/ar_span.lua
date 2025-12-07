-- Add attributes for Arabic text in a span
local ar_span = {}

function ar_span.ArabicSpan(el)
    --text = pandoc.utils.stringify(el)
    --contents = {pandoc.Str(text)}
    contents = el.content
    if FORMAT:match 'latex' then
      -- for handling alternate Arabic font
      if el.classes:includes 'aralt' then
        -- can't seem to use string concatenate directly. Have to use RawInline
        table.insert(
          contents, 1,
          pandoc.RawInline('latex', '\\altfamily ')
        )
      elseif el.classes:includes 'quran' then
        -- can't seem to use string concatenate directly. Have to use RawInline
        table.insert(
          contents, 1,
          pandoc.RawInline('latex', '\\quranfamily ')
        )
 
      end
      -- no dir needed for babel and throws error if it sees dir attribute. was previously needed for polyglossia
      return pandoc.Span(contents, {lang='ar'})
    elseif FORMAT:match 'html' then
      classval = 'reg-ar-span'
      if el.classes:includes 'aralt' then
        classval = 'alt-ar-span'
      elseif el.classes:includes 'quran' then
        classval = 'quran-ar-span'
      end
      -- dir needed for html otherwise punctuation gets messed up
      return pandoc.Span(contents, {class=classval, lang='ar', dir='rtl'})
    end
end

return ar_span

