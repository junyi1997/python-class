# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 14:32:06 2019

@author: MIS801
"""
import turtle
import tkinter as tk
import pyqrcode
import sys
import s_105103308_lib as lib
    
def my_main():
    
    t=turtle.Turtle()
    s=turtle.getscreen()
    lib.InitMyWindows(s,1000,800)
    shapedata=lib.ReadShape("myshape.txt")
    s.register_shape("myshape",tuple(shapedata))
    t.shape("myshape")
    t.shapesize(2,2)
    t.penup()
    t.goto(-300,250)
    t.pendown()
    t.stamp()
    
    qr = pyqrcode.QRCode("www.oit.edu.tw")
    codeimg=qr.xbm(8)
    codebmp=tk.BitmapImage(data=codeimg)
    cv=s.getcanvas()
    cv.create_image(0,0,image=codebmp,anchor=tk.N) 
    
    s.onkey(lambda : lib.close(s),"X")
    
    s.onclick(lambda x,y:lib.mouse_R(s),btn=3)
    
    s.listen()
    s.mainloop()

if __name__=="__main__":
    a=__file__
    print("105103308/吳俊逸 在[",a,"]中.........")
    my_main()
    
    