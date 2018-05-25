"""
Created on Wed Apr 25 09:17:08 2018

@author: Thomas
"""
import tkinter as tk
W,H,r=600,600,2
u=10
v=1
g=5

class Application(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Première approche")
        self.can = tk.Canvas(self,width=W,height=H,bg='white')
        self.can.pack()
    
class EllipticCurve:
    
    def __init__(self, a, b, application):
        self.a = a
        self.b = b
        self.list_point = []
        self.app=application
    def __eq__(self, C):
        return (self.a, self.b) == (C.a, C.b)

    def has_point(self, x, y):
        return (y ** 2) - (x ** 3 + self.a * x + self.b) < 10**-10

    def __str__(self):
        return ('y^2 = x^3 + {}x + {}'.format(self.a, self.b))
    
    def function(self,x):
        return (x ** 3 + self.a * x + self.b)**0.5
    
    def draw(self):
        
        self.app.can.create_line(W/g,0,W/g,H,fill='black',width=0)
        self.app.can.create_line(0,H/2,W,H/2,fill='black',width=0)
        for x in range(-3,11):
            self.app.can.create_text(int(u*x+W/g)+4,H/2-4,text=str(x),fill='green')
            self.app.can.create_line(round((u*x+W/g),0),H/2,round(u*x+W/g,0),H/2+5,fill='black')
        for x in range(int(-W/g)*100,int(W/2)*100) :
            if not isinstance(self.function(x/100), complex) :
                x=x/100
                y = self.function(x)
                self.app.can.create_oval(int(u*x+W/g),int(v*y+H/2),int(u*x+W/g),int(v*y+H/2),fill='blue',width=0)
                y =-y
                self.app.can.create_oval(int(u*x+W/g),int(v*y+H/2),int(u*x+W/g),int(v*y+H/2),fill='blue',width=0)

        for point in self.list_point :
            self.app.can.create_oval(u*point.x-r+W/g,v*point.y-r+H/2,u*point.x+r+W/g,v*point.y+r+H/2,fill='red',width=1)
            self.app.can.update()
        
class Point:
    """A point on a specific curve."""
    
    def __init__(self, curve, x, y):
        self.curve = curve
        self.x = x 
        self.y = y
        self.curve.list_point.append(self)
        
#        if not self.curve.has_point(x, y):
#            raise ValueError('{} is not on curve {}'.format(self, self.curve))
        
    def __str__(self):
        return ('({}, {})'.format(self.x, self.y))

    def __getitem__(self, index):
        return [self.x, self.y][index]

    def __eq__(self, Q):
        return (self.curve, self.x, self.y) == (Q.curve, Q.x, Q.y)

    def __neg__(self):
        return Point(self.curve, self.x, -self.y)
    
    def __add__(self,Q):
        
        if isinstance(self,Inf) and isinstance(Q,Inf):
            return Q
        if isinstance(self,Inf):
            return Q
        if isinstance(Q,Inf):
            return self
        if self == Q :
            m = (3*(self.x)**2+self.curve.a)/(2*self.y)
            X = m**2-2*self.x
            Y = m*(self.x-X)-self.y
        
        else : 
            
            m = (Q.y-self.y)/(Q.x-self.x)
            X = m**2-self.x-Q.x
            Y = m*(self.x-X)-self.y
        return (Point(self.curve,X,Y))
    
    
    def __mul__(self,n):
        
        """Always put the point before the number ex: A*8 """
        
        if isinstance(n,Point):
            raise ValueError("Can't multiply two objects together")
            
        if type(n) == int and n >= 0 :
            if n == 0:
                return(Inf(self.curve))
            prod = self
            for i in range(n-1):
                prod = self + prod
            return(prod)
        else :
            raise ValueError("Expected n to be a positiv integer")
            
class Inf(Point):
    
    """The custom infinity point"""
    
    def __init__(self, curve):
        self.curve = curve
        
    def __str__(self):
        return (" i'm like infinity")
    
    def __eq__(self, Q):
        return isinstance(Q, Inf)

    def __neg__(self):
        """-0 = 0"""
        return self

def inverse(a,b):
    """ return the inverse of a modulo b """
    (c1,u1,v1),(c2,u2,v2)=(a,1,0),(b,0,1)
    while c2>0:
        q=c1//c2
        (c1,u1,v1),(c2,u2,v2)=(c2,u2,v2),(c1-q*c2,u1-q*u2,v1-q*v2)
    return (u1)
     
     
# Pre-defined exemple 

App = Application()
El=EllipticCurve(-1,12,App)
for x in range(-2,37):
    A = Point(El,x,El.function(x))
El.draw()
App.mainloop()
