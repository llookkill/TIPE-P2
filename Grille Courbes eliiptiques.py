# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 14:01:19 2018

@author: urand Théophane
"""
import tkinter as tk
p = 37
a, b = 14,31
class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Courbes elliptiques")
        self.can = tk.Canvas(self, width = 600, height = 600)
        self.can.pack()
        self.can.create_line(50,550, 550, 550, width = 3)
        self.can.create_line(50,50, 50, 550, width = 3)
        for i in range (p):
            self.can.create_line(45, 550-i*500/(p-1), 55, 550-i*500/(p-1), width = 2)
            self.can.create_line(50, 550-i*500/(p-1), 550, 550-i*500/(p-1))
            self.can.create_text(35, 550-i*500/(p-1), text = str(i))
            self.can.create_line(550-i*500/(p-1), 545, 550-i*500/(p-1), 555, width = 2)
            self.can.create_line(550-i*500/(p-1), 50, 550-i*500/(p-1), 550)
            self.can.create_text(550-i*500/(p-1),565, text = str(p-1-i))

        
    def placePoint(self, point, color):
        Px = point[0]*500/(p-1) + 50
        Py = 500 - point[1]*500/(p-1) + 50
        self.can.create_oval(Px-5, Py-5, Px+5, Py+5, fill = color)
                    
def show(a,b, color):
    for i in courbeElliptique[(a,b)]:
        app.placePoint(i, color)
        
if __name__=="__main__":
    app = App()
    
    courbeElliptique = dict()
    points = list()
    for a in range (p):
        for b in range (p):
            for x in range (p):
                for y in range (p):
                    if ((y**2-x**3-a*x-b)%p == 0):
                        points.append((x,y))
            courbeElliptique[(a,b)] = points
            points = list()
            
    show(1,3, "red")
    show(9,17, "blue")
    

    app.mainloop() 
