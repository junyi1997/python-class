# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 14:32:06 2019

@author: MIS801
"""
def mouse_R(s):
    s.colormode(255)
    s.bgcolor(255,235,227)

def InitMyWindows(s,w,h):
    s.setup(w,h,None,None)

def ReadShape(filename):
    with open (filename,"r",encoding="UTF-8") as fd:
        data=fd.read()
    data=data.strip()
    datalist=data.split(";")
    resaule=[]
    for eachone in datalist:
        eachone=eachone.strip()
        eachone=eachone.strip("()")
        rec=eachone.split(",")
        rectuple=(eval(rec[0]),eval(rec[1]))
        resaule.append(rectuple) 
    return resaule

def close(s):
    print("程式結束")
    s.bye()
   
def my_main():
    ReadShape("myshape.txt")
    
if __name__=="__main__":
    a=__file__
    print("105103308/吳俊逸 在[",a,"]中.........")
    my_main()