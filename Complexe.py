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
