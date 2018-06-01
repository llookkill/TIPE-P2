# -*- coding: utf-8 -*-
"""
Created on Wed May 30 11:24:16 2018

@author: duran
"""

#CCCCCCCCCCCCCCCCCCCCCC

# On a des éléments p (points) avec une ordonnée et une abscisse 
# p : (a, b)

#Courbe elliptique ---> P + P = Q = 2P (selon les régles précédentes)

from Point import*




def createGroupP(p):
    grP = list()
    grP.append(p)
    if(p.y == 0):
        grP.append(Inf(p.curve))
    else:
        q = p+p
        n=0
        while (q != -p and q != p):
            grP.append(q)
            q = q+p
        grP.append(Inf(p.curve))
    return(grP)

if __name__=="__main__":
    El=EllipticCurve(1,1,37)
    El.create_all_point()
    groupePointP = createGroupP(El.list_point[0])
    for grosCaca in groupePointP:
        print(grosCaca)

    