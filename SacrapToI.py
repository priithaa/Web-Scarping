from bs4 import BeautifulSoup
import requests
import pandas as pd 

source = requests.get('https://timesofindia.indiatimes.com').text

soup = BeautifulSoup(source, 'lxml')

parent = soup.find('div', class_='top-story')


t = list()
for anchor in parent.find_all('a'):

	row=list()
	try:
		row.append(anchor['title'])
		row.append("https://timesofindia.indiatimes.com/"+anchor['href'])
		t.append(row)
	except Exception as e:
		pass

df = pd.DataFrame(t,columns=["Headline","Link"])
print(df)