# -*- coding: utf-8 -*-
from pytube import YouTube
from bs4 import BeautifulSoup
import requests
a=set("")
b=[]
i=0
resp=requests.get("https://www.youtube.com/watch?v=KGaR1sUgHiQ&list=RDKGaR1sUgHiQ&start_radio=1")
if resp.status_code != 200:
    print("Error....")
    quit()
#print(resp.text)
bs=BeautifulSoup(resp.text,"lxml")
data=bs.find_all("a")
for each in data:
    url=each.get("href")
    if "&lis" in url:
        #print("抓到的網址：",url,"\n")
        a.add(url)
print(a)
b=list(a)
i=len(a)
print("i",i)

for j in range(1,i):
    print(b[j])
    c="https://www.youtube.com"+str(b[j])
    yt=YouTube(c)
    print("YT影片名稱：",yt.title)
    print("YT影片長度：{:}秒".format(yt.length))
    yt.streams.first().download()
#lists=yt.streams.all()
#lists[1].download()
#for a in lists:
#    print(a)
#yt.streams.first().download()



