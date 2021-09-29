from bs4 import BeautifulSoup 

import requests
url = "https://www.bbc.com/sport/football"
r = requests.get(url)



#def goal_getsource():
news = []
soup = BeautifulSoup(r.content,'html5lib')
table = soup.find('div', attrs = {'class' : "gel-layout gel-layout--equal gs-u-mt gs-u-mt+@s sp-qa-top-stories"})

for row in table.findAll('div',attrs = {"class":"gel-layout__item"}):
   
    x = {}
    x['title'] = row.div['data-bbc-title']
    x['link'] = row.div['data-bbc-result']
    y = row.find('div',attrs = {'class':'gs-o-media-island'})
    y = y.find('div',attrs = {'class': 'gs-o-responsive-image gs-o-responsive-image--16by9'})
    x['img'] = y.img['data-src'].replace("{width}","480")
    news.append(x)



for news in news:
    print(news['title'])
    print(news['link'])
    print(news['img'])
    print("")
