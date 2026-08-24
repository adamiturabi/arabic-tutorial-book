-- Reset numbered example list counter for every chapter for PDF

-- Tracks the current example number
local example_counter = 1

-- intercept headers to check for manual resets or specific levels
function Header(el)
    -- Reset on Header level 1 (e.g., # New Chapter)
    if el.level == 1 then
        example_counter = 1
    end
    
    -- Also check for a custom attribute like: # Header { .reset-examples }
    if el.classes:includes('reset-examples') then
        example_counter = 1
    end
    
    return el
end

-- Intercept custom Div containers
function OrderedList(ol)
    if ol.style == "Example" then -- don't modify sub-lists. those will be alpha or roman
      -- Modify the ordered list here
      if FORMAT:match 'latex' then
        ol.start = example_counter
        print("count=", example_counter)
      end

      -- Increment our internal tracking counter
      example_counter = example_counter + 1
    end
    return ol
end

