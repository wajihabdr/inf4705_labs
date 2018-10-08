import sys
import time

# Permet la lecture d'une matrice
# A besoin de path du fichier

fileName1 = str(sys.argv[1])
fileName2 = str(sys.argv[2])
options = sys.argv[3:]

# fonction pour imprimer une matrice


def printMatrice(matrice, N):
    for i in range(N):
        line = ''
        for j in range(N):
            line += str(matrice[i][j]) + '\t'
        print(line)


fichier1 = open(fileName1, 'r')
fichier2 = open(fileName2, 'r')

expoMatrice1 = int(fichier1.readline())
expoMatrice2 = int(fichier2.readline())
if expoMatrice1 == expoMatrice2:
    N = expoMatrice1*2

    matrice1 = [None]*N
    matrice2 = [None]*N

    for i in range(N):
        line1 = fichier1.readline().replace('\t\n', '')
        matrice1[i] = line1.split('\t')

        line2 = fichier2.readline().replace('\t\n', '')
        matrice2[i] = line2.split('\t')

    #
    # Algo Conventionnel
    #
    start_time = time.time()

    result = [[0 for x in range(N)] for y in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += int(matrice1[i][k]) * int(matrice2[k][j])

    end_time = time.time()

    if '-all' in options:  # On imprime la matrice résultat
        print('Matrice 1 :')
        printMatrice(matrice1, N)

        print('\n' + 'Matrice 2 :')
        printMatrice(matrice2, N)

        print('\n' + 'Result :')
        printMatrice(result, N)

    if '-p' in options:  # On imprime la matrice résultat
        print('Result :')
        printMatrice(result, N)

    if '-t' in options:  # On imprime le temps d'exécution
        interval = end_time - start_time
        print('\n' + 'Temps d execution :' + str(interval) + ' sec')

else:
    print('ERREUR !!!')
    print('Les deux matrices sont de taille differente')
