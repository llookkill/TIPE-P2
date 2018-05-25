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
        reel=self.reel*compB.reel-self.imag*compB.imag
        imag=self.reel*compB.imag+self.imag*compB.reel
        n=None
        return(Complexe(reel,imag,n))


k = 0     
listComp = [None] * 49
for reel in range (7):
    for imag in range (7):
        listComp[k] = Complexe(reel, imag, k)
        k += 1
