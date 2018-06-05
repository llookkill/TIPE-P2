"""
Created on Wed Apr 25 09:17:08 2018
@author: Thomas
"""

class EllipticCurve: #classe de la courbe
    
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p # ajout d'un paramètre p pour le modulo
        self.list_point = []

        
    def __eq__(self, C):
        return (self.a, self.b) == (C.a, C.b)

    def has_point(self, x, y):
        return (y ** 2) % self.p == (x ** 3 + self.a * x + self.b) % self.p

    def __str__(self):
        return ('y^2 = x^3 + {}x + {} modulo {}'.format(self.a, self.b,self.p))
    
    def create_all_point(self):# on crée tous les points de la courbe que l'on enregistre dans list_point
        for x in range(self.p):
            for y in range(self.p):
                if self.has_point(x,y):
                    self.list_point.append(Point(self,x,y))
                    
class Point: 
    
    """A point on a specific curve."""
    
    def __init__(self, curve, x, y):
        self.curve = curve
        self.x = x 
        self.y = y
    
    def __repr__(self): #repésentation du Point dans l'interpréteur
        return( "Point : Coordonées({}, {})".format(self.x, self.y))
    
    def __str__(self):
        return ('({}, {})'.format(self.x, self.y))
    
    def __hash__(self): #permet de définir un hash identique pour deux points de même coordonées (utile pour faire des set de points)
        return(hash(self.__repr__()))

    def __getitem__(self, index):
        return [self.x, self.y][index]

    def __eq__(self, Q):
        return (self.x, self.y) == (Q.x, Q.y)

    def __neg__(self):
        return Point(self.curve, self.x, -self.y)
    
    def __add__(self,Q): #ajout du modulo p dans les calculs de l'addition ainsi que la fonction inverse()
        
        if isinstance(self,Inf) and isinstance(Q,Inf):
            return Q
        if isinstance(self,Inf):
            return Q
        if isinstance(Q,Inf):
            return self
        if self == Q :
            m = (3*(self.x)**2+self.curve.a)*inverse((2*self.y),self.curve.p)
            X = m**2-2*self.x
            Y = m*(self.x-X)-self.y
        
        else : 
            
            m = (Q.y-self.y)*inverse((Q.x-self.x),self.curve.p)
            X = m**2-self.x-Q.x
            Y = m*(self.x-X)-self.y
        return (Point(self.curve,X%self.curve.p,Y%self.curve.p))
    
    def __mul__(self,n):
        
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
            
    def __rmul__(self,n):
        return(self*n)
        
        
class Inf(Point):
    
    """The custom infinity point"""
    
    def __init__(self, curve):
        self.curve = curve
        self.x=self.y='inf'
    def __str__(self):
        return ("I'm like the infinity")
    
    def __repr__(self):
        return("point à l'infini")
    def __eq__(self, Q):
        return isinstance(Q, Inf)

    def __neg__(self):
        """-0 = 0"""
        return self
    
    def __hash__(self):
        return(hash(self.__repr__()))
        
def inverse(a,b): # définition de la fonction qui renvoie l'inverse de a modulo b via l'algorithme d'Euclide étendu
    """ return the inverse of a modulo b """
    (c1,u1,v1),(c2,u2,v2)=(a,1,0),(b,0,1)
    l = []
    while c2>0:
        l.append(c2)
        q=c1//c2
        (c1,u1,v1),(c2,u2,v2)=(c2,u2,v2),(c1-q*c2,u1-q*u2,v1-q*v2)
    if 1 not in l : # on vérifie que c'est bien l'inverse sinon on retourne une erreur  
        raise ValueError("{} is not inversible in z/{}z".format(a,b))
        
    return (u1)
