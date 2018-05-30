import tkinter as tk
p = 49
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
    def __init__(self, reel, imag, num):
        self.reel = reel
        self.imag = imag
        self.n = num
        
    def __str__(self):
        
        if self.reel==0 and self.imag==1:
            return ('i')
        elif self.imag==0:
            return ("{}".format(self.reel))
        elif self.reel==0:
            return ("{}i".format(self.imag))
        elif self.imag==1:
            return ("{}+i".format(self.reel))
        elif self.imag<0:
            return ("{}{}i".format(self.reel,self.imag))
        else:
            return ("{}+{}i".format(self.reel,self.imag))
        
    def __add__(self,B):
        
        if isinstance(B,float) or isinstance(B,int):
            reel = self.reel + B
            imag = self.imag 
            
        if isinstance(B,Complexe):
            reel = self.reel + B.reel
            imag = self.imag + B.imag
            
        return(Complexe(reel, imag, None))
        
    def __radd__(self,B):
        return(self+B)
        
    def __neg__(self):
        
        return(Complexe(-self.reel,-self.imag,self.n))
        
    def __mul__(self,B):
        
        if isinstance(self,Complexe) and isinstance(B,Complexe) : #isinstance is a test for class for example : isinstance(A,Complexe) return True if A is an object from the class Complexe.
            
            reel = self.reel*B.reel-self.imag*B.imag
            imag = self.reel*B.imag+self.imag*B.reel
            return(Complexe(reel,imag,None))
            
        if isinstance(self,Complexe) and isinstance(B,int):
            
            reel = self.reel*B
            imag = self.imag*B
            return(Complexe(reel,imag,None))
            
    def __rmul__(self,B):
        return(self*B)

    def __sub__(self,compB):
        return(self + -compB)
    def __eq__(self,B):
        return (self.reel == B.reel and self.imag == B.imag)
    
    def __mod__(self, scalaire):
        return(Complexe(self.reel % scalaire, self.imag % scalaire, None))
    
#    def __pow__(self,puissance):
#        reel = self.reel
#        imag = self.imag
#        for k in range(puissance-1):
#            reel,imag = reel*self.reel-imag*self.imag,reel*self.imag+imag*self.reel
#        n = None
#        return(Complexe(reel,imag,n))

    def __pow__(self,p):
        prod = 1
        for i in range(p):
            prod = prod*self
        return (prod)

k = 0     
listComp = [None] * 49
for reel in range (7):
    for imag in range (7):
        listComp[k] = Complexe(reel, imag, k)
        k += 1
        
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
    
    for a in range (p):
        for b in range (p):
            show(a, b, "red")

    app.mainloop() 
