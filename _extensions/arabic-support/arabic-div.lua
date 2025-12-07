-- Add attributes for Arabic text in a div
Div = function(el)
  if el.classes:includes 'ar' or el.classes:includes 'aralt' or el.classes:includes 'quran' then
    contents = el.content
    if FORMAT:match 'latex' then
      -- for handling alternate Arabic font
      if el.classes:includes 'aralt' then
        -- can't seem to use string concatenate directly. Have to use RawInline
        table.insert(
          contents, 1,
          pandoc.RawInline('latex', '\\altfamily ')
        )
      elseif el.classes:includes 'aralt' then
        table.insert(
          contents, 1,
          pandoc.RawInline('latex', '\\quranfamily ')
        )
      end
      -- no dir needed for babel and throws error if it sees dir attribute. was previously needed for polyglossia
      -- The underscore in data_latex is automatically converted to a hyphen
      return pandoc.Div(contents, {class='otherlanguage', data_latex="{arabic}", lang='ar'})
    elseif FORMAT:match 'html' then
      classval = 'reg-ar-div'
      if el.classes:includes 'aralt' then
        classval = 'alt-ar-div'
      elseif el.classes:includes 'quran' then
        classval = 'quran-ar-div'
      end
      -- dir needed for html otherwise punctuation gets messed up
      return pandoc.Div(contents, {class=classval, lang='ar', dir='rtl'})
    end
  end
end

