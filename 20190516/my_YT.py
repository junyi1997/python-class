# -*- coding: utf-8 -*-
"""
Created on Thu May 16 15:24:33 2019

@author: MIS801
"""
from pytube import YouTube

class myyt:
    def __init__(self):
        self.__yt=None
        self.__URL=""

    def SetURL(self,URL):
        self.__URL=URL
        self.__yt=YouTube(self.__URL)
    
    def GetURL(self):
        return self.__URL
    
    @property
    def TheURL(self):
        if self.__URL != "":
            return self.__URL
            print(self.__URL)
        else :
            return "URL is empty..."
    @TheURL.setter
    def TheURL(self,URL):
        if "hacking" in URL:
            URL=""
            return
        self.__URL=URL
        self.__yt=YouTube(self.__URL)
        
    def __GetYTLength(self):
        return self.__yt.length
    
    def __GetYTTitle(self):
        return self.__yt.title
    
    def __Getmin(self):
        return int(self.__GetYTLength())//60
    
    def __Getsec(self):
        return int(self.__GetYTLength())%60
    
    def ShowVideoInfoByConsole(self):
        Length=self.__GetYTLength()
        Title=self.__GetYTTitle()
        mymin=self.__Getmin()
        mysec=self.__Getsec()
        print("--------------START Video Information--------------")
        print("-    影片的標題是：",Title)
        print("-    總時間為：{:}分{:}秒".format(mymin,mysec))
        print("-    總秒數為：{:}秒".format(Length))
        print("---------------END Video Information---------------")
        
yt=myyt()
#yt.SetURL("https://www.youtube.com/watch?v=KGaR1sUgHiQ")
print(yt.TheURL="hacking.com")
#yt.ShowVideoInfoByConsole()
