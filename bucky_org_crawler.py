import requests
from bs4 import BeautifulSoup


def trade_spider(max_pages):
	page = 1
	while page <= max_pages:
		url = 'https://thenewboston.com/search.php?type=0&sort=reputation&page==' + str(page)
		source_code = requests.get(url, allow_redirects=False)
		plain_text = source_code.text.encode('ascii', 'replace')
		soup = BeautifulSoup(plain_text,'html.parser')
		for link in soup.findAll('a', {'class': 'user-name'}):
			href = link.get('href')
			title = link.string
			print(href)
			print(title)
		page += 1

trade_spider(1)
