# -*- coding: utf-8 -*-
import turtle

class myturtle:
    def __init__(self):
        self.t=turtle.Turtle()
        self.s=self.t.getscreen()
        
    def showCircle(self):
        self.t.circle(30)
    
    def showT(self):
        for i in range(4):
            self.t.forward(100)
            self.t.left(90)
        
        
    def Go(self):
        self.s.mainloop()
    
t1=myturtle()
t1.showCircle()
t1.showT()
t1.Go()       