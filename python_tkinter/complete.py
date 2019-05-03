import tkinter as tk
import tkinter.messagebox as messagebox
from  tkinter import ttk
import time
from tkinter import Tk, Scrollbar, Frame
from tkinter.ttk import Treeview
#import cv2
import numpy as np
from PIL import Image,ImageTk
#import CV.camera_CV
sum=0#顯示總金額(最下面)
i=0#表格內容
'''
1-->紙類
2-->塑膠類
3-->鐵鋁罐
'''
num1=0
money=0#顯示總金額
sum1=0#顯示投入次數
sum2=0#表格圖案位置
sumi=0#紀錄表格次數
save1=[]#紀錄投入物件名稱(中文)
save2=[]#紀錄投入物件名稱(代碼)
save3=[]#紀錄投入物件當下時間
save4=[]#紀錄投入物件當下圖片
saveK1=[]#紀錄表格數據
saveK2=[]#紀錄表格數據
saveK3=[]#紀錄表格數據
saveK4=[]#紀錄表格數據
list1=[]
########################################################################
class MyApp(object):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        self.win = parent
        self.win.title("Main frame")
        self.frame = tk.Frame(parent)
        self.frame.pack()
        #圖片呼叫
        win.title("拯救海龜的鼻子_開始畫面")
        self.photo_background=tk.PhotoImage(file=r"./拯救海龜的鼻子/背景圖/人機_起始頁面.png")
        self.photo_fb=tk.PhotoImage(file=r"./拯救海龜的鼻子/背景圖/FB.png")
        self.photo_google=tk.PhotoImage(file=r"./拯救海龜的鼻子/背景圖/google.png")
        self.photo_QR=tk.PhotoImage(file=r"./拯救海龜的鼻子/背景圖/QR.png")
        canvas_width = 800
        canvas_height =530
        canvas = tk.Canvas(win, 
        width=canvas_width, 
        height=canvas_height)
        canvas.pack()
        #背景
        canvas.create_image(400,240, image=self.photo_background)
        YY=330
        #選擇登入方式
        but_FB=tk.Button(win,image=self.photo_fb, command=self.ButFB) 
        but_FB.place(x=430,y=YY,width=80,height=80)

        but_google=tk.Button(win,image=self.photo_google, command=self.ButGoogle) 
        but_google.place(x=530,y=YY,width=80,height=80)

        but_QR=tk.Button(win,image=self.photo_QR, command=self.ButQRcode) 
        but_QR.place(x=630,y=YY,width=80,height=80)

        #選擇使用說明
        but=tk.Button(win,text='觀看使用說明',font= ('Noto Sans Mono CJK TC Regular',30),fg='white',bg='magenta', command=self.openFrame) 
        but.place(x=12,y=YY,height=60)

    #----------------------------------------------------------------------
    def ButFB(self):
        """"""
        win_FB = tk.Toplevel()
        win_FB.geometry("250x130+270+180")
        win_FB.title('登入方法')
        def bt_OK():
            win_FB.destroy()
            self.hide()
            self.openFrame1('fb')
        def bt_NO():
            win_FB.destroy()    
        label = tk.Label(win_FB, text='使用FB登入',font= ('Noto Sans Mono CJK TC Regular',20),bg='#B4C6E7')
        label.pack()
        btn_OK = tk.Button(win_FB, text="是",font= ('Noto Sans Mono CJK TC Regular',20),bg='#71C7D5',fg='white',command=bt_OK)
        btn_OK.pack(side=tk.LEFT,padx=(50,20))
        btn_ON = tk.Button(win_FB, text="否",font= ('Noto Sans Mono CJK TC Regular',20),bg='#FF0000',fg='white',command=bt_NO)
        btn_ON.pack(side=tk.LEFT,padx=(30,0))  
    #----------------------------------------------------------------------
    def ButGoogle(self):
        """"""
        win_Google = tk.Toplevel()
        win_Google.geometry("250x130+270+180")
        win_Google.title('登入方法')
        def bt_OK():
            win_Google.destroy()
            self.hide()
            self.openFrame1('Google')
        def bt_NO():
            win_Google.destroy() 
        label = tk.Label(win_Google, text='使用Google登入',font= ('Noto Sans Mono CJK TC Regular',20),bg='#B4C6E7')
        label.pack()
        btn_OK = tk.Button(win_Google, text="是",font= ('Noto Sans Mono CJK TC Regular',20),bg='#71C7D5',fg='white',command=bt_OK)
        btn_OK.pack(side=tk.LEFT,padx=(50,20))
        btn_ON = tk.Button(win_Google, text="否",font= ('Noto Sans Mono CJK TC Regular',20),bg='#FF0000',fg='white',command=bt_NO)
        btn_ON.pack(side=tk.LEFT,padx=(30,0))    
    #----------------------------------------------------------------------
    def ButQRcode(self):
        """"""
        win_QR = tk.Toplevel()
        win_QR.geometry("250x130+270+180")
        win_QR.title('登入方法')
        def bt_OK():
            win_QR.destroy()
            self.hide()
            self.openFrame1('QR')
        def bt_NO():
            win_QR.destroy() 
        label = tk.Label(win_QR, text='使用QRcode登入',font= ('Noto Sans Mono CJK TC Regular',20),bg='#B4C6E7')
        label.pack()
        btn_OK = tk.Button(win_QR, text="是",font= ('Noto Sans Mono CJK TC Regular',20),bg='#71C7D5',fg='white',command=bt_OK)
        btn_OK.pack(side=tk.LEFT,padx=(50,20))
        btn_ON = tk.Button(win_QR, text="否",font= ('Noto Sans Mono CJK TC Regular',20),bg='#FF0000',fg='white',command=bt_NO)
        btn_ON.pack(side=tk.LEFT,padx=(30,0))   
    #----------------------------------------------------------------------
    def ButEXIT(self,c):
        """"""
        win_EXIT = tk.Toplevel()
        win_EXIT.geometry("250x130+270+180")
        win_EXIT.title('清單選擇')
        def bt_OK():
            self.clear()
            win_EXIT.destroy()
            c.destroy()
            self.show()
        def bt_NO():
            global sum,money,sum1,i,num1
            sum+=money
            i+=sum1
            win_EXIT.destroy() 
            self.ButSAVE(c)
        label = tk.Label(win_EXIT, text='請選擇下列選項',font= ('Noto Sans Mono CJK TC Regular',20),bg='#B4C6E7')
        label.pack()
        btn_OK = tk.Button(win_EXIT, text="離開",font= ('Noto Sans Mono CJK TC Regular',20),bg='#71C7D5',fg='white',command=bt_OK)
        btn_OK.pack(side=tk.LEFT,padx=(25,20))
        btn_ON = tk.Button(win_EXIT, text="儲存",font= ('Noto Sans Mono CJK TC Regular',20),bg='#FF0000',fg='white',command=bt_NO)
        btn_ON.pack(side=tk.LEFT,padx=(30,0))        
    #----------------------------------------------------------------------
    def ButSAVE(self,winC):
        """"""
        win_EXIT = tk.Toplevel()
        win_EXIT.geometry("250x130+270+180")
        win_EXIT.title('小提醒')
        
        def bt_OK():
            self.clear()
            win_EXIT.destroy()

        def bt_NO():
            win_EXIT.destroy() 

        label = tk.Label(win_EXIT, text='是否清除本頁面資料',font= ('Noto Sans Mono CJK TC Regular',20),bg='#B4C6E7')
        label.pack()
        btn_OK = tk.Button(win_EXIT, text="是",font= ('Noto Sans Mono CJK TC Regular',20),bg='#71C7D5',fg='white',command=bt_OK)
        btn_OK.pack(side=tk.LEFT,padx=(50,20))
        btn_ON = tk.Button(win_EXIT, text="否",font= ('Noto Sans Mono CJK TC Regular',20),bg='#FF0000',fg='white',command=bt_NO)
        btn_ON.pack(side=tk.LEFT,padx=(30,0))   
    #----------------------------------------------------------------------
    def hide(self):
        """"""
        self.win.withdraw()
    #----------------------------------------------------------------------
    def openFrame(self):
        """"""
        self.hide()
        win_HOW = tk.Toplevel()
        #win_HOW.attributes("-fullscreen", True)
        win_HOW.geometry("800x470")
        win_HOW.title("使用說明")
        win_HOW.photo_background=tk.PhotoImage(file=r"./拯救海龜的鼻子/背景圖/人機_說明頁面.png")
        canvas_width = 800
        canvas_height =530
        canvas = tk.Canvas(win_HOW, 
        width=canvas_width, 
        height=canvas_height)
        canvas.pack()
        #背景
        canvas.create_image(400,240, image=win_HOW.photo_background)

        handler = lambda: self.onCloseOtherFrame(win_HOW)
        btn = tk.Button(win_HOW, text="continue",command=handler,font= ('Noto Sans Mono CJK TC Regular',20),fg='white',bg='Maroon',width=8)
        btn.place(x=330,y=380)
    #----------------------------------------------------------------------
    def openFrame2(self):
        """"""
        self.hide()
        win_L = tk.Toplevel()
        #win_L.attributes("-fullscreen", True)
        win_L.geometry("800x470")
        win_L.title("紀錄查詢")
        win_L.photo_background=tk.PhotoImage(file=r"./拯救海龜的鼻子/背景圖/海龜.png")
        canvas_width = 800
        canvas_height =530
        canvas = tk.Canvas(win_L, 
        width=canvas_width, 
        height=canvas_height)
        canvas.pack()
        #背景
        canvas.create_image(400,240, image=win_L.photo_background)
        handler = lambda: win_L.destroy()
        btn = tk.Button(win_L, text="確定",command=handler,font= ('Noto Sans Mono CJK TC Regular',20),fg='white',bg='Maroon',width=8)
        btn.place(x=330,y=380)  
                
        #使用Treeview組件實現表格功能

        frame = Frame(win_L)

        frame.place(x=100, y=50, width=600, height=280)

        #滾動條

        scrollBar = tk.Scrollbar(frame)

        scrollBar.pack(side=tk.RIGHT, fill=tk.Y)

        #Treeview組件，6列，顯示表頭，帶垂直滾動條

        tree = Treeview(frame,

                                columns=( 'c1' , 'c2' , 'c3' ,'c4'),

                                show= "headings" ,

                                yscrollcommand=scrollBar.set)

        #設置每列寬度和對齊方式

        tree.column( 'c1' , width=80,anchor= 'center' )

        tree.column( 'c2' , width=150, anchor= 'center' )

        tree.column( 'c3' , width=150, anchor= 'center' )

        tree.column( 'c4' , width=200, anchor= 'center' )

        #設置每列表頭標題文本

        tree.heading( 'c1' , text= '投入次數' )

        tree.heading( 'c2' , text= '投入物品(時間)' )

        tree.heading( 'c3' , text= '分類項目(鐵、塑膠、紙)' )

        tree.heading( 'c4' , text= 'SC幣(鐵$3、塑膠$2、紙$1)' )

        tree.pack(side=tk.LEFT, fill=tk.Y)

        #Treeview組件與垂直滾動條結合

        scrollBar.config(command=tree.yview)

        #定義並綁定Treeview組件的鼠標單擊事件

        def treeviewClick(event):

            pass

        tree.bind( '<Button-1>' , treeviewClick)

        for c in range(i):
            tree.insert("",c,values=(c+1,saveK3[c],saveK1[c],saveK2[c])) #插入數據                 
        
    #----------------------------------------------------------------------
    def bt_search(self):
        for aa in range(sum1):
            a="{:}{:}".format(save3[aa],save1[aa])
            list1.append(a)
        okc=tk.messagebox.askokcancel(title='小提醒', message='是否以點擊右下方確定紐')
        if okc == True:
            self.openFrame2()
    #----------------------------------------------------------------------        
    def bt_塑膠(self):
        global sum1,i,money,num1
        if sum1 <10:
            num1+=1
            sum1+=1
            money+=2
            save1.append("塑膠")
            save2.append(2)
            save3.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))   
            saveK1.append("塑膠")
            saveK2.append(2)
            saveK3.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            #make_photo(sum1)
            #self.adj(sum1)
            
    #----------------------------------------------------------------------        
    def bt_紙(self):
        global sum1,i,money,num1
        if sum1 <10:
            num1+=1
            sum1+=1
            money+=1
            save1.append("紙")
            save2.append(1)
            save3.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            saveK1.append("紙")
            saveK2.append(1)
            saveK3.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            #make_photo(sum1)
            #self.adj(sum1)
            
    #----------------------------------------------------------------------
    def bt_鐵(self):
        global sum1,i,money,num1
        if sum1 <10:
            num1+=1
            sum1+=1
            money+=3 
            save1.append("鐵")
            save2.append(3)
            save3.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            saveK1.append("鐵")
            saveK2.append(3)
            saveK3.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))                
            #make_photo(sum1)
            #self.adj(sum1)
            

    def clear(self):
        global money,sum1,num1
        save1.clear()
        save2.clear()
        save3.clear()
        save4.clear()
        sum1=0
        money=0
        num1=0
        #self.顯示(winC=win_main)

    def 顯示(self,winC):
        #winC = tk.Toplevel()
        global sum1,i,money,num1
        #表格圖案位置
        #位置=[115,213,316]     
        # 290
        #以下是定義物件
        winC.photo_L紙類=tk.PhotoImage(file=r"./拯救海龜的鼻子/背景圖/L紙類.png")
        winC.photo_L塑膠類=tk.PhotoImage(file=r"./拯救海龜的鼻子/背景圖/L塑膠類.png")
        winC.photo_L鐵鋁罐=tk.PhotoImage(file=r"./拯救海龜的鼻子/背景圖/L鐵鋁罐.png")
        winC.photo_SC紙類=tk.PhotoImage(file=r"./拯救海龜的鼻子/背景圖/SC紙類.png")
        winC.photo_SC塑膠類=tk.PhotoImage(file=r"./拯救海龜的鼻子/背景圖/SC塑膠類.png")
        winC.photo_SC鐵鋁罐=tk.PhotoImage(file=r"./拯救海龜的鼻子/背景圖/SC鐵鋁罐.png")
        winC.photo_0=tk.PhotoImage(file=r"./拯救海龜的鼻子/數字/0.png")
        winC.photo_1=tk.PhotoImage(file=r"./拯救海龜的鼻子/數字/1.png")
        winC.photo_2=tk.PhotoImage(file=r"./拯救海龜的鼻子/數字/2.png")
        winC.photo_3=tk.PhotoImage(file=r"./拯救海龜的鼻子/數字/3.png")
        winC.photo_4=tk.PhotoImage(file=r"./拯救海龜的鼻子/數字/4.png")
        winC.photo_5=tk.PhotoImage(file=r"./拯救海龜的鼻子/數字/5.png")
        winC.photo_6=tk.PhotoImage(file=r"./拯救海龜的鼻子/數字/6.png")
        winC.photo_7=tk.PhotoImage(file=r"./拯救海龜的鼻子/數字/7.png")
        winC.photo_8=tk.PhotoImage(file=r"./拯救海龜的鼻子/數字/8.png")
        winC.photo_9=tk.PhotoImage(file=r"./拯救海龜的鼻子/數字/9.png")
        winC.photo_10=tk.PhotoImage(file=r"./拯救海龜的鼻子/數字/10.png")
        winC.photo_11=tk.PhotoImage(file=r"./拯救海龜的鼻子/數字/11.png")
        winC.photo_12=tk.PhotoImage(file=r"./拯救海龜的鼻子/數字/12.png")
        winC.photo_13=tk.PhotoImage(file=r"./拯救海龜的鼻子/數字/13.png")
        winC.photo_14=tk.PhotoImage(file=r"./拯救海龜的鼻子/數字/14.png")
        winC.photo_15=tk.PhotoImage(file=r"./拯救海龜的鼻子/數字/15.png")
        winC.photo_16=tk.PhotoImage(file=r"./拯救海龜的鼻子/數字/16.png")
        winC.photo_17=tk.PhotoImage(file=r"./拯救海龜的鼻子/數字/17.png")
        winC.photo_18=tk.PhotoImage(file=r"./拯救海龜的鼻子/數字/18.png")
        winC.photo_19=tk.PhotoImage(file=r"./拯救海龜的鼻子/數字/19.png")
        winC.photo_20=tk.PhotoImage(file=r"./拯救海龜的鼻子/數字/20.png")
        winC.photo_21=tk.PhotoImage(file=r"./拯救海龜的鼻子/數字/21.png")
        winC.photo_22=tk.PhotoImage(file=r"./拯救海龜的鼻子/數字/22.png")
        winC.photo_23=tk.PhotoImage(file=r"./拯救海龜的鼻子/數字/23.png")
        winC.photo_24=tk.PhotoImage(file=r"./拯救海龜的鼻子/數字/24.png")
        winC.photo_25=tk.PhotoImage(file=r"./拯救海龜的鼻子/數字/25.png")
        winC.photo_26=tk.PhotoImage(file=r"./拯救海龜的鼻子/數字/26.png")
        winC.photo_27=tk.PhotoImage(file=r"./拯救海龜的鼻子/數字/27.png")
        winC.photo_28=tk.PhotoImage(file=r"./拯救海龜的鼻子/數字/28.png")
        winC.photo_29=tk.PhotoImage(file=r"./拯救海龜的鼻子/數字/29.png")
        winC.photo_30=tk.PhotoImage(file=r"./拯救海龜的鼻子/數字/30.png")

        winC.im01=tk.PhotoImage(file=r"./test1.png")
        winC.im02=tk.PhotoImage(file=r"./test2.png")
        winC.im03=tk.PhotoImage(file=r"./test3.png")
        '''
        winC.im04=tk.PhotoImage(file=r"./test4.png")
        winC.im05=tk.PhotoImage(file=r"./test5.png")
        winC.im06=tk.PhotoImage(file=r"./test6.png")
        winC.im07=tk.PhotoImage(file=r"./test7.png")
        winC.im08=tk.PhotoImage(file=r"./test8.png")
        winC.im09=tk.PhotoImage(file=r"./test9.png")
        winC.im10=tk.PhotoImage(file=r"./test10.png")
        '''
        num=[winC.photo_0,winC.photo_1,winC.photo_2,winC.photo_3,winC.photo_4,winC.photo_5,
        winC.photo_6,winC.photo_7,winC.photo_8,winC.photo_9,winC.photo_10,
        winC.photo_11,winC.photo_12,winC.photo_13,winC.photo_14,winC.photo_15,
        winC.photo_16,winC.photo_17,winC.photo_18,winC.photo_19,winC.photo_20,
        winC.photo_21,winC.photo_22,winC.photo_23,winC.photo_24,winC.photo_25,
        winC.photo_26,winC.photo_27,winC.photo_28,winC.photo_29,winC.photo_30,]

        L=['',winC.photo_L紙類,winC.photo_L塑膠類,winC.photo_L鐵鋁罐] 
        sc=['',winC.photo_SC紙類,winC.photo_SC塑膠類,winC.photo_SC鐵鋁罐]

        #im=['',winC.im01,winC.im02,winC.im03,winC.im04,winC.im05,
        #    winC.im06,winC.im07,winC.im08,winC.im09,winC.im10]
        im=['',winC.im01,winC.im02,winC.im03]
        canvas_width = 800
        canvas_height =530
        canvas = tk.Canvas(winC, 
        width=canvas_width, 
        height=canvas_height)
        canvas.pack()

        label_SUM = tk.Label(winC, text=0,font= ('Noto Sans Mono CJK TC Regular',30),bg='#A6C0CD')
        label_SUM.place(x=357,y=400)
        #顯示總金額
        label_money = tk.Label(winC, text=0,font= ('Noto Sans Mono CJK TC Regular',16),bg='#B4C6E7')
        label_money.place(x=579,y=360)
        #顯示投入次數
        label_sum1 = tk.Label(winC, text=0,font= ('Noto Sans Mono CJK TC Regular',16),bg='#B4C6E7')
        label_sum1.place(x=286,y=360)
        #顯示樣式總類
        label_sum2 = tk.Label(winC, text=0,font= ('Noto Sans Mono CJK TC Regular',16),bg='#B4C6E7')
        label_sum2.place(x=440,y=360)
        #表格標頭數字
        label_num1 = tk.Label(winC, text=0,font= ('Noto Sans Mono CJK TC Regular',16),bg='#B4C6E7')
        label_num1.place(x=170,y=95)
        label_num2 = tk.Label(winC, text=0,font= ('Noto Sans Mono CJK TC Regular',16),bg='#B4C6E7')
        label_num2.place(x=170,y=200)
        label_num3 = tk.Label(winC, text=0,font= ('Noto Sans Mono CJK TC Regular',16),bg='#B4C6E7')
        label_num3.place(x=170,y=305)
        label_time1 = tk.Label(winC, text="",font= ('Noto Sans Mono CJK TC Regular',8),bg='#B4C6E7')
        label_time1.place(x=220,y=137)
        label_time2 = tk.Label(winC, text="",font= ('Noto Sans Mono CJK TC Regular',8),bg='#B4C6E7')
        label_time2.place(x=220,y=240)
        label_time3 = tk.Label(winC, text="",font= ('Noto Sans Mono CJK TC Regular',8),bg='#B4C6E7')
        label_time3.place(x=220,y=343)

        #顯示總金額(右下角)
        labe = tk.Label(winC,image=num[money])
        labe.place(x=735,y=425)  
        if sum1==0:       
            label_num1.configure(text=0)
            label_num2.configure(text=0)
            label_num3.configure(text=0)
            label_time1.configure(text="")
            label_time2.configure(text="")
            label_time3.configure(text="")
            canvas.create_image(415,213, image=winC.N21)
        elif sum1==1:
            canvas.create_image(440,115, image=L[save2[0]])#第一格
            canvas.create_image(570,115, image=sc[save2[0]])#第一格

            canvas.create_image(290,115, image=im[save2[0]])#第一格

            label_time1.configure(text=save3[0])
            label_num1.configure(text=1)
        elif sum1==2:
            canvas.create_image(440,115, image=L[save2[0]])#第一格
            canvas.create_image(570,115, image=sc[save2[0]])#第一格

            canvas.create_image(290,115, image=im[save2[0]])#第一格

            label_time1.configure(text=save3[0])
            label_num1.configure(text=1)
            
            canvas.create_image(440,213, image=L[save2[1]])#第二格
            canvas.create_image(570,213, image=sc[save2[1]])#第二格 

            canvas.create_image(290,213, image=im[save2[1]])#第二格 

            label_time2.configure(text=save3[1])
            label_num2.configure(text=2)
        else:
            canvas.create_image(440,115, image=L[save2[sum1-3]])#第一格
            canvas.create_image(570,115, image=sc[save2[sum1-3]])#第一格 
            canvas.create_image(290,115, image=im[save2[sum1-3]])#第一格 

            canvas.create_image(440,213, image=L[save2[sum1-2]])#第二格
            canvas.create_image(570,213, image=sc[save2[sum1-2]])#第二格
            canvas.create_image(290,213, image=im[save2[sum1-2]])#第二格 
            
            canvas.create_image(440,316, image=L[save2[sum1-1]])#第三格
            canvas.create_image(570,316, image=sc[save2[sum1-1]])#第三格
            canvas.create_image(290,316, image=im[save2[sum1-1]])#第三格 

            label_num1.configure(text=num1-2)
            label_num2.configure(text=num1-1)
            label_num3.configure(text=num1)  
            label_time1.configure(text=save3[sum1-3])
            label_time2.configure(text=save3[sum1-2])
            label_time3.configure(text=save3[sum1-1])   

        #顯示總金額(右下角)
        labe.configure(image=num[money])
        #顯示總金額
        label_money.configure(text=money)
        #顯示投入次數
        label_sum1.configure(text=sum1)
        #顯示樣式總類
        label_sum2.configure(text=sum2)
        #顯示總金額
        label_SUM.configure(text=sum)        
    #----------------------------------------------------------------------
    def openFrame1(self,tit):
        """"""
        win_main = tk.Toplevel()
        #win_main.attributes("-fullscreen", True)
        win_main.geometry("800x470")
        win_main.title(tit)
        win_main.fb=tk.PhotoImage(file=r"./拯救海龜的鼻子/背景圖/FB.png")
        win_main.google=tk.PhotoImage(file=r"./拯救海龜的鼻子/背景圖/google.png")
        win_main.QR=tk.PhotoImage(file=r"./拯救海龜的鼻子/背景圖/QR.png")
        win_main.N21=tk.PhotoImage(file=r"./拯救海龜的鼻子/背景圖/1.png")     
        win_main.photo_background=tk.PhotoImage(file=r"./拯救海龜的鼻子/背景圖/人機_背景.png")
        canvas_width = 800
        canvas_height =530
        canvas = tk.Canvas(win_main, 
        width=canvas_width, 
        height=canvas_height)
        canvas.pack()
        def bt_OK():
            global sum,money,sum1,i,num1
            print("save3=",save3)
            print("save2=",save2)
            print("save1=",save1)
            self.ButEXIT(win_main)
        
        #背景
        canvas.create_image(400,240, image=win_main.photo_background)
        #handler = lambda: self.onCloseOtherFrame(win_main)
        btn_re = tk.Button(win_main, text="紀錄查詢",font= ('Noto Sans Mono CJK TC Regular',16),bg='#71C7D5',fg='white',command=self.bt_search)
        btn_re.place(x=70,y=410)
        btn_ok = tk.Button(win_main, text="離開/儲存",font= ('Noto Sans Mono CJK TC Regular',20),bg='#FBB03B',fg='white',command =bt_OK)#,command=handler)
        btn_ok.place(x=650,y=100)
        
        

        #測試功能按鈕
        
        def bt_塑膠1():
            self.bt_塑膠()
            self.顯示(win_main)
        def bt_紙1():
            self.bt_紙()
            self.顯示(win_main)
        def bt_鐵1():
            self.bt_鐵()
            self.顯示(win_main)
        
        btn_塑膠 = tk.Button(win_main, text="塑膠",font= ('Noto Sans Mono CJK TC Regular',20),bg='#FBB03B',fg='white',command=bt_塑膠1)
        btn_塑膠.place(x=10,y=100)
        btn_紙 = tk.Button(win_main, text="紙",font= ('Noto Sans Mono CJK TC Regular',20),bg='#FBB03B',fg='white',command=bt_紙1)
        btn_紙.place(x=10,y=200)
        btn_鐵 = tk.Button(win_main, text="鐵",font= ('Noto Sans Mono CJK TC Regular',20),bg='#FBB03B',fg='white',command=bt_鐵1)
        btn_鐵.place(x=10,y=300)

        #右上登入圖
        if tit =='fb':
            canvas.create_image(750,40, image=win_main.fb)
            saveK1.clear()
            saveK2.clear()
            saveK3.clear()
        elif tit =='QR':
            canvas.create_image(750,40, image=win_main.QR)  
            saveK1.clear()
            saveK2.clear()
            saveK3.clear()
        else:
            canvas.create_image(750,40, image=win_main.google)
            saveK1.clear()
            saveK2.clear()
            saveK3.clear()
        
    #----------------------------------------------------------------------
    def onCloseOtherFrame(self, otherFrame):
        """"""
        otherFrame.destroy()
        self.show()
    #----------------------------------------------------------------------
    def show(self):
        """"""
        self.win.update()
        self.win.deiconify()
#----------------------------------------------------------------------
if __name__ == "__main__":
    win = tk.Tk()
    #win.attributes("-fullscreen", True)
    win.geometry("800x470")
    app = MyApp(win)
    win.mainloop()
