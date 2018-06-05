# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 14:01:19 2018

@author: urand Théophane
"""
import tkinter as tk
p = 7
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
        
class Complexe:
    """Objets créé à partir d'un carré non existant (à l'image des complexes dans R)
    Un objet complexe à une valeur réelle, une valeur imaginaire, et un numéro arbitraire
    """
    def __init__(self, reel, imag, num):
        self.reel = reel
        self.imag = imag
        self.n = num
        
        
    def __add__(self,compB):
        """On définit l'adition de deux complexes comme l'addition des valeurs entieres entre elles et l'addition des valeurs imaginaires entre elles
        """
        reel = self.reel + compB.reel
        imag = self.imag + compB.imag
        n=None
        return(Complexe(reel, imag, n))
        
    def __sub__(self,compB):
        reel = self.reel - compB.reel
        imag = self.imag - compB.imag
        n=None
        return(Complexe(reel, imag, n))
    
    def __mul__(self,compB):
        """La multiplication est semblable à celle des complexes dans C au détail pres que les valeurs réelles et imaginaires sont modulo p)"""
        reel=self.reel*compB.reel-self.imag*compB.imag
        imag=self.reel*compB.imag+self.imag*compB.reel
        n=None
        return(Complexe(reel,imag,n))
        
    def __pow__(self, n):
        for k in range (n):
            a = self * self
        return a


listComp = [None] * 49
for reel in range (p):
    for imag in range (p):
        listComp[k] = Complexe(reel, imag, reel+c*imag)

        
if __name__=="__main__":
    app = App()
    
    courbeElliptique = dict()
    points = list()
    for a in range (p):
        for b in range (p):
            for x in listComp:
                for y in listComp:
                    if ((y**2-x**3-a*x-b)%p == 0):
                        points.append((x.n, y.n))
            courbeElliptique[(a,b)] = points
            points = list()
    
    show(1,1, "red")

    app.mainloop() 
