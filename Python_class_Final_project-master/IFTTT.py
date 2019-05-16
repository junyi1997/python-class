
#推撥Code
#沒事不要執行Line會很吵
from urllib.request import urlopen
from urllib.parse import quote
from datetime import datetime
from threading import Timer

def printTime(inc,endtime,text,i):
    if i< endtime:
        i+=1
        print(i,datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        c="第{:}次小提醒".format(i)
        d="要推播之內容為{:}".format(text)
        a=quote(c,'utf-8')
        b=quote(d,'utf-8')
        html = urlopen("https://maker.ifttt.com/trigger/105103308/with/key/dqTARGjv_Q1zeS_-LY1TyV?value1={:}&value2={:}".format(a,b))
        t = Timer(inc, printTime, (inc,endtime,text,i,))
        t.start()

def my_main():
    i=0
    mytime=eval(input("請輸入間隔秒數："))
    endtime=eval(input("請輸推播次數："))
    text=input("請輸入要推播之內容：")
    printTime(mytime,endtime,text,i)
if __name__ == "__main__":
    my_main()