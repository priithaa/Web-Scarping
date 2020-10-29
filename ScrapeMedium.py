from bs4 import BeautifulSoup
import requests


source = requests.get('https://medium.com/').text

soup = BeautifulSoup(source, 'lxml')


# print(soup.prettify())

xc = soup.find('div',class_="qj qk v ch ql am qm e d")

k = list()

for article in xc.find_all('a', class_="ax ay az ba bb bc bd be bf bg bh bi bj bk bl"):

	k.append(article['href'])

for a in k:
	print(a)