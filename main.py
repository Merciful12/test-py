import requests
import os
import sys

r = requests.get('http://worldclockapi.com/api/json/est/now')
print(r.text)

with open('index.html', 'w+') as f:
  f.write('<h1>' + sys.argv[1] + '</h1>')

