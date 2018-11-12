import sys
import time
import random
import math

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
    # taille_ = taille
    solution = sorted(batons, reverse = True)
    print ("sorted : ", solution)
    solutionVoisine = []
    uneSolution = []
    #ici j'essaye de mettre le reste des poids du fichier dans le tableau 
    for i in range(len(resultat)):
        for j in range(i,taille):
            print("i :", i, S[i], "j :",j, solution[j])
            if S[i] == solution[j]:
                print("remove")
               # S.remove(S[i])
               # solution.remove(solution[j])
                break
            else:
                print("append")
                solutionVoisine.append(solution[j])
    print("solution", solutionVoisine)
    poids = 0
    for k in range(len(solutionVoisine)):
        uneSolution.append(solutionVoisine[random.randint(0, (len(solutionVoisine)))])
        poids += uneSolution[k]
        if poids > poidTotal : break

    while poids > poidTotal:
        valeur = random.randint(0,len(uneSolution))
        uneSolution.remove(uneSolution[valeur])
        poids -= uneSolution[valeur]
    return uneSolution        
   
def somme(tableau):
    somme = 0
    for i in range(len(tableau)):
        somme += tableau[i]
    return somme
# t = temperature et doit permettre au debut d'avoir plus de probabilite de prendre le mavaise solution
#teta doit être inferieur à 1 et donc comme chaque fois on multiplie ca par le temperature
# à chaque itératio de l'algo la propabilité de prendre la mauvaise solution doit diminuer
#unif est la probabilite
def recuit(S0, T, kmax, P, alpha):
    S = S0
    sMeilleur = S
    teta = T
    sPrime = []
    for k in (1, kmax):
        for j in (1,P):
            sPrime = gloutonSolutionVoisine(S)
            delta = somme(sPrime) - somme(S)
            valeur = math.exp(delta/(teta*k))
            if delta >= 0 or (valeur >=0 and valeur <=1):
                S = sPrime
                if somme(S) > somme(sMeilleur):
                    sMeilleur = S
        teta *= alpha
    return sMeilleur

S0 = glouton(batons,poidTotal,taille)
print("glouton : ", S0)
recuit = recuit(S0,100,12,5,0.5)
options = sys.argv[2:]
if '-p' in options: # On imprime la solution
    print("84 73 12 44 98 75") # Données bidon, mais output du bon format demandé
if '-t' in options: # On imprime le temps d'exécution
    print("4.1347628746") # Données bidon, mais output du bon format demandé
