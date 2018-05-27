class Complexe:
    def __init__(self, reel, imag, num):
        self.reel = reel
        self.imag = imag
        self.n = num
        
        
    def __add__(self,compB):
        reel = self.reel + compB.reel
        imag = self.imag + compB.imag
        n=None
        return(Complexe(reel, imag, n))
    
    def __mul__(self,compB):
        reel = self.reel*compB.reel-self.imag*compB.imag
        imag = self.reel*compB.imag+self.imag*compB.reel
        n = None
        return(Complexe(reel,imag,n))

    def __rmul__(self,scalaire):
        reel = self.reel
        imag = self.imag
        for k in range(scalaire-1):
            reel+=self.reel
            imag+=self.imag
        n = None
        return(Complexe(reel,imag,n))

    def visualiser(self):
        if self.reel==0 and self.imag==1:
            print('i')
        elif self.reel==0:
            print(self.imag,'i',sep='')
        elif self.imag==1:
            print(self.reel,'+','i',sep='')
        elif self.imag==0:
            print(self.reel)
        elif self.imag<0:
            print(self.reel,self.imag,'i',sep='')
        else:
            print(self.reel,'+',self.imag,'i',sep='')

    def __sub__(self,compB):
        reel = self.reel - compB.reel
        imag = self.imag - compB.imag
        n = None
        return(Complexe(reel,imag,n))

    def __pow__(self,puissance):
        reel = self.reel
        imag = self.imag
        for k in range(puissance-1):
            reel,imag = reel*self.reel-imag*self.imag,reel*self.imag+imag*self.reel
        n = None
        return(Complexe(reel,imag,n))


k = 0     
listComp = [None] * 49
for reel in range (7):
    for imag in range (7):
        listComp[k] = Complexe(reel, imag, k)
        k += 1
