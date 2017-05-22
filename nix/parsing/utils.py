from bs4 import BeautifulSoup
import requests
from parsing.models import Article

URL = 'https://news.ycombinator.com/newest'


def parse(n=1):  # n - number of pages
    url = URL
    for page in range(1, n+1):
        soup = BeautifulSoup(requests.get(url).text, 'html.parser')
        for article in soup.findAll('tr', {'class': 'athing'}):
            a = Article()
            try:
                a.author = article.nextSibling.find("a", {"class": "hnuser"}).text
                a.title = article.find("a", {"class": "storylink"}).text
            except AttributeError:
                print(article)
                continue
            site = article.find("span", {"class": "sitestr"})
            a.url = article.find("a", {"class": "storylink"}).attrs['href']
            if not site:
                a.site = 'news.ycombinator.com'
                a.url = 'https://' + a.site + '/' + a.url
            else:
                a.site = site.text
            a.id = article.get('id')
            a.save()
        url = URL[:-6] + soup.find("a", {"class": "morelink"}).attrs['href']