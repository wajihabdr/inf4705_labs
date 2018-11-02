import sys
import time

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

def glouton(batons, poidsMax,taille):
    resultat = []
    poids = 0
    i = 1
    if batons[0] < poidsMax :
        resultat.append(batons[0])
        poids += batons[0]
    while i <= taille:
        if poids + batons[i] <= poidsMax :
            resultat.append(batons[i])
            poids += batons[i]    
        elif poids == poidsMax :
            break
        i += 1
    return resultat

start_time = time.time()
result = glouton(batons,poidTotal,taille)
end_time = time.time()
    
if '-p' in options:  # On imprime la matrice résultat
    print(result) # Données bidon, mais output du bon format demandé
if '-t' in options:  # On imprime le temps d'exécution
    interval = end_time - start_time
    print(interval)
    #print('\n' + 'Temps d execution :' + str(interval) + ' sec')
