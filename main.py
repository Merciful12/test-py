from html import HTML
import os

h = HTML()
h.p(sys.argv[1])

with open('index.html', 'w+') as f:
  f.write(h)

