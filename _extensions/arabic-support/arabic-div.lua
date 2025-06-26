-- Add attributes for Arabic text in a div
function ArabicDiv (el)
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
      classval = 'reg-ar-div'
      if el.classes:includes 'aralt' then
        classval = 'alt-ar-div'
      end
      -- dir needed for html otherwise punctuation gets messed up
      return pandoc.Div(contents, {class=classval, lang='ar', dir='rtl'})
    end
end
ex_counter = 1

function LingEx (el)
    ex_counter_str = tostring(ex_counter)
    crossref = "#lingex-" .. ex_counter_str
    ex_counter = ex_counter + 1

    table.insert(
      el.content, 1,
      pandoc.Div("(" .. ex_counter_str .. ")", {crossref .. "-num"}))
    table.insert(
      el.content, 
      pandoc.Div("ref", {crossref .. "-ref"}))

    return pandoc.Div(el.content, {layout='[0.1, 0.6, -0.1, 0.2]'})
end

function Div (el)
  if el.classes:includes 'ar' or el.classes:includes 'aralt' then
    return ArabicDiv(el)
  elseif el.classes:includes 'lingex' then
    return LingEx(el)
  end
end
