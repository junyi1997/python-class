# -*- coding: utf-8 -*-
import my1
print("in my 1",__name__)

def add(x,y):
    return(print(x+y))
    
if __name__=="__main__":
    add(3,5)
    