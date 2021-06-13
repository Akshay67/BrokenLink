import requests
from lxml import html
from lxml import etree
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)
r = requests.get('https://bugcrowd.com/programs')


doc = etree.HTML(r.content)
for url in doc.xpath('//a[@href]'):
    #print(url.get('href'))
    if r.status_code == 200:
        print(url.get('href'), Back.GREEN +' 200 OK!')
    elif r.status_code == 404:
        print(url.get('href'), Back.YELLOW + ' 404 Not Found! ')
    elif r.status_code == 500:
        print(url.get('href'), Back.RED + ' - Yooo Man We Got 500 -->  Need Backup..!')
    #print( requests.get(url.get('href')))
