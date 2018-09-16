import sys

# Permet la lecture d'une matrice
# A besoin de path du fichier
path = './exemple/exemplaires/'

fileName1 = path + str(sys.argv[1])
fileName2 = path + str(sys.argv[2])

fichier1 = open(fileName1, 'r')
fichier2 = open(fileName2, 'r')

expoMatrice1 = int(fichier1.readline())
expoMatrice2 = int(fichier2.readline())
if expoMatrice1 == expoMatrice2:
    N = expoMatrice1*2
    print('N = ' + str(N))

    matrice1 = [None]*N
    matrice2 = [None]*N

    for i in range(N):
        line1 = fichier1.readline().replace('\t\n', '')
        matrice1[i] = line1.split('\t')

        line2 = fichier2.readline().replace('\t\n', '')
        matrice2[i] = line2.split('\t')

    print('Matrice 1 :')
    for i in range(N):
        print(matrice1[i])

    print('\n' + 'Matrice 2 :')
    for i in range(N):
        print(matrice2[i])

    #
    ## Algo Conventionnel
    #

    result = [[0 for x in range(N)] for y in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += int(matrice1[i][k]) * int(matrice2[k][j])
    print('\n' + 'Result :')
    for i in range(N):
        print(result[i])


else:
    print('ERREUR !!!')
    print('Les deux matrices sont de taille differente')

