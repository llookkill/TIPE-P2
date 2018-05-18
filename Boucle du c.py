# -*- coding: utf-8 -*-
"""
Created on Wed May 16 10:52:55 2018

@author: duran
"""

b = 1
p = 37


u0 = 0
u1 = 1
r0 = p
r1 = b%p


while 1:
    r2 = r0%r1
    q1 = r0/r1
    
    if (((r2 == 0) or ((u1*b)%p == 1))):
        break
    r0 = r1
    r1 = r2
    aux = u1
    u1 = (u0-q1*u1)%b
    u0 = aux
    
print(u0)
print(u1)
print(r0)
print(r1)
