# -*- coding: utf-8 -*-
"""
Created on Fri May 25 13:48:20 2018

@author: duran
"""

class Complexe:
    def __init__(self, reel, imag, num):
        self.reel = reel
        self.imag = imag
        self.n = num
        
    def __mul__(self, compB):
        return(Complexe)
  
k = 0     
listComp = [None] * 49
for reel in range (7):
    for imag in range (7):
        listComp[k] = Complexe(reel, imag, k)
        k += 1
