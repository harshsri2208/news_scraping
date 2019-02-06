from bs4 import BeautifulSoup
import requests

res=requests.get('https://www.indiatoday.in/')
soup=BeautifulSoup(res.text,'lxml')

news_box=soup.find('ul',{'class':'itg-listing'})
all_news=news_box.find_all('a')

print("\nTop News Headlines from IndiaToday.com")
print("--------------------------------------\n")

x=1

for news in all_news:
	print(x,") ",news.text)
	x=x+1