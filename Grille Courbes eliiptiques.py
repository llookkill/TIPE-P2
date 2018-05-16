# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 14:01:19 2018

@author: Durand Théophane
"""
import tkinter as tk
p = 37
a, b = 14,31
Eab = list()
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
          
        for x in range (p):
            for y in range (p):
                if (y**2==x**3+a*x+b):
                    Eab.append((x, y))
        
        for i in Eab:
            self.can.create_text(i[0], i[1], text = "I")
        
    def placePoint(self, p):
        Px = p[0]*500/36 + 50
        Py = 500 - p[1]*500/36 + 50
        self.can.create_oval(Px-3, Py-3, Px+3, Py+3, fill = "red")
                    
        
if __name__=="__main__":
    app = App()
    Eab = set()
    for a in range (36):
        for b in range (36):
            for x in range (36):
                for y in range (36):
                    if (y**2 == x**3 + a * x + b):
                        app.placePoint(x, y)
    app.mainloop() 
