from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests

source = requests.get('https://en.wikipedia.org/wiki/Android_version_history').text

soup = BeautifulSoup(source, 'lxml')

flower = soup.find('table', class_='wikitable')

j = list()
for th in flower.find_all('th'):
	j.append(th.text.split('\n')[0])


t= list()
for tr in flower.find_all('tr'):
	h = list()
	for td in tr.find_all('td'):
		h.append(td.text.split('\n')[0])
	t.append(h)

df = pd.DataFrame(t,columns=j)

print(df)
# print(flower)

# print(soup.prettify())
