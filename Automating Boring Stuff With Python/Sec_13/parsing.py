import bs4
import requests
res = requests.get("https://automatetheboringstuff.com/2e/chapter0/")
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
elems = soup.select('#calibre_link-1669')
print(elems[0].text)
