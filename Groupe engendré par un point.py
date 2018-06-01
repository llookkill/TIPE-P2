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


if __name__=="__main__":
    pUtilises = set()
    pFacteur = set()
    for a in range (100):
        for b in range (100):
            El=EllipticCurve(a,b,100)
            El.create_all_point()
            for p in El.list_point:
                grP = list()
                grP.append(p)
                if(p.y == 0):
                    grP.append(Inf(p.curve))
                else:
                    q = p+p
                    n=0
                    while (q not in grP):
                        grP.append(q)
                        try :
                            aux = q
                            q = q+p
                        except:
                            pFacteur.add(aux)
                            break
                
                setG = set(grP)
                pUtilises.union(setG)
                                    
                                    
