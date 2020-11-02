from bs4 import BeautifulSoup
import requests
import urllib
import shutil

def download_image(image,name):
    filename = "C://Users//CB518tx//Desktop//Web-Scraping//ScrapeI//"+image.split("/")[-1].split('?')[0]
    # print(filename)
    r = requests.get(image, stream =True)
    if r.status_code==200:
    	r.raw.decode_content = True
    	with open(filename,'wb') as f:
    		shutil.copyfileobj(r.raw, f)

    	print('Image Successfully downloaded')
    else:
    	print("Couldn't Download")

source = requests.get('https://www.passiton.com/inspirational-quotes').text

soup = BeautifulSoup(source, 'lxml')

branch = soup.find('section', class_='half-section bg-extra-dark-gray half-section')

for x in branch.find_all('img'):
		download_image(x['src'],x['alt'].split('#')[0])

