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
        self.can.create_line(0,550, 600, 550, width = 3)
        self.can.create_line(50,0, 50, 600, width = 3)
        for i in range (37):
            self.can.create_line(45, 550-i*500/36, 55, 550-i*500/36, width = 2)
            self.can.create_line(0, 550-i*500/36, 600, 550-i*500/36)
            self.can.create_text(35, 550-i*500/36, text = str(i))
            self.can.create_line(550-i*500/36, 545, 550-i*500/36, 555, width = 2)
            self.can.create_line(550-i*500/36, 0, 550-i*500/36, 600)
            self.can.create_text(550-i*500/36,565, text = str(36-i))

        
    def placePoint(self, p, color):
        Px = p[0]*500/36 + 50
        Py = 500 - p[1]*500/36 + 50
        self.can.create_oval(Px-5, Py-5, Px+5, Py+5, fill = color)
                    
        
if __name__=="__main__":
    app = App()
    Eab = set()
    a = 14
    b = 7
    for x in range (37):
        for y in range (37):
            if ((y**2-x**3-a*x-b)%37 == 0):
                Eab.add((x, y))
    for i in Eab:
        app.placePoint(i, "magenta")
        
    Eab = set()
    a = 22
    b = 13
    for x in range (37):
        for y in range (37):
            if ((y**2-x**3-a*x-b)%37 == 0):
                Eab.add((x, y))
    for i in Eab:
        app.placePoint(i, "green")
        
    Eab = set()
    a = 33
    b = 17
    for x in range (37):
        for y in range (37):
            if ((y**2-x**3-a*x-b)%37 == 0):
                Eab.add((x, y))
    for i in Eab:
        app.placePoint(i, "blue")
        
    
    app.mainloop() 
