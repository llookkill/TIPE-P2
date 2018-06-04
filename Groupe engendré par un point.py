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
                            
#V 2
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
    #On initialise l'élement du groupe (Z/pZ)
    k = 100
    
    #Liste des points qui ont été testés
    pUtilises = list()
    
    #liste des points facteus de p
    pFacteur = list()
    
    #On boucle sur les différentes courbes
    for a in range (k):
        for b in range (k):
            
            #On créé la courbe
            El=EllipticCurve(a,b,k)
            
            #On enregistre tous les points à coordonnées entieres sur cette courbe
            El.create_all_point()
            
            #On boucle sur tous les points de la courbe
            for p in El.list_point:
                #Si on a un point déja utilisé on passe à la suite
                if (p in pUtilises):
                    break
                grP = list()
                grP.append(p)
                if(p.y == 0):
                    grP.append(Inf(p.curve))
                else:
                    try :
                        print(a, " ", b)
                        aux = p
                        q = p+p
                    except:
                        pFacteur.append(aux)
                        pUtilises.append(aux)
                        break
                    while (q not in grP):
                        grP.append(q)
                        try :
                            print(a, " ", b)
                            aux = q
                            q = q+p
                        except:
                            pFacteur.append(aux)
                            pUtilises.append(aux)
                            break
                pUtilises.extend(grP)
                                    
                                    
                
                setG = set(grP)
                pUtilises.union(setG)
                                    
                                    
