from bs4 import BeautifulSoup
import requests
import pandas as pd
source = requests.get('https://boston.craigslist.org/search/sof').text

soup = BeautifulSoup(source, 'lxml')

tiles = list()
for a in soup.find_all('li', class_="result-row"):
	h=list()
	h.append(a.div.a.text)
	h.append(a.div.a['href'])
	tiles.append(h)


data = pd.DataFrame(tiles, columns=['Job Posting', 'Link'])

print(data)