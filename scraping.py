# import urllib2
from urllib.request import urlopen


url = "http://www.goal.com/en/news/fifa-18-player-ratings-the-complete-list-of-the-top-100/141gsqcxv5djl11pm1cq061eks"
page = urlopen(url)
from bs4 import BeautifulSoup

soup = BeautifulSoup(page)

all_tables=soup.find_all('center')

print (all_tables[0].h2.strong)


