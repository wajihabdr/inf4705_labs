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
def genSolution(c, I, poidsMax, solution):
    if I[poidsMax] < 1:
        solution.append(poidsMax)
    else:
        solution = genSolution(c, I, I[poidsMax], solution)
        solution = genSolution(c, I, poidsMax - I[poidsMax], solution)
    return solution
# -------------------------------------------------------------
def progdyn1(batons, poidTotal):
    n = len(batons)
    c = [math.inf for x in range(poidTotal+1)]
    I = [0 for x in range(poidTotal+1)]

    for i in range(n):
        c[batons[i]] = 1
        I[batons[i]] = -i

    for j in range(poidTotal+1):
        if c[j] != 1:
            for i in range(math.floor(j/2)):
                if c[j] > c[i] + c[j-i]:
                    c[j] = c[i] + c[j-i]
                    I[j] = i

    solution = []
    return genSolution(c, I, poidTotal, solution)
# -------------------------------------------------------------

start_time = time.time()
result = progdyn1(batons, poidTotal)
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