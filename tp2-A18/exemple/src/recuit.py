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
    poidsTries = sorted(batons, reverse = True)
    resultat = []
    poids = 0
    i = 1
    if poidsTries[0] < poidsMax :
        resultat.append(poidsTries[0])
        poids += poidsTries[0]
    while i <= taille-1:
        if poids + poidsTries[i] <= poidsMax :
            resultat.append(poidsTries[i])
            poids += poidsTries[i]    
        elif poids == poidsMax :
            break
        i += 1
    return resultat

def gloutonSolutionVoisine(resultat):
    S = []
    S = resultat
    solution = sorted(batons, reverse = True)
    solutionVoisine = []
    #ici j'essaye de mettre le reste des poids du fichier dans le tableau 
    for i in len(resultat):
        for j in taille:
            if solution[j] == S[i]:
                solution.remove(solution[j])
            else:
                solutionVoisine.append(solution[j])
    return solutionVoisine
            
    S.append(random.randint(1,))
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
