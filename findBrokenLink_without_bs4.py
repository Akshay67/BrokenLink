import requests
from lxml import html
from lxml import etree

r = requests.get('https://bugcrowd.com/programs')

doc = etree.HTML(r.content)
for url in doc.xpath('//a[@href]'):
    #print(url.get('href'))
    if r.status_code == 200:
         print(url.get('href'), ' - 200 OK!')
    #print( requests.get(url.get('href')))
#print r