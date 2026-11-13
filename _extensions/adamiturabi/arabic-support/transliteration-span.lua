--function Span (el)
--  if el.classes:includes 'trn' then
--    input_text = pandoc.utils.stringify(el)
--    output_text = RomanizeMapping(input_text, true)
--    contents = {pandoc.Str(output_text)}
--    return pandoc.Span(contents, {class='trnital'})
--  end
--end

local romanize = require("romanize")

function Span (el)
  if el.classes:includes 'trn' 
  or el.classes:includes 'trn2' then
    input_text = pandoc.utils.stringify(el)
    output_text = romanize.RomanizeMapping(input_text, true)
    contents = {pandoc.Str(output_text)}
    if el.classes:includes 'trn' then
      contents = pandoc.Span(pandoc.Emph(contents), {class='trn'})
    end
    return pandoc.Span(contents, {class='trn2'})
  end
end

