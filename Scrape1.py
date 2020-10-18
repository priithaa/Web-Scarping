
from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('VidLinks.csv','w')
source = requests.get('http://coreyms.com').text
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Headline','Summary','Video_Links'])

soup = BeautifulSoup(source, 'lxml')

for article in soup.find_all('article'):

	header = article.h2.text
	print(header)
	print()
	paragraph = article.find('div').p.text
	print(paragraph)
	
	try:
		statement = article.find('iframe', class_='youtube-player')['src']
		vid_id = statement.split('/')[4]

		vid_id = vid_id.split('?')[0]

		yt_link = f'www.youtube.com/watch?v={vid_id}'
	except Exception as e:
		yt_link = None

		

	print(yt_link)
	print()
	csv_writer.writerow([header, paragraph, yt_link])

csv_file.close()