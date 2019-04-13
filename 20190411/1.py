# -*- coding: utf-8 -*-
import turtle
from functools import partial
a=0
#from turtle import
def SetTurtleShape(t,s):
    #s.register_shape("T",((10,-6),(0,10),(-10,-6)))
    #t.shape("T")
    t.shapesize(2,2)
def ev_up(t):
    print("...<UP>...")
    t.setheading(90)
    
def ev_left(t):
    print("...<LEFT>...")
    t.setheading(180)
    
def ev_down(t):
    print("...<DOWN>...")
    t.setheading(270)
    
def ev_right(t):
    print("...<RIGHT>...")
    t.setheading(0)

def ev_space(t):
    t.forward(10)

def ev_d(t):
    if t.isdown():
        print("擡起畫筆")
        t.penup() # 擡起畫筆 
        return
    else:
        print("放下畫筆")
        t.pendown()
        return

def ev_start(t):
    print("開始繪製ICON")
    t.begin_poly()

def ev_end(t,s):
    print("結束繪製ICON")
    t.end_poly()
    poly=t.get_poly()
    s.register_shape("Myicon",poly)
    t.shape("Myicon")
    
    
def mymain():
    print("程式開始......")
    t=turtle.Turtle()
    s=turtle.Screen()
    s.setup(0.5,0.5,None,None)
    SetTurtleShape(t,s)
    myup = lambda :ev_up(t) 
    myleft = lambda :ev_left(t) 
    myright = lambda :ev_right(t) 
    mydown = lambda :ev_down(t) 
    myspace=lambda :ev_space(t)
    myd=lambda :ev_d(t)
    t.penup() # 擡起畫筆 
    
    ev_s=partial(ev_start,t)
    ev_e=partial(ev_end,t,s)
    
    s.onkey(myup,'Up')#s.onkey(lambda :t.setheading(90),"Up")
    s.onkey(myleft,'Left')#s.onkey(lambda :t.setheading(270),"Left")
    s.onkey(myright,'Right')#s.onkey(lambda :t.setheading(0),"Right")
    s.onkey(mydown,'Down')#s.onkey(lambda :t.setheading(180),"Down")
    s.onkey(myspace,'space')
    s.onkey(myd,'d')
    s.onkey(ev_s,'s')
    s.onkey(ev_e,'e')
    
    s.listen()
           
    s.mainloop()
    
    
if __name__=="__main__":
    mymain()

        
