import requests
from bs4 import BeautifulSoup
page = requests.get("https://en.wikipedia.org/wiki/Ryanair")


soup = BeautifulSoup(page.content, 'html.parser')
print(soup.find_all('p'))