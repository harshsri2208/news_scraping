import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://in.reuters.com').read()
soup = bs.BeautifulSoup(source)
print(soup.title)
print(soup.get_text('headlines'))
