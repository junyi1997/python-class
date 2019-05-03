# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 14:32:06 2019

@author: MIS801
"""
import turtle
import tkinter as tk
import pyqrcode
from pyqrcode import QRCode 
import sys

    
def my_main():
    import s_105103308_lib as lib
    t=turtle.Turtle()
    s=turtle.Screen()
    s.setup(1000,800,-300,250)
    s.register_shape("T",((30.0, 0.0), (28.53, 9.27), (24.27, 17.64), 
                          (17.64, 24.27), (9.27, 28.53), (0.0, 30.0), 
                          (-9.27, 28.53), (-17.64, 24.27), (-24.27, 17.64),
                          (-28.53, 9.27), (-30.0, 0.0), (-28.53, -9.27), 
                          (-24.27, -17.64), (-17.64, -24.27), (-9.27, -28.53), 
                          (-0.0, -30.0), (9.27, -28.53), (17.64, -24.27), 
                          (24.27, -17.64), (28.53, -9.27)))
    t.shape("T")
    t.shapesize(2,2)
    t.penup()
    t.goto(-300,250)
    
    t.stamp()
    s.onkey(lambda : quit(),"X")
    s.onclick(lib.mouse_R(s),btn=2)
    s.onkey(lambda :lib.mouse_R(s),"1")
    s.listen()
    
    
    while True:
        b=input("URL：")
        if b=="http://www.oit.edu.tw":
            '''
            print("我QRcode不會做")
            s.register_shape(".//QR.gif")
            t.shape(".//QR.gif")
            t.penup()
            t.goto(0,0)
            break
            '''
            qr = QRCode('http://www.oit.edu.tw')
            codeimg=qr.xbm(8)
            codebmp=tk.BitmapImage(data=codeimg)
            cv=s.getcanvas()
            cv.creat_image(0,0,image=codebmp,anchor=tk.N)
            
    s.mainloop()
if __name__=="__main__":
    a=__file__
    print("105103308/吳俊逸 在[",a,"]中.........")
    my_main()
    
    