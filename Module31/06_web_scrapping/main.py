import requests
from bs4 import BeautifulSoup


res = []
url = 'http://www.columbia.edu/~fdc/sample.html'
response = requests.get(url).content
soup = BeautifulSoup(response, "html.parser")

for link in soup.find_all('h3'):
    res.append(link.get_text())

print(res)
