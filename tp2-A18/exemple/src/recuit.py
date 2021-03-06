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
for i in range(taille): #O(n)
    ligne = fichier.readline().replace('\t\n', '')
    data = ligne.split('\t')
    batons.append(int(data[1]))
poidTotal = int(fichier.readline())

# TODO: Algo ici
def glouton(batons, poidsMax,taille): #O(taillelogtaille)
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

def gloutonSolutionVoisine(resultat): #O(taillelogtaille)
    solution = sorted(batons, reverse = True) #O(taillelogtaille)
    solutionVoisine = [] #O(1)
    uneSolution = [] #O(1)
    for i in range(len(resultat), len(solution)): 
        solutionVoisine.append(solution[i]) #O(taille)

    poids = 0
    for k in range(len(solutionVoisine)): #O(log len(solutionVoisine) )
        valeurRandom = random.randint(0, (len(solutionVoisine)-1))
        uneSolution.append(solutionVoisine[valeurRandom])
        poids += uneSolution[k]
        if poids > poidTotal : break

    while poids > poidTotal: #O(nlogn)
        index = random.randint(0,len(uneSolution)-1)
        poids -= uneSolution[index]
        uneSolution.remove(uneSolution[index]) #O(n)
    return uneSolution        
   
def somme(tableau): #O(len(tableau))
    somme = 0
    for i in range(len(tableau)):
        somme += tableau[i]
    return somme

def recuit(S0, T, kmax, P, alpha): #O(kmax*taillelogtaille)
    S = S0 #O(1)
    sMeilleur = S #O(1)
    teta = T #O(1)
    sPrime = []
    for k in (1, kmax): #O(kmax)
        for j in (1,P): #O(P)
            sPrime = gloutonSolutionVoisine(S) #O(taillelogtaille)
            delta = somme(sPrime) - somme(S) #O(S) ou #O(sPrime)
            valeur = math.exp(delta/(teta*k))
            if delta >= 0 or (valeur >=0 and valeur <=1): #O(S) ou #O(sPrime)
                S = sPrime
                if somme(S) > somme(sMeilleur):
                    sMeilleur = S
        teta *= alpha
    return sMeilleur

S0 = glouton(batons,poidTotal,taille)

start_time = time.time()
recuit = recuit(S0,100,10,10,0.6)  #O(kmax*taillelogtaille)
end_time = time.time()

options = sys.argv[2:]
if '-p' in options: # On imprime la solution
    print(recuit)
if '-t' in options: # On imprime le temps d'exécution
    interval = end_time - start_time
    print(interval)
if '-test' in options:
    interval = end_time - start_time
    temps = str(interval).replace('.', ',')

    diffPoids = poidTotal
    for i in range(len(recuit)):
        diffPoids -= recuit[i]

    print(temps + ';' + str(diffPoids))
