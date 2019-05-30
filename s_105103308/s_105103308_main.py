   
import tkinter as tk
import tkinter.messagebox as messagebox
import pickle
from  tkinter import ttk
import time
from tkinter import Tk, Scrollbar, Frame
from tkinter.ttk import Treeview
#import cv2
import numpy as np
from PIL import Image
#import CV.camera_CV

# filebase引用必要套件
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import RPi.GPIO as GPIO

import turtle
########################################################################
class MyApp(object):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, parent):
       self.t=turtle.Turtle()
       self.s=turtle.Screen()
        '''定義變數'''
        self.sum=0#顯示總金額(最下面)
        self.i=0#表格內容
        '''
        1-->紙類
        2-->塑膠類
        3-->鐵鋁罐
        '''
        self.A=0

        self.num1=0
        self.money=0#顯示總金額
        self.sum1=0#顯示投入次數
        self.sum2=0#顯示總分類項
        self.sum2_1=0#顯示總分類項(紙)
        self.sum2_2=0#顯示總分類項(塑膠)
        self.sum2_3=0#顯示總分類項(鐵)

        self.sumi_1=0#紀錄filebase資料比數(Google)
        self.sumi_1_1=0#紀錄上一筆filebase資料比數(Google)
        self.sumi_2=0#紀錄filebase資料比數(fb)
        self.sumi_2_1=0#紀錄上一筆filebase資料比數(Google)
        self.sumi_3=0#紀錄filebase資料比數(QR)
        self.sumi_3_1=0#紀錄上一筆filebase資料比數(Google)

        self.sumi=0#紀錄表格次數
        self.save1=[]#紀錄投入物件名稱(中文)
        self.save2=[]#紀錄投入物件名稱(代碼)SC幣
        self.save3=[]#紀錄投入物件當下時間
        self.save4=[]#紀錄投入物件當下圖片
        self.saveK1=[]#紀錄表格數據
        self.saveK2=[]#紀錄表格數據
        self.saveK3=[]#紀錄表格數據
        self.saveK4=[]#紀錄表格數據
        self.list1=[]

        self.GUI_IN=8#馬達IN1
        self.GUI_紙類=10#馬達IN2
        self.GUI_塑膠=12#馬達IN3
        self.GUI_鐵=11#馬達IN4
        self.GUI_a=0
        self.GUI_b=0
        self.GUI_c=0
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.GUI_IN, GPIO.OUT)
        GPIO.setup(self.GUI_紙類, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.GUI_塑膠, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.GUI_鐵, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.output(self.GUI_IN,GPIO.LOW)

        """Constructor"""
        self.win = parent
        self.win.title("Main frame")
        self.frame = tk.Frame(parent)
        self.frame.pack()
        #圖片呼叫
        win.title("拯救海龜的鼻子_開始畫面")
        self.photo_background=tk.PhotoImage(file=r"./image/人機_起始頁面.png")
        self.photo_fb=tk.PhotoImage(file=r"./image/FB.png")
        self.photo_google=tk.PhotoImage(file=r"./image/google.png")
        self.photo_QR=tk.PhotoImage(file=r"./image/QR.png")
        self.photo_Clear=tk.PhotoImage(file=r"./image/clear.png")
        canvas_width = 800
        canvas_height =530
        canvas = tk.Canvas(win, 
        width=canvas_width, 
        height=canvas_height)
        canvas.pack()
        #背景
        canvas.create_image(400,240, image=self.photo_background)
        
        #選擇登入方式
        but_FB=tk.Button(win,image=self.photo_fb, command=self.ButFB) 
        but_FB.place(x=430,y=330,width=80,height=80)

        but_google=tk.Button(win,image=self.photo_google, command=self.ButGoogle) 
        but_google.place(x=530,y=330,width=80,height=80)

        but_QR=tk.Button(win,image=self.photo_QR, command=self.ButQRcode) 
        but_QR.place(x=630,y=330,width=80,height=80)

        #選擇使用說明
        but=tk.Button(win,text='觀看使用說明',font= ('Noto Sans Mono CJK TC Regular',30),fg='white',bg='magenta', command=self.openFrame) 
        but.place(x=12,y=330,height=60)

        def userPWD():
            cleardata = tk.messagebox.askyesno('Welcome','是否為管理者？')
            if cleardata:  
                self.password()

        but_QR=tk.Button(win,image=self.photo_Clear, command=userPWD) 
        but_QR.place(x=750,y=0,width=50,height=60)
    #----------------------------------------------------------------------
    def chooseclear(self):
        win_ch = tk.Toplevel()
        win_ch.geometry('500x250+130+130')
        win_ch.bg06=tk.PhotoImage(file=r"./image/bg06.png")
        canvas_width = 500
        canvas_height =250
        canvas = tk.Canvas(win_ch, 
        width=canvas_width, 
        height=canvas_height)
        canvas.pack()   
        #背景
        canvas.create_image(130,10, image=win_ch.bg06)
        def print_selection():
            Ans=tk.messagebox.askyesno(title='小提醒', message='你是否選擇要清除' + var.get()+"的資料庫？")
            if Ans:
                if var.get()=='Google':
                    l.config(text='清除Google資料')
                    #手動刪除資料庫
                    C=max(self.sumi_1,self.sumi_2,self.sumi_3)
                    print("C=",C)
                    for i in range(C):
                        if i<9:
                            A="第0{:}次".format(i+1)
                        else:
                            A="第{:}次".format(i+1)
                        doc_ref = db.collection("Google").document(A)
                        doc_ref.delete()

                elif var.get()=='fb':
                    l.config(text='清除fb資料')
                    #手動刪除資料庫
                    C=max(self.sumi_1,self.sumi_2,self.sumi_3)
                    print("C=",C)
                    for i in range(C):
                        if i<9:
                            A="第0{:}次".format(i+1)
                        else:
                            A="第{:}次".format(i+1)
                        doc_ref = db.collection("fb").document(A)
                        doc_ref.delete()
                            
                elif var.get()=='QRcode':
                    l.config(text='清除QRcode資料')
                    #手動刪除資料庫
                    C=max(self.sumi_1,self.sumi_2,self.sumi_3)
                    print("C=",C)
                    for i in range(C):
                        if i<9:
                            A="第0{:}次".format(i+1)
                        else:
                            A="第{:}次".format(i+1)
                        doc_ref = db.collection("QRcode").document(A)
                        doc_ref.delete()
                tk.messagebox.showinfo( "小提醒", "資料已刪除完畢")
                cleardata = tk.messagebox.askyesno('Welcome',
                                    '是否要離開本頁面？')

                if cleardata:
                    win_ch.destroy()        
        def chpwd():
            self.usr_sign_up()
              
        var = tk.StringVar()
        l = tk.Label(win_ch, bg='yellow', text='選擇要清除之資料庫',font= ('Noto Sans Mono CJK TC Regular',20))
        l.place(x=10, y=10)
        btn_chpw = tk.Button(win_ch, text='更改密碼', bg='orange',font= ('Noto Sans Mono CJK TC Regular',20),command=chpwd)
        btn_chpw.place(x=250, y=100)
        r1 = tk.Radiobutton(win_ch, text='Google',
                            variable=var, value='Google',font= ('Noto Sans Mono CJK TC Regular',16),
                            command=print_selection)
        r1.place(x=50, y=70)

        r2 = tk.Radiobutton(win_ch, text='Facebook',
                            variable=var, value='fb',font= ('Noto Sans Mono CJK TC Regular',16),
                            command=print_selection)
        r2.place(x=50, y=130)

        r3 = tk.Radiobutton(win_ch, text='QRcode',
                            variable=var, value='QRcode',font= ('Noto Sans Mono CJK TC Regular',16),
                            command=print_selection)
        r3.place(x=50, y=190)

    def usr_sign_up(self):

        def sign_to_Mofan_Python():
            np = new_pwd.get()
            npf = new_pwd_confirm.get()
            nn = new_name.get()
            with open('usrs_info.pickle', 'rb') as usr_file:
                exist_usr_info = pickle.load(usr_file)
            if np != npf:
                tk.messagebox.showerror('Error', '兩個密碼不相同')
            #elif nn in exist_usr_info:
            #    tk.messagebox.showerror('Error', '此帳號已存在，請直接登入！')
            else:
                exist_usr_info[nn] = np
                with open('usrs_info.pickle', 'wb') as usr_file:
                    pickle.dump(exist_usr_info, usr_file)
                tk.messagebox.showinfo('Welcome', '恭喜你已成功更改密碼！')
                win_pw_sign_up.destroy()
        win_pw_sign_up = tk.Toplevel()
        win_pw_sign_up.geometry("500x200+130+130")
        win_pw_sign_up.title('更改密碼')

        new_name = tk.StringVar()
        new_name.set('105103308')
        tk.Label(win_pw_sign_up, text='使用者帳號: ').place(x=10, y= 10)
        entry_new_name = tk.Entry(win_pw_sign_up, textvariable=new_name)
        entry_new_name.place(x=150, y=10)

        new_pwd = tk.StringVar()
        tk.Label(win_pw_sign_up, text='使用者密碼: ').place(x=10, y=50)
        entry_usr_pwd = tk.Entry(win_pw_sign_up, textvariable=new_pwd, show='*')
        entry_usr_pwd.place(x=150, y=50)

        new_pwd_confirm = tk.StringVar()
        tk.Label(win_pw_sign_up, text='重複輸入密碼: ').place(x=10, y= 90)
        entry_usr_pwd_confirm = tk.Entry(win_pw_sign_up, textvariable=new_pwd_confirm, show='*')
        entry_usr_pwd_confirm.place(x=150, y=90)

        btn_comfirm_sign_up = tk.Button(win_pw_sign_up, text='建立', command=sign_to_Mofan_Python)
        btn_comfirm_sign_up.place(x=150, y=130)

        def usr_clear():
            new_name.set('105103308')
            new_pwd_confirm.set('')
            new_pwd.set('')
        # login and sign up button
        btn_login = tk.Button(win_pw_sign_up, text='C',font= ('Noto Sans Mono CJK TC Regular',18), command=usr_clear)
        btn_login.place(x=420, y=130,width=40,height=40)
        A=0
        def btn0():
                
            if self.A==0:
                self.A=1
                buttontext.set('↑')   
                
            elif self.A==1:
                self.A=0 
                  
                buttontext.set('↓')   
        def btn01():
              
            if self.A==0:
                entry_usr_pwd.insert(tk.END, '1')
            else:
                entry_usr_pwd_confirm.insert(tk.END, '1')

        def btn02():
              
            if self.A==0:
                entry_usr_pwd.insert(tk.END, '2')
            else:
                entry_usr_pwd_confirm.insert(tk.END, '2')
        def btn03():
              
            if self.A==0:
                entry_usr_pwd.insert(tk.END, '3')
            else:
                entry_usr_pwd_confirm.insert(tk.END, '3')
        def btn04():
              
            if self.A==0:
                entry_usr_pwd.insert(tk.END, '4')
            else:
                entry_usr_pwd_confirm.insert(tk.END, '4')
        def btn05():
              
            if self.A==0:
                entry_usr_pwd.insert(tk.END, '5')
            else:
                entry_usr_pwd_confirm.insert(tk.END, '5')
        def btn06():
              
            if self.A==0:
                entry_usr_pwd.insert(tk.END, '6')
            else:
                entry_usr_pwd_confirm.insert(tk.END, '6')
        def btn07():
              
            if self.A==0:
                entry_usr_pwd.insert(tk.END, '7')
            else:
                entry_usr_pwd_confirm.insert(tk.END, '7')
        def btn08():
              
            if self.A==0:
                entry_usr_pwd.insert(tk.END, '8')
            else:
                entry_usr_pwd_confirm.insert(tk.END, '8')
        def btn09():
             
            if self.A==0:
                entry_usr_pwd.insert(tk.END, '9')
            else:
                entry_usr_pwd_confirm.insert(tk.END, '9')
        def btn00():
              
            if self.A==0:
                entry_usr_pwd.insert(tk.END, '0')
            else:
                entry_usr_pwd_confirm.insert(tk.END, '0')
        buttontext = tk.StringVar()
        buttontext.set('↓')   
        btn_login = tk.Button(win_pw_sign_up, textvariable = buttontext,font= ('Noto Sans Mono CJK TC Regular',20), command=btn0)
        btn_login.place(x=340, y=130,width=40,height=40)
        btn_login = tk.Button(win_pw_sign_up, text='0',font= ('Noto Sans Mono CJK TC Regular',20), command=btn00)
        btn_login.place(x=380, y=130,width=40,height=40)
        btn_login = tk.Button(win_pw_sign_up, text='1',font= ('Noto Sans Mono CJK TC Regular',20), command=btn01)
        btn_login.place(x=340, y=90,width=40,height=40)
        btn_login = tk.Button(win_pw_sign_up, text='2',font= ('Noto Sans Mono CJK TC Regular',20), command=btn02)
        btn_login.place(x=380, y=90,width=40,height=40)
        btn_login = tk.Button(win_pw_sign_up, text='3',font= ('Noto Sans Mono CJK TC Regular',20), command=btn03)
        btn_login.place(x=420, y=90,width=40,height=40)
        btn_login = tk.Button(win_pw_sign_up, text='4',font= ('Noto Sans Mono CJK TC Regular',20), command=btn04)
        btn_login.place(x=340, y=50,width=40,height=40)
        btn_login = tk.Button(win_pw_sign_up, text='5',font= ('Noto Sans Mono CJK TC Regular',20), command=btn05)
        btn_login.place(x=380, y=50,width=40,height=40)
        btn_login = tk.Button(win_pw_sign_up, text='6',font= ('Noto Sans Mono CJK TC Regular',20), command=btn06)
        btn_login.place(x=420, y=50,width=40,height=40)
        btn_login = tk.Button(win_pw_sign_up, text='7',font= ('Noto Sans Mono CJK TC Regular',20), command=btn07)
        btn_login.place(x=340, y=10,width=40,height=40)
        btn_login = tk.Button(win_pw_sign_up, text='8',font= ('Noto Sans Mono CJK TC Regular',20), command=btn08)
        btn_login.place(x=380, y=10,width=40,height=40)
        btn_login = tk.Button(win_pw_sign_up, text='9',font= ('Noto Sans Mono CJK TC Regular',20), command=btn09)
        btn_login.place(x=420, y=10,width=40,height=40)
    #----------------------------------------------------------------------
    def password(self):
        self.win_pw = tk.Toplevel()
        self.win_pw.title('root')
        self.win_pw.geometry('500x200+130+130')
        self.win_pw.bg05=tk.PhotoImage(file=r"./image/bg05.png")
        canvas_width = 500
        canvas_height =200
        canvas = tk.Canvas(self.win_pw, 
        width=canvas_width, 
        height=canvas_height)
        canvas.pack()   
        #背景
        canvas.create_image(130,10, image=self.win_pw.bg05)

        # user information
        tk.Label(self.win_pw, text='使用者名稱: ').place(x=50, y= 50)
        tk.Label(self.win_pw, text='使用者密碼: ').place(x=50, y=90)

        var_usr_name = tk.StringVar()
        var_usr_name.set('105103308')
        entry_usr_name = tk.Entry(self.win_pw, textvariable=var_usr_name)
        entry_usr_name.place(x=160, y=50)
        var_usr_pwd = tk.StringVar()
        entry_usr_pwd = tk.Entry(self.win_pw, textvariable=var_usr_pwd, show='*')
        entry_usr_pwd.place(x=160, y=90)

        def usr_login():
            usr_name = var_usr_name.get()
            usr_pwd = var_usr_pwd.get()
            try:
                with open('usrs_info.pickle', 'rb') as usr_file:
                    usrs_info = pickle.load(usr_file)
            except EOFError:
                with open('usrs_info.pickle', 'wb') as usr_file:
                    usrs_info = {'admin': 'admin'}
                    pickle.dump(usrs_info, usr_file)
            if usr_name in usrs_info:
                if usr_pwd == usrs_info[usr_name]:
                    tk.messagebox.showinfo(title='歡迎', message='歡迎來到拯救海龜的鼻子' + usr_name)
                    #cleardata = tk.messagebox.askyesno('Welcome',
                    #                '是否要清空資料庫？')

                    #if cleardata:  
                    self.win_pw.destroy()              
                    self.chooseclear()
                             
                else:
                    tk.messagebox.showerror(message='密碼輸入錯誤')

            else:
                tk.messagebox.showerror(message='查無此人')
                '''
                is_sign_up = tk.messagebox.askyesno('Welcome',
                                    '無使用者資料，是否創建一個？')
                if is_sign_up:
                    self.usr_sign_up()
                '''
        def usr_clear():
            var_usr_name.set('105103308')
            var_usr_pwd.set('')
        # login and sign up button
        btn_login = tk.Button(self.win_pw, text='登入',font= ('Noto Sans Mono CJK TC Regular',18), command=usr_login)
        btn_login.place(x=150, y=130)
        btn_login = tk.Button(self.win_pw, text='C',font= ('Noto Sans Mono CJK TC Regular',18), command=usr_clear)
        btn_login.place(x=420, y=130,width=40,height=40)

        def btn01():
            entry_usr_pwd.insert(tk.END, '1')
        def btn02():
            entry_usr_pwd.insert(tk.END, '2')
        def btn03():
            entry_usr_pwd.insert(tk.END, '3')
        def btn04():
            entry_usr_pwd.insert(tk.END, '4')
        def btn05():
            entry_usr_pwd.insert(tk.END, '5')
        def btn06():
            entry_usr_pwd.insert(tk.END, '6')
        def btn07():
            entry_usr_pwd.insert(tk.END, '7')
        def btn08():
            entry_usr_pwd.insert(tk.END, '8')
        def btn09():
            entry_usr_pwd.insert(tk.END, '9')
        def btn00():
            entry_usr_pwd.insert(tk.END, '0')
            
        btn_login = tk.Button(self.win_pw, text='#',font= ('Noto Sans Mono CJK TC Regular',20))
        btn_login.place(x=340, y=130,width=40,height=40)
        btn_login = tk.Button(self.win_pw, text='0',font= ('Noto Sans Mono CJK TC Regular',20), command=btn00)
        btn_login.place(x=380, y=130,width=40,height=40)
        btn_login = tk.Button(self.win_pw, text='1',font= ('Noto Sans Mono CJK TC Regular',20), command=btn01)
        btn_login.place(x=340, y=90,width=40,height=40)
        btn_login = tk.Button(self.win_pw, text='2',font= ('Noto Sans Mono CJK TC Regular',20), command=btn02)
        btn_login.place(x=380, y=90,width=40,height=40)
        btn_login = tk.Button(self.win_pw, text='3',font= ('Noto Sans Mono CJK TC Regular',20), command=btn03)
        btn_login.place(x=420, y=90,width=40,height=40)
        btn_login = tk.Button(self.win_pw, text='4',font= ('Noto Sans Mono CJK TC Regular',20), command=btn04)
        btn_login.place(x=340, y=50,width=40,height=40)
        btn_login = tk.Button(self.win_pw, text='5',font= ('Noto Sans Mono CJK TC Regular',20), command=btn05)
        btn_login.place(x=380, y=50,width=40,height=40)
        btn_login = tk.Button(self.win_pw, text='6',font= ('Noto Sans Mono CJK TC Regular',20), command=btn06)
        btn_login.place(x=420, y=50,width=40,height=40)
        btn_login = tk.Button(self.win_pw, text='7',font= ('Noto Sans Mono CJK TC Regular',20), command=btn07)
        btn_login.place(x=340, y=10,width=40,height=40)
        btn_login = tk.Button(self.win_pw, text='8',font= ('Noto Sans Mono CJK TC Regular',20), command=btn08)
        btn_login.place(x=380, y=10,width=40,height=40)
        btn_login = tk.Button(self.win_pw, text='9',font= ('Noto Sans Mono CJK TC Regular',20), command=btn09)
        btn_login.place(x=420, y=10,width=40,height=40)


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

        win_FB.bg01=tk.PhotoImage(file=r"./image/bg01.png")
        canvas_width = 250
        canvas_height =130
        canvas = tk.Canvas(win_FB, 
        width=canvas_width, 
        height=canvas_height)
        canvas.pack()   
        #背景
        canvas.create_image(0,0, image=win_FB.bg01)
        label = tk.Label(win_FB, text='使用FB登入',font= ('Noto Sans Mono CJK TC Regular',20),bg='#B4C6E7')
        label.place(x=50,y=10)
        btn_OK = tk.Button(win_FB, text="是",font= ('Noto Sans Mono CJK TC Regular',20),bg='#71C7D5',fg='white',command=bt_OK)
        btn_OK.place(x=50,y=60,width=60,height=60)
        btn_ON = tk.Button(win_FB, text="否",font= ('Noto Sans Mono CJK TC Regular',20),bg='#FF0000',fg='white',command=bt_NO)
        btn_ON.place(x=130,y=60,width=60,height=60)
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
        win_Google.bg02=tk.PhotoImage(file=r"./image/bg02.png")
        canvas_width = 250
        canvas_height =130
        canvas = tk.Canvas(win_Google, 
        width=canvas_width, 
        height=canvas_height)
        canvas.pack()   
        #背景
        canvas.create_image(0,0, image=win_Google.bg02)
        label = tk.Label(win_Google, text='使用Google登入',font= ('Noto Sans Mono CJK TC Regular',20),bg='#B4C6E7')
        label.place(x=20,y=10)
        btn_OK = tk.Button(win_Google, text="是",font= ('Noto Sans Mono CJK TC Regular',20),bg='#71C7D5',fg='white',command=bt_OK)
        btn_OK.place(x=50,y=60,width=60,height=60)
        btn_ON = tk.Button(win_Google, text="否",font= ('Noto Sans Mono CJK TC Regular',20),bg='#FF0000',fg='white',command=bt_NO)
        btn_ON.place(x=130,y=60,width=60,height=60)   
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
        win_QR.bg03=tk.PhotoImage(file=r"./image/bg03.png")
        canvas_width = 250
        canvas_height =130
        canvas = tk.Canvas(win_QR, 
        width=canvas_width, 
        height=canvas_height)
        canvas.pack()   
        #背景
        canvas.create_image(0,0, image=win_QR.bg03)
        label = tk.Label(win_QR, text='使用QRcode登入',font= ('Noto Sans Mono CJK TC Regular',20),bg='#B4C6E7')
        label.place(x=20,y=10)
        btn_OK = tk.Button(win_QR, text="是",font= ('Noto Sans Mono CJK TC Regular',20),bg='#71C7D5',fg='white',command=bt_OK)
        btn_OK.place(x=50,y=60,width=60,height=60)
        btn_ON = tk.Button(win_QR, text="否",font= ('Noto Sans Mono CJK TC Regular',20),bg='#FF0000',fg='white',command=bt_NO)
        btn_ON.place(x=130,y=60,width=60,height=60)
        win_QR.mainloop()  
    #----------------------------------------------------------------------
    def ButEXIT(self,c,sum1,tit):
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
            self.sum+=self.money
            self.i+=self.sum1
            win_EXIT.destroy() 
            self.ButSAVE(c,tit)
        win_EXIT.bg04=tk.PhotoImage(file=r"./image/bg04.png")
        canvas_width = 250
        canvas_height =130
        canvas = tk.Canvas(win_EXIT, 
        width=canvas_width, 
        height=canvas_height)
        canvas.pack()   
        #背景
        canvas.create_image(0,0, image=win_EXIT.bg04)
        label = tk.Label(win_EXIT, text='請選擇下列選項',font= ('Noto Sans Mono CJK TC Regular',20),bg='#B4C6E7')
        label.place(x=20,y=10)
        btn_OK = tk.Button(win_EXIT, text="離開",font= ('Noto Sans Mono CJK TC Regular',20),bg='#71C7D5',fg='white',command=bt_OK)
        btn_OK.place(x=50,y=60,width=60,height=60)
        btn_ON = tk.Button(win_EXIT, text="儲存",font= ('Noto Sans Mono CJK TC Regular',20),bg='#FF0000',fg='white',command=bt_NO)
        btn_ON.place(x=130,y=60,width=60,height=60)       
    #----------------------------------------------------------------------
    def ButSAVE(self,winC,tit):
        """"""
        
        win_EXIT = tk.Toplevel()
        win_EXIT.geometry("250x130+270+180")
        win_EXIT.title('小提醒')
        #上傳資料到filebase
    
        #------------------------------------------------------------------------------
        if tit == "Google":
            for i in range(self.sumi_1_1,self.sumi_1):
                doc = {
                    'sum1':i+1,
                    'name': self.save1[i-self.sumi_1_1],
                    'SCoin': self.save2[i-self.sumi_1_1],
                    'time':self.save3[i-self.sumi_1_1]
                }
                if i<9:
                    A="第0{:}次".format(i+1)
                else:
                    A="第{:}次".format(i+1)
                # 語法
                # doc_ref = db.collection("集合名稱").document("文件id")
                doc_ref = db.collection(tit).document(A)
                # doc_ref提供一個set的方法，input必須是dictionary
                doc_ref.set(doc)
            self.sumi_1_1=self.sumi_1 
        elif tit == "fb":
            for i in range(self.sumi_2_1,self.sumi_2):
                doc = {
                    'sum1':i+1,
                    'name': self.save1[i-self.sumi_2_1],
                    'SCoin': self.save2[i-self.sumi_2_1],
                    'time':self.save3[i-self.sumi_2_1]
                }
                if i<9:
                    A="第0{:}次".format(i+1)
                else:
                    A="第{:}次".format(i+1)
                # 語法
                # doc_ref = db.collection("集合名稱").document("文件id")
                doc_ref = db.collection(tit).document(A)
                # doc_ref提供一個set的方法，input必須是dictionary
                doc_ref.set(doc)
            self.sumi_2_1=self.sumi_2     
        elif tit =="QR":
            for i in range(self.sumi_3_1,self.sumi_3):
                doc = {
                    'sum1':i+1,
                    'name': self.save1[i-self.sumi_3_1],
                    'SCoin':self.save2[i-self.sumi_3_1],
                    'time':self.save3[i-self.sumi_3_1]
                }
                if i<9:
                    A="第0{:}次".format(i+1)
                else:
                    A="第{:}次".format(i+1)
                # 語法
                # doc_ref = db.collection("集合名稱").document("文件id")
                doc_ref = db.collection(tit).document(A)
                # doc_ref提供一個set的方法，input必須是dictionary
                doc_ref.set(doc)
            self.sumi_3_1=self.sumi_3
        #------------------------------------------------------------------------------
        def bt_OK():
            print("in")
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
        win_HOW.photo_background=tk.PhotoImage(file=r"./image/人機_說明頁面.png")
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
    def openFrame2(self,tit):
        
        """"""
        self.hide()
        win_L = tk.Toplevel()
        #win_L.attributes("-fullscreen", True)
        win_L.geometry("800x470")
        win_L.title("紀錄查詢")
        win_L.photo_background=tk.PhotoImage(file=r"./image/海龜.png")
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
        self.save4.clear()
        if tit == "Google":
            self.sumi_1=0
            #Get Collection
            doc_ref = db.collection(tit)
            docs = doc_ref.get()
            print("docs=",docs)
            for doc in docs:
                self.sumi_1+=1
                self.save4.append(doc.to_dict())
            self.sumi_1_1=self.sumi_1    
            print("save4=",self.save4)
            print("sumi_1=",self.sumi_1)
            for i in range(0,self.sumi_1):
                self.saveK1.append(self.save4[i]['sum1'])
                self.saveK2.append(self.save4[i]['time'])
                self.saveK3.append(self.save4[i]['name'])
                self.saveK4.append(self.save4[i]['SCoin'])
                  
        ##############################################################################
            for c in range(self.sumi_1):
                tree.insert("",c,values=(self.saveK1[c],self.saveK2[c],self.saveK3[c],self.saveK4[c])) #插入數據                 
        ##############################################################################    
        elif tit == "fb":
            self.sumi_2=0
            #Get Collection
            doc_ref = db.collection(tit)
            docs = doc_ref.get()
            print("docs=",docs)
            for doc in docs:
                self.sumi_2+=1
                self.save4.append(doc.to_dict())
            self.sumi_2_1=self.sumi_2    
            
            for i in range(0,self.sumi_2):
                self.saveK1.append(self.save4[i]['sum1'])
                self.saveK2.append(self.save4[i]['time'])
                self.saveK3.append(self.save4[i]['name'])
                self.saveK4.append(self.save4[i]['SCoin'])  
                   
        ##############################################################################
            for c in range(self.sumi_2):
                tree.insert("",c,values=(self.saveK1[c],self.saveK2[c],self.saveK3[c],self.saveK4[c])) #插入數據                 
        ##############################################################################            
        elif tit =="QR":
            self.sumi_3=0
            #Get Collection
            doc_ref = db.collection(tit)
            docs = doc_ref.get()
            print("docs=",docs)
            for doc in docs:
                self.sumi_3+=1
                self.save4.append(doc.to_dict())
            self.sumi_3_1=self.sumi_3    
            
            for i in range(0,self.sumi_3):
                self.saveK1.append(self.save4[i]['sum1'])
                self.saveK2.append(self.save4[i]['time'])
                self.saveK3.append(self.save4[i]['name'])
                self.saveK4.append(self.save4[i]['SCoin'])  
                         
        ##############################################################################
            for c in range(self.sumi_3):
                tree.insert("",c,values=(self.saveK1[c],self.saveK2[c],self.saveK3[c],self.saveK4[c])) #插入數據                 
        ##############################################################################
    #----------------------------------------------------------------------
    def bt_search(self,tit):
        self.openFrame2(tit)
    #----------------------------------------------------------------------        
    def bt_塑膠(self,tit):
       
        if self.sum1 <10:
            self.sum2_2=1
            self.num1+=1
            self.sum1+=1
            self.money+=2
            self.save1.append("塑膠")
            self.save2.append(2)
            self.save3.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))   
            #make_photo(sum1)
            #self.adj(sum1)
            
            if tit == "Google":
                self.sumi_1+=1
                print("sumi_1=",self.sumi_1)
                print("sumi_1_1=",self.sumi_1_1)
            elif tit == "fb":
                self.sumi_2+=1
                print("sumi_2=",self.sumi_2)
                print("sumi_2_1=",self.sumi_2_1)
            elif tit =="QR":
                self.sumi_3+=1 
                print("sumi_3=",self.sumi_3)
                print("sumi_3_1=",self.sumi_3_1)
    #----------------------------------------------------------------------        
    def bt_紙(self,tit):
        
        if self.sum1 <10:
            self.sum2_1=1
            self.num1+=1
            self.sum1+=1
            self.money+=1
            self.save1.append("紙")
            self.save2.append(1)
            self.save3.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            
            #make_photo(sum1)
            #self.adj(sum1)
            if tit == "Google":
                self.sumi_1+=1
                print("sumi_1=",self.sumi_1)
                print("sumi_1_1=",self.sumi_1_1)
            elif tit == "fb":
                self.sumi_2+=1
                print("sumi_2=",self.sumi_2)
                print("sumi_2_1=",self.sumi_2_1)
            elif tit =="QR":
                self.sumi_3+=1 
                print("sumi_3=",self.sumi_3)
                print("sumi_3_1=",self.sumi_3_1)
    #----------------------------------------------------------------------
    def bt_鐵(self,tit):
        
        if self.sum1 <10:
            self.sum2_3=1
            self.num1+=1
            self.sum1+=1
            self.money+=3 
            self.save1.append("鐵")
            self.save2.append(3)
            self.save3.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                           
            #make_photo(sum1)
            #self.adj(sum1)
            if tit == "Google":
                self.sumi_1+=1
                print("sumi_1=",self.sumi_1)
                print("sumi_1_1=",self.sumi_1_1)
            elif tit == "fb":
                self.sumi_2+=1
                print("sumi_2=",self.sumi_2)
                print("sumi_2_1=",self.sumi_2_1)
            elif tit =="QR":
                self.sumi_3+=1 
                print("sumi_3=",self.sumi_3)
                print("sumi_3_1=",self.sumi_3_1)
