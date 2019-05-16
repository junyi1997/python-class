# -*- coding: utf-8 -*-

class flower:
    def __init__(self,n,c):
        print("{:}物件實體初始化中...".format(self))
        self.color=c
        self.name=n
    def show(self):
        print("Hi, I am a {:} Flower...".format(self.color))
        
f1=flower("Lily","藍色")
f1.show()
        
f2=flower("Rose","紅色")
f2.show()
        
f3=flower("Jock","黃色")
f3.show()
        
        