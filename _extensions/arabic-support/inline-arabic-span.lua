local ar_span = require("ar_span")

function Span (el)
  if el.classes:includes 'ar' or el.classes:includes 'aralt' then
    return ar_span.ArabicSpan(el)
  end
end