#######################################################################################################
    def clear(self):
        
        #self.openFrame1()
        self.num1=0
        self.money=0#顯示總金額
        self.sum1=0#顯示投入次數
        self.sum2=0#顯示總分類項
        self.sum2_1=0#顯示總分類項(紙)
        self.sum2_2=0#顯示總分類項(塑膠)
        self.sum2_3=0#顯示總分類項(鐵)
        self.save1.clear()#紀錄投入物件名稱(中文)
        self.save2.clear()#紀錄投入物件名稱(代碼)
        self.save3.clear()#紀錄投入物件當下時間
        self.顯示()
        #save4.clear()#紀錄投入物件當下圖片
        
#######################################################################################################        
    
    #----------------------------------------------------------------------
    def 顯示(self):
        #winC = tk.Toplevel()
        
        #表格圖案位置
        #位置=[115,213,316]     
        # 290
        
        num=[self.win_main.photo_0,self.win_main.photo_1,self.win_main.photo_2,self.win_main.photo_3,self.win_main.photo_4,self.win_main.photo_5,
        self.win_main.photo_6,self.win_main.photo_7,self.win_main.photo_8,self.win_main.photo_9,self.win_main.photo_10,
        self.win_main.photo_11,self.win_main.photo_12,self.win_main.photo_13,self.win_main.photo_14,self.win_main.photo_15,
        self.win_main.photo_16,self.win_main.photo_17,self.win_main.photo_18,self.win_main.photo_19,self.win_main.photo_20,
        self.win_main.photo_21,self.win_main.photo_22,self.win_main.photo_23,self.win_main.photo_24,self.win_main.photo_25,
        self.win_main.photo_26,self.win_main.photo_27,self.win_main.photo_28,self.win_main.photo_29,self.win_main.photo_30,]
        
        L=['',self.win_main.photo_L紙類,self.win_main.photo_L塑膠類,self.win_main.photo_L鐵鋁罐] 
        sc=['',self.win_main.photo_SC紙類,self.win_main.photo_SC塑膠類,self.win_main.photo_SC鐵鋁罐]

        #im=['',self.win_main.im01,self.win_main.im02,self.win_main.im03,self.win_main.im04,self.win_main.im05,
        #    self.win_main.im06,self.win_main.im07,self.win_main.im08,self.win_main.im09,self.win_main.im10]
        im=['',self.win_main.im01,self.win_main.im02,self.win_main.im03]
        

        label_SUM = tk.Label(self.win_main, text=0,font= ('Noto Sans Mono CJK TC Regular',30),bg='#A6C0CD')
        label_SUM.place(x=357,y=400)
        #顯示總金額
        label_money = tk.Label(self.win_main, text=0,font= ('Noto Sans Mono CJK TC Regular',16),bg='#B4C6E7')
        label_money.place(x=579,y=360)
        #顯示投入次數
        label_sum1 = tk.Label(self.win_main, text=0,font= ('Noto Sans Mono CJK TC Regular',16),bg='#B4C6E7')
        label_sum1.place(x=286,y=360)
        #顯示樣式總類
        label_sum2 = tk.Label(self.win_main, text=0,font= ('Noto Sans Mono CJK TC Regular',16),bg='#B4C6E7')
        label_sum2.place(x=440,y=360)
        #表格標頭數字
        label_num1 = tk.Label(self.win_main, text=0,font= ('Noto Sans Mono CJK TC Regular',16),bg='#B4C6E7')
        label_num1.place(x=170,y=95)
        label_num2 = tk.Label(self.win_main, text=0,font= ('Noto Sans Mono CJK TC Regular',16),bg='#B4C6E7')
        label_num2.place(x=170,y=200)
        label_num3 = tk.Label(self.win_main, text=0,font= ('Noto Sans Mono CJK TC Regular',16),bg='#B4C6E7')
        label_num3.place(x=170,y=305)
        label_time1 = tk.Label(self.win_main, text="",font= ('Noto Sans Mono CJK TC Regular',8),bg='#B4C6E7')
        label_time1.place(x=220,y=137)
        label_time2 = tk.Label(self.win_main, text="",font= ('Noto Sans Mono CJK TC Regular',8),bg='#B4C6E7')
        label_time2.place(x=220,y=240)
        label_time3 = tk.Label(self.win_main, text="",font= ('Noto Sans Mono CJK TC Regular',8),bg='#B4C6E7')
        label_time3.place(x=220,y=343)

        #顯示總金額(右下角)
        labe = tk.Label(self.win_main,image=num[self.money])
        labe.place(x=735,y=425)  
        if self.sum1==0:       
            label_num1.configure(text=0)
            label_num2.configure(text=0)
            label_num3.configure(text=0)
            label_time1.configure(text="")
            label_time2.configure(text="")
            label_time3.configure(text="")
            self.canvas.create_image(415,213, image=self.win_main.N21)
        elif self.sum1==1:
            self.canvas.create_image(440,115, image=L[self.save2[0]])#第一格
            self.canvas.create_image(570,115, image=sc[self.save2[0]])#第一格

            self.canvas.create_image(290,115, image=im[self.save2[0]])#第一格

            label_time1.configure(text=self.save3[0])
            label_num1.configure(text=1)
        elif self.sum1==2:
            self.canvas.create_image(440,115, image=L[self.save2[0]])#第一格
            self.canvas.create_image(570,115, image=sc[self.save2[0]])#第一格

            self.canvas.create_image(290,115, image=im[self.save2[0]])#第一格

            label_time1.configure(text=self.save3[0])
            label_num1.configure(text=1)
            
            self.canvas.create_image(440,213, image=L[self.save2[1]])#第二格
            self.canvas.create_image(570,213, image=sc[self.save2[1]])#第二格 

            self.canvas.create_image(290,213, image=im[self.save2[1]])#第二格 

            label_time2.configure(text=self.save3[1])
            label_num2.configure(text=2)
        else:
            self.canvas.create_image(440,115, image=L[self.save2[self.sum1-3]])#第一格
            self.canvas.create_image(570,115, image=sc[self.save2[self.sum1-3]])#第一格 
            self.canvas.create_image(290,115, image=im[self.save2[self.sum1-3]])#第一格 

            self.canvas.create_image(440,213, image=L[self.save2[self.sum1-2]])#第二格
            self.canvas.create_image(570,213, image=sc[self.save2[self.sum1-2]])#第二格
            self.canvas.create_image(290,213, image=im[self.save2[self.sum1-2]])#第二格 
            
            self.canvas.create_image(440,316, image=L[self.save2[self.sum1-1]])#第三格
            self.canvas.create_image(570,316, image=sc[self.save2[self.sum1-1]])#第三格
            self.canvas.create_image(290,316, image=im[self.save2[self.sum1-1]])#第三格 

            label_num1.configure(text=self.num1-2)
            label_num2.configure(text=self.num1-1)
            label_num3.configure(text=self.num1)  
            label_time1.configure(text=self.save3[self.sum1-3])
            label_time2.configure(text=self.save3[self.sum1-2])
            label_time3.configure(text=self.save3[self.sum1-1])   

        #顯示總金額(右下角)
        labe.configure(image=num[self.money])
        #顯示總金額
        label_money.configure(text=self.money)
        #顯示投入次數
        label_sum1.configure(text=self.sum1)
        #顯示樣式總類
        label_sum2.configure(text=self.sum2)
        #顯示總金額
        label_SUM.configure(text=self.sum)        
    #----------------------------------------------------------------------
    def openFrame1(self,tit):
        print("in",GPIO.input(self.GUI_IN))
        GPIO.output(self.GUI_IN,GPIO.HIGH)
        time.sleep(1)
        print("self.GUI_IN",self.GUI_IN)
        """"""
        self.win_main = tk.Toplevel()
        #win_main.attributes("-fullscreen", True)
        self.win_main.geometry("800x470")
        self.win_main.title(tit)
        self.win_main.fb=tk.PhotoImage(file=r"./image/FB.png")
        self.win_main.google=tk.PhotoImage(file=r"./image/google.png")
        self.win_main.QR=tk.PhotoImage(file=r"./image/QR.png")
        self.win_main.N21=tk.PhotoImage(file=r"./image/w1.png")     
        self.win_main.photo_background=tk.PhotoImage(file=r"./image/人機_背景.png")
        #以下是定義物件
        self.win_main.photo_L紙類=tk.PhotoImage(file=r"./image/L紙類.png")
        self.win_main.photo_L塑膠類=tk.PhotoImage(file=r"./image/L塑膠類.png")
        self.win_main.photo_L鐵鋁罐=tk.PhotoImage(file=r"./image/L鐵鋁罐.png")
        self.win_main.photo_SC紙類=tk.PhotoImage(file=r"./image/SC紙類.png")
        self.win_main.photo_SC塑膠類=tk.PhotoImage(file=r"./image/SC塑膠類.png")
        self.win_main.photo_SC鐵鋁罐=tk.PhotoImage(file=r"./image/SC鐵鋁罐.png")
        self.win_main.photo_0=tk.PhotoImage(file=r"./image/0.png")
        self.win_main.photo_1=tk.PhotoImage(file=r"./image/1.png")
        self.win_main.photo_2=tk.PhotoImage(file=r"./image/2.png")
        self.win_main.photo_3=tk.PhotoImage(file=r"./image/3.png")
        self.win_main.photo_4=tk.PhotoImage(file=r"./image/4.png")
        self.win_main.photo_5=tk.PhotoImage(file=r"./image/5.png")
        self.win_main.photo_6=tk.PhotoImage(file=r"./image/6.png")
        self.win_main.photo_7=tk.PhotoImage(file=r"./image/7.png")
        self.win_main.photo_8=tk.PhotoImage(file=r"./image/8.png")
        self.win_main.photo_9=tk.PhotoImage(file=r"./image/9.png")
        self.win_main.photo_10=tk.PhotoImage(file=r"./image/10.png")
        self.win_main.photo_11=tk.PhotoImage(file=r"./image/11.png")
        self.win_main.photo_12=tk.PhotoImage(file=r"./image/12.png")
        self.win_main.photo_13=tk.PhotoImage(file=r"./image/13.png")
        self.win_main.photo_14=tk.PhotoImage(file=r"./image/14.png")
        self.win_main.photo_15=tk.PhotoImage(file=r"./image/15.png")
        self.win_main.photo_16=tk.PhotoImage(file=r"./image/16.png")
        self.win_main.photo_17=tk.PhotoImage(file=r"./image/17.png")
        self.win_main.photo_18=tk.PhotoImage(file=r"./image/18.png")
        self.win_main.photo_19=tk.PhotoImage(file=r"./image/19.png")
        self.win_main.photo_20=tk.PhotoImage(file=r"./image/20.png")
        self.win_main.photo_21=tk.PhotoImage(file=r"./image/21.png")
        self.win_main.photo_22=tk.PhotoImage(file=r"./image/22.png")
        self.win_main.photo_23=tk.PhotoImage(file=r"./image/23.png")
        self.win_main.photo_24=tk.PhotoImage(file=r"./image/24.png")
        self.win_main.photo_25=tk.PhotoImage(file=r"./image/25.png")
        self.win_main.photo_26=tk.PhotoImage(file=r"./image/26.png")
        self.win_main.photo_27=tk.PhotoImage(file=r"./image/27.png")
        self.win_main.photo_28=tk.PhotoImage(file=r"./image/28.png")
        self.win_main.photo_29=tk.PhotoImage(file=r"./image/29.png")
        self.win_main.photo_30=tk.PhotoImage(file=r"./image/30.png")

        self.win_main.im01=tk.PhotoImage(file=r"./image/test1.png")
        self.win_main.im02=tk.PhotoImage(file=r"./image/test2.png")
        self.win_main.im03=tk.PhotoImage(file=r"./image/test3.png")
        '''
        self.win_main.im04=tk.PhotoImage(file=r"./test4.png")
        self.win_main.im05=tk.PhotoImage(file=r"./test5.png")
        self.win_main.im06=tk.PhotoImage(file=r"./test6.png")
        self.win_main.im07=tk.PhotoImage(file=r"./test7.png")
        self.win_main.im08=tk.PhotoImage(file=r"./test8.png")
        self.win_main.im09=tk.PhotoImage(file=r"./test9.png")
        self.win_main.im10=tk.PhotoImage(file=r"./test10.png")
        '''
        self.canvas_width = 800
        self.canvas_height =530
        self.canvas = tk.Canvas(self.win_main, 
        width=self.canvas_width, 
        height=self.canvas_height)
        self.canvas.pack()
        def bt_OK():
            print("out")
            GPIO.output(self.GUI_IN,GPIO.LOW)
            print("save3=",self.save3)
            print("save2=",self.save2)
            print("save1=",self.save1)
            self.ButEXIT(self.win_main,self.sum1,tit)
        
        #背景
        self.canvas.create_image(400,240, image=self.win_main.photo_background)
        #handler = lambda: self.onCloseOtherFrame(win_main)
        btn_re = tk.Button(self.win_main, text="紀錄查詢",font= ('Noto Sans Mono CJK TC Regular',16),bg='#71C7D5',fg='white',command=lambda:self.bt_search(tit))
        btn_re.place(x=70,y=410)
        btn_ok = tk.Button(self.win_main, text="離開/儲存",font= ('Noto Sans Mono CJK TC Regular',20),bg='#FBB03B',fg='white',command =bt_OK)#,command=handler)
        btn_ok.place(x=650,y=100)

        #測試功能按鈕
        
        def bt_塑膠1():
            self.bt_塑膠(tit)
            self.顯示()
        def bt_紙1():
            self.bt_紙(tit)
            self.顯示()
        def bt_鐵1():
            self.bt_鐵(tit)
            self.顯示()
            
            
        self.s.onkey(lambda:bt_塑膠1(),self.GUI_a=GPIO.input(self.GUI_紙類))  
        self.s.onkey(lambda:bt_紙1(),self.GUI_a=GPIO.input(self.GUI_紙類))  
        self.s.onkey(lambda:bt_鐵1(),self.GUI_c=GPIO.input(self.GUI_鐵))  
        self.s.listen()
        '''
        while True:
            self.GUI_a=GPIO.input(self.GUI_紙類)
            self.GUI_b=GPIO.input(self.GUI_塑膠)
            self.GUI_c=GPIO.input(self.GUI_鐵)
            #print("GUI_a",self.GUI_a,"GUI_b",self.GUI_b,"GUI_c",self.GUI_c)
            time.sleep(1)
            if self.GUI_a ==1:
                bt_紙1()
                print("是紙類")
            elif self.GUI_b ==1:
                bt_塑膠1()
                print("是塑膠類")
            elif self.GUI_c ==1:
                pass
            else:
                pass    
                
            #self.win_main.mainloop()
        '''    
        '''
        btn_塑膠 = tk.Button(self.win_main, text="塑膠",font= ('Noto Sans Mono CJK TC Regular',20),bg='#FBB03B',fg='white',command=bt_塑膠1)
        btn_塑膠.place(x=10,y=100)
        btn_紙 = tk.Button(self.win_main, text="紙",font= ('Noto Sans Mono CJK TC Regular',20),bg='#FBB03B',fg='white',command=bt_紙1)
        btn_紙.place(x=10,y=200)
        btn_鐵 = tk.Button(self.win_main, text="鐵",font= ('Noto Sans Mono CJK TC Regular',20),bg='#FBB03B',fg='white',command=bt_鐵1)
        btn_鐵.place(x=10,y=300)
        '''
        #右上登入圖
        if tit =='fb':
            self.canvas.create_image(750,40, image=self.win_main.fb)
            self.saveK1.clear()
            self.saveK2.clear()
            self.saveK3.clear()
        elif tit =='QR':
            self.canvas.create_image(750,40, image=self.win_main.QR)  
            self.saveK1.clear()
            self.saveK2.clear()
            self.saveK3.clear()
        else:
            self.canvas.create_image(750,40, image=self.win_main.google)
            self.saveK1.clear()
            self.saveK2.clear()
            self.saveK3.clear()
        
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
    # 引用私密金鑰
    # path/to/serviceAccount.json 請用自己存放的路徑
    cred = credentials.Certificate(r'./serviceAccount.json')

    # 初始化firebase，注意不能重複初始化
    firebase_admin.initialize_app(cred)

    # 初始化firestore
    db = firestore.client()
    
    win = tk.Tk()
    win.attributes("-fullscreen", True)
    win.geometry("800x470")
    app = MyApp(win)

    #更新資料筆數(QR)
    doc_ref = db.collection("Google")
    docs = doc_ref.get()
    print("docs=",docs)
    app.sumi_1=0
    for doc in docs:
        app.sumi_1+=1
    app.sumi_1_1=app.sumi_1 

    #更新資料筆數(QR)
    doc_ref = db.collection("fb")
    docs = doc_ref.get()
    print("docs=",docs)
    app.sumi_2=0
    for doc in docs:
        app.sumi_2+=1
    app.sumi_2_1=app.sumi_2 

    #更新資料筆數(QR)
    doc_ref = db.collection("QR")
    docs = doc_ref.get()
    print("docs=",docs)
    app.sumi_3=0
    for doc in docs:
        app.sumi_3+=1
    app.sumi_3_1=app.sumi_3   
 
    win.mainloop()

