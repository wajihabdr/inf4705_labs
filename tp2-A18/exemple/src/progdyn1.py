import sys
import math
import time

ex_path = sys.argv[1]  # Path de l'exemplaire
options = sys.argv[2:]

# Lecture du fichier source
fichier = open(ex_path, 'r')
n = int(fichier.readline())
batons = []

for i in range(n):
    ligne = fichier.readline().replace('\t\n', '')
    data = ligne.split('\t')
    batons.append(int(data[1]))
poidTotal = int(fichier.readline())

# -------------------------------------------------------------

# -------------------------------------------------------------


def progdyn1(batons, poidTotal):
    c = [math.inf for x in range(poidTotal+1)]
    I = [None for x in range(poidTotal+1)]

    for i in range(len(batons)):
        c[batons[i]] = 1
        I[batons[i]] = -i

    for j in range(poidTotal+1):
        if c[j] != 1:
            for i in range(int(j/2)):
                if c[j] > c[i] + c[j-i]:
                    c[j] = c[i] + c[j-i]
                    I[j] = i

    print(c)
    print(I)
    return []
# -------------------------------------------------------------


start_time = time.time()
result = progdyn1(batons, poidTotal)
end_time = time.time()

options = sys.argv[2:]
if '-p' in options:  # On imprime la solution
    print(result)
if '-t' in options:  # On imprime le temps d'exécution
    interval = end_time - start_time
    print(interval)
