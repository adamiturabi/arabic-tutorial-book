-- Add attributes for Arabic text in a div
function Div (el)
  if el.classes:includes 'ar' or el.classes:includes 'aralt' then
    contents = el.content
    if FORMAT:match 'latex' then
      -- for handling alternate Arabic font
      if el.classes:includes 'aralt' then
        -- can't seem to use string concatenate directly. Have to use RawInline
        table.insert(
          contents, 1,
          pandoc.RawInline('latex', '\\altfamily ')
        )
      end
      -- no dir needed for babel and throws error if it sees dir attribute. was previously needed for polyglossia
      -- The underscore in data_latex is automatically converted to a hyphen
      return pandoc.Div(contents, {class='otherlanguage', data_latex="{arabic}", lang='ar'})
    elseif FORMAT:match 'html' then
      classval = 'reg-ar-text'
      if el.classes:includes 'aralt' then
        classval = 'alt-ar-text'
      end
      -- dir needed for html otherwise punctuation gets messed up
      return pandoc.Div(contents, {class=classval, lang='ar', dir='rtl'})
    end
  end
end

