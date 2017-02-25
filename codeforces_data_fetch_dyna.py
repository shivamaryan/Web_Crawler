import requests
from bs4 import BeautifulSoup


def trade_spider(max_pages):
	page = 1
	while page <= max_pages:
		url = 'http://codeforces.com/problemset/standings/page/' + str(page)
		source_code = requests.get(url, allow_redirects=False)
		plain_text = source_code.text.encode('ascii', 'replace')
		soup = BeautifulSoup(plain_text,'html.parser')
		for link in soup.findAll('a', {'class': 'rated-user user-red'}):
			href = 'http://codeforces.com'+link.get('href')
			title = link.string
			#print(href)
			print('')
			print(title) 
			get_single_item_data(href)
		page += 1

def get_single_item_data(item_url):
		source_code = requests.get(item_url, allow_redirects=False)
		plain_text = source_code.text.encode('ascii', 'replace')
		soup = BeautifulSoup(plain_text,'html.parser')
		for link in soup.findAll('span', {'class': 'user-red'}):
			a=link.string
			print(a,end=' ')
			

trade_spider(1)
