import requests
from bs4 import BeautifulSoup
  
URL = "https://www.skysports.com/football/news"
website = requests.get(URL)


def skysports_getsource():

    news = []

    soup = BeautifulSoup(website.content, 'html5lib')
    # print(soup.prettify())
    table = soup.find('div', attrs = {'class' : 'news-list'}) 

    for row in table.findAll('div', attrs = {'class' : 'news-list__item news-list__item--show-thumb-bp30'}):
        x = {}
        y = row.find('div', attrs = {'class' : 'label'})
        z = row.find('img')
        x['title'] = row.a['title']
        x['link'] = row.a['href']
        x['datetime'] = y.span.text
        x['img'] = z['data-src']
        news.append(x)

    return news
    # print(news[0]['title'])

# for news in news:
#     print(news['title'])
#     print(news['link'])
#     print(news['datetime'])
#     print(news['img'])
#     print("")
# print(table)