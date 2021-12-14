import requests
from bs4 import BeautifulSoup
page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
print(page)
print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup)

print(soup.prettify())

soup = BeautifulSoup(page.content, 'html.parser')
print(soup.find_all('p'))