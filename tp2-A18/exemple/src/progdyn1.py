import sys
import math

ex_path = sys.argv[1] # Path de l'exemplaire

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
c = [math.inf] * poidTotal
index = [None] * poidTotal

for i in range(taille):
    c[batons[i]] = 1
    index[batons[i]] = -1

for j in range(poidTotal):
    if c[j] != 1:
        for i in range(int(j/2)):
            if c[j] > c[i] + c[j-i]:
                c[j] = c[i] + c[j-i]
                index[j] = i

print('C[N] est : ')
print(c)
print('index :')
print(index)

options = sys.argv[2:]
if '-p' in options: # On imprime la solution
    print("84 73 12 44 98 75") # Données bidon, mais output du bon format demandé
if '-t' in options: # On imprime le temps d'exécution
    print("4.1347628746") # Données bidon, mais output du bon format demandé
