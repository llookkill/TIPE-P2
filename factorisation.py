# -*- coding: utf-8 -*-
"""
Created on Wed May 30 11:24:16 2018

@author: duran
"""

#CCCCCCCCCCCCCCCCCCCCCC

# On a des éléments p (points) avec une ordonnée et une abscisse 
# p : (a, b)

#Courbe elliptique ---> P + P = Q = 2P (selon les régles précédentes)

from Point import*   # Utilisation du module POint, donnant acces aux classes Point, et ElliptiqueCurve
def pgcd(a,b) :  
   #Fonction permettant le calcul du PGCD entre deux entiers a et b
   while a%b != 0 : 
      a, b = b, a%b 
   return b

if __name__=="__main__":
    #On initialise l'élement du groupe (Z/pZ)
    k = 15
    
    #Liste des points qui ont été testés
    pUtilises = set()
    fact = set()
    #liste des points facteus de p
    pFacteur = set()
    #On boucle sur les différentes courbes
    for a in range (k):
        for b in range (k):
            #On créé la courbe
            El=EllipticCurve(a,b,k)
            
            #On enregistre tous les points à coordonnées entieres sur cette courbe
            El.create_all_point()
            
            #On boucle sur tous les points de la courbe
            for p in El.list_point:
               #Si le point p à déja été utilisé, on passe à la suite afin d'accélérer le processus
                if p not in pUtilises:
                    grP = list() #Liste définissant le groupe engendré par P
                    grP.append(p)
                     
                     #Si l'ordonnée de P est nulle on passe à la suite car le point n'est pas intéréssant.
                    if(p.y == 0):
                        pass
                    else:
                     #Pour chaque point on essaie de l'additionner à lui même  si une erreur (inverse inexistant) apparait, on sait que ce point à un facteur commun avec le modulo
                        try :
                            aux = p
                            q = p+p
                        except ValueError:
                            pFacteur.add(aux)
                            fact.add(pgcd(2*aux.y,k)) #Cette instruction permet de retrouver le diviseur du modulo qui nous intéresse
                            pUtilises.add(aux)
                            break
                          #On boucle sur en additionnant p à q en détéctant à chaque fois si une erreur est soulevée
                        while (q not in grP):
                           
                            grP.append(q)
                            try :
                                aux = q
                                q = q+p
                            except ValueError:
                                pFacteur.add(aux)
                                fact.add(pgcd(q.x-p.x, k))
                                pUtilises.add(aux)
                                break
                    pUtilises = pUtilises.union(set(grP))
    #On affiche tous les facteur trouvés
    print(fact)                            
