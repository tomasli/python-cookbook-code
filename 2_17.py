s = 'Elements are written ad "<tag>text</tag>".'
import html
print(s)
print(html.escape(s))

# Disable excaping of quotes
print(html.escape(s, quote=False))
