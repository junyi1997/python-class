# -*- coding: utf-8 -*-
import turtle 
#from turtle import*

t=turtle.Turtle()
s=turtle.Screen()
'''
t=Turtle()
s=Screen()
'''
def my_rect():
    t.begin_fill()
    for i in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()

my_rect()
s.mainloop()
