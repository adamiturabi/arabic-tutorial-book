function Strong(el)
  -- Check if the output format is HTML
  if FORMAT:match('html') then
    -- Return a Span element with inline CSS for color
    return pandoc.Span(el.content, {style = "color: #9b111e;"})
  elseif FORMAT:match('latex') then
    ---- Inject \textcolor{red}{ at the beginning of the bold element's content
    --table.insert(el.content, 1, pandoc.RawInline('latex', '\\textcolor{red}{'))
    ---- Close the bracket at the end
    --table.insert(el.content, pandoc.RawInline('latex', '}'))
    --return el
    -- Insert LaTeX raw inlines before and after the text content to change color
    local result = {
      pandoc.RawInline('latex', '\\textcolor[HTML]{9B111E}{'),
    }

    -- Append the inner text elements (stripping the 'Strong' wrapper removes bold)
    for _, inline in ipairs(el.content) do
      table.insert(result, inline)
    end

    table.insert(result, pandoc.RawInline('latex', '}'))

    return result
  end
  -- For other formats (like PDF/Word), leave it unchanged
  return el
end

