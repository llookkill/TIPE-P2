import tkinter as tk
from Complex import *

c = 7
p = c**2

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

 
listComp = []
for reel in range (c):
    for imag in range (c):
        listComp.append(Complexe(reel,imag,c,c*reel + imag))

        
if __name__=="__main__":
    app = App()
    
    courbeElliptique = dict()
    points = list()
    
    for a in range (p):
        for b in range (p):
            for x in listComp:
                for y in listComp:
                    if ((y**2-x**3-a*x-b) % p == listComp[0]):
                        points.append((x.n, y.n))
            courbeElliptique[(a,b)] = points
            points = list()
            

#    for a in range (p):
#        for b in range (p):
#            show(a, b, "red")
    show(5, 4, "red")
    app.mainloop() 
