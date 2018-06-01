"""
Created on Wed Apr 25 09:17:08 2018
@author: Thomas
"""

class EllipticCurve:
    
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p
        self.list_point = []

        
    def __eq__(self, C):
        return (self.a, self.b) == (C.a, C.b)

    def has_point(self, x, y):
        return (y ** 2) % self.p == (x ** 3 + self.a * x + self.b) % self.p

    def __str__(self):
        return ('y^2 = x^3 + {}x + {} modulo {}'.format(self.a, self.b,self.p))
    
    def function(self,x):
        return (x ** 3 + self.a * x + self.b)**0.5 % self.p
    
    def create_all_point(self):
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
    def create_group(self):
        return( [n*self for n in range(self.curve.p)])
        
class Inf(Point):
    
    """The custom infinity point"""
    
    def __init__(self, curve):
        self.curve = curve
        
    def __str__(self):
        return ("I'm like the infinity")
    
    def __eq__(self, Q):
        return isinstance(Q, Inf)

    def __neg__(self):
        """-0 = 0"""
        return self

def inverse(a,b):
    """ return the inverse of a modulo b """
    (c1,u1,v1),(c2,u2,v2)=(a,1,0),(b,0,1)
    l = []
    while c2>0:
        l.append(c2)
        q=c1//c2
        (c1,u1,v1),(c2,u2,v2)=(c2,u2,v2),(c1-q*c2,u1-q*u2,v1-q*v2)
    if 1 not in l :
        raise ValueError("{} is not inversible in z/{}z".format(a,b))
        
    return (u1)
