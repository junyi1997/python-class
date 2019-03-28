# -*- coding: utf-8 -*-
import turtle 
#from turtle import*

def my_main():
    t=turtle.Turtle()
    s=turtle.Screen()
    '''
    t=Turtle()
    s=Screen()
    '''
    
    def my_fun():
        t.forward(10)
        
    s.onkey(my_fun,"space")
    s.listen()
    
    my_rect(t,-200,-200,100,50,tcolor=("blue","yellow"))
    s.mainloop()
    
def my_goto(t,x=0,y=0):
    t.penup()
    t.goto(x,y)
    t.pendown()    


def my_rect(t,x,y,w,h,tcolor=("#000000","#000000")):
    edge=(w,h,w,h)                      
    t.pencolor(tcolor[0])
    t.fillcolor(tcolor[1])    
    my_goto(t,x,y)
    t.begin_fill()
    for i in edge:
        t.forward(i)
        t.left(90)
    t.end_fill()




if __name__=="__main__":
    my_main()
    
