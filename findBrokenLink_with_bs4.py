import requests
import bs4
import lxml

res = requests.get('http://www.asciitable.com/')
#print(res.text)
soup = bs4.BeautifulSoup(res.text,'lxml')
for link in soup.find_all('a',href=True):
    #response = requests.get(link['href'])

    if res.status_code == 200:
        print(link, ' - 200 OK!')
    #print(link['href'])
