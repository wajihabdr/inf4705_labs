import sys
import math
import time

ex_path = sys.argv[1]  # Path de l'exemplaire
options = sys.argv[2:]

# Lecture du fichier source
fichier = open(ex_path, 'r')
n = int(fichier.readline())
batons = []

for i in range(n): #O(n)
    ligne = fichier.readline().replace('\t\n', '')
    data = ligne.split('\t')
    batons.append(int(data[1]))
poidTotal = int(fichier.readline())
# -------------------------------------------------------------
def progdyn2(batons, N):
    n = len(batons) #O(len(batons)log(len(batons)))
    c = [[0 for x in range(N+1)] for x in range(n)]

    c[0][0] = True
    for j in range(1, N+1): #O(N+1)
        if batons[0] == j:
            c[0][j] = True
        else:
            c[0][j] = False

    for i in range(1, n): #O((n)(N))
        for j in range(N+1):
            if c[i-1][j] == True:
                c[i][j] = True
            elif batons[i] <= j and c[i-1][j-batons[i]] == True:
                c[i][j] = True
            else:
                c[i][j] = False

    solution = []
    j = N
    i = n-1
    while j > 0: #O < O(N)

        while i > 0 and c[i-1][j] == True:
            i -= 1
        j = j - batons[i]
        if j >= 0:
            solution.append(batons[i])
        i -= 1

    return solution
# -------------------------------------------------------------

start_time = time.time()
result = progdyn2(sorted(batons), poidTotal)
end_time = time.time()

if '-p' in options:  # On imprime la solution
    print(result)
if '-t' in options:  # On imprime le temps d'exécution
    interval = end_time - start_time
    print(interval)
if '-test' in options:
    interval = end_time - start_time
    temps = str(interval).replace('.', ',')

    diffPoids = poidTotal
    for i in range(len(result)):
        diffPoids -= result[i]

    print(temps + ';' + str(diffPoids))