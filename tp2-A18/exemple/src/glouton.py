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
    poidsTries = sorted(batons, reverse = True)
    resultat = []
    poids = 0
    i = 1
    if poidsTries[0] <= poidsMax :
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

start_time = time.time()
result = glouton(batons,poidTotal,taille)
end_time = time.time()
    
if '-p' in options:
    print(result) 
if '-t' in options:  # On imprime le temps d'exécution
    interval = end_time - start_time
    print(interval)

    #print('\n' + 'Temps d execution :' + str(interval) + ' sec')
if '-test' in options:
    interval = end_time - start_time
    temps = str(interval).replace('.', ',')

    diffPoids = poidTotal
    for i in range(len(result)):
        diffPoids -= result[i]

    print(temps + ';' + str(diffPoids))
