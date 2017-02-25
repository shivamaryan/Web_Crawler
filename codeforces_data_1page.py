import requests
from bs4 import BeautifulSoup


def trade_spider(max_pages):
	page = 1
	while page <= max_pages:
		url = 'http://codeforces.com/problemset/standings?friendsEnabled=on' #+ str(page)
		source_code = requests.get(url, allow_redirects=False)
		plain_text = source_code.text.encode('ascii', 'replace')
		soup = BeautifulSoup(plain_text,'html.parser')
		for link in soup.findAll('a', {'class': 'rated-user user-red'}):
			href = 'http://codeforces.com'+link.get('href')
			title = link.get('title')
			
			print(title)	#Newbie or pupil, or any other, is printed here
			print(href)
		page += 1

trade_spider(1)
