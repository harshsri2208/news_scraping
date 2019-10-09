from bs4 import BeautifulSoup
from tkinter import *
import requests

root = Tk()
root.title("News scraper")

frame = Frame(root)
frame.grid(row=1, columnspan=2)

res=requests.get('https://www.indiatoday.in/')
soup=BeautifulSoup(res.text,'lxml')

news_box=soup.find('ul',{'class':'itg-listing'})
all_news=news_box.find_all('a')

print("\nTop News Headlines from IndiaToday.com")
print("--------------------------------------\n")

Label(root, text="Top News Headlines from IndiaToday.com", font="Verdana 10 bold").grid(row=0,columnspan=2)

def get_news():
	rowCount=1

	for widget in frame.winfo_children():
		widget.destroy()

	for news in all_news:
		print(rowCount,") ",news.text)

		Label(frame,justif=LEFT,text=str(rowCount)+") "+news.text).grid(row=rowCount, sticky=W, columnspan=2)

		rowCount=rowCount+1

get_news()
button = Button(root, text='Refresh', width=25, command=get_news).grid(row=2, sticky=W+E, column=0)
button = Button(root, text='Close', width=25, command=root.destroy).grid(row=2, sticky=W+E, column=1)

root.mainloop()
