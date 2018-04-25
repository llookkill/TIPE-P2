"""
Created on Wed Apr 25 09:17:08 2018

@author: Thomas
"""

import random
import matplotlib

class EllipticCurve:
    
    """Represents a single elliptic curve defined over a finite field.

    See here:
        http://en.wikipedia.org/wiki/Elliptic_curve
        http://jeremykun.com/2014/02/24/elliptic-curves-as-python-objects/

    p must be prime, since we use the modular inverse to compute point
    addition.

    """
    
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __eq__(self, C):
        return (self.a, self.b) == (C.a, C.b)

    def has_point(self, x, y):
        return (y ** 2) - (x ** 3 + self.a * x + self.b) < 10**-5

    def __str__(self):
        return ('y^2 = x^3 + {}x + {}'.format(self.a, self.b))

class Point:
    """A point on a specific curve."""
    
    def __init__(self, curve, x, y):
        self.curve = curve
        self.x = x 
        self.y = y

        if not self.curve.has_point(x, y):
            raise ValueError('{} is not on curve {}'.format(self, self.curve))

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

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
    
    """The custom infinity point."""
    def __init__(self, curve):
        self.curve = curve

    def __eq__(self, Q):
        return isinstance(Q, Inf)

    def __neg__(self):
        """-0 = 0"""
        return self
    
#pre-defined curve
El=EllipticCurve(3,5)
A,B=Point(El,-1,1),Point(El,1,3)
