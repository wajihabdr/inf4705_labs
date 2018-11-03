import sys
import time
import random

ex_path = sys.argv[1] # Path de l'exemplaire
options = sys.argv[2:]

# Lecture du fichier source
fichier = open(ex_path,'r')
taille = int(fichier.readline())
batons = []
for i in range(taille):
    ligne = fichier.readline().replace('\t\n', '')
    data = ligne.split('\t')
    batons.append(int(data[1]))
poidTotal = int(fichier.readline())

# TODO: Algo ici
def glouton(batons, poidsMax,taille):
    resultat = []
    poids = 0
    i = 1
    if batons[0] < poidsMax :
        resultat.append(batons[0])
        poids += batons[0]
    while i <= taille-1:
        if poids + batons[i] <= poidsMax :
            resultat.append(batons[i])
            poids += batons[i]    
        elif poids == poidsMax :
            break
        i += 1
    return resultat

def gloutonSolutionVoisine(resultat):
    resultat.ap
# t = temperature et doit permettre au debut d'avoir plus de probabilite de prendre le mavaise solution
#teta doit être inferieur à 1 et donc comme chaque fois on multiplie ca par le temperature
# à chaque itératio de l'algo la propabilité de prendre la mauvaise solution doit diminuer
#unif est la probabilite
def recruit(S0, T, kmax, P, alpha):
    S = S0
    sMeilleur = S
    tetaUn = T
    for i in (1, kmax):
        for j in (1,P):
            

        
    return sMeilleur

S0 = glouton(batons,poidTotal,taille)
options = sys.argv[2:]
if '-p' in options: # On imprime la solution
    print("84 73 12 44 98 75") # Données bidon, mais output du bon format demandé
if '-t' in options: # On imprime le temps d'exécution
    print("4.1347628746") # Données bidon, mais output du bon format demandé
