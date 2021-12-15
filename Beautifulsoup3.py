import requests
from bs4 import BeautifulSoup
url="https://www.imdb.com/chart/top/?ref_=nv_mv_250"
content = requests.get(url)
soup = BeautifulSoup(content.text, 'html.parser')
#Extract title Page
print(soup.find('title'))


for heading in soup.find_all('h1'):
   print(heading.text)

for heading in soup.find_all('h3'):
    print(heading.text)

a_string = soup.find(string="The Godfather")
print(a_string)