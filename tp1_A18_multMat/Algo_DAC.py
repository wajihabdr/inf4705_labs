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
    def additionConventionnelle(A,B):
        taille = len(A)
    C = [[0 for x in range(taille)] for y in range(taille)]
    for i in range(taille):
        for j in range(taille):
            C[i][j] = int(A[i][j]) + int(B[i][j])
    return C

# soustraction conventionnelle
def soustractionConventionnelle(A,B):
    taille = len(A)
    C = [[0 for x in range(taille)] for y in range(taille)]
    for i in range(0,taille):
        for j in range(0,taille):
            C[i][j] = int(A[i][j]) - int(B[i][j])
    return C

#
## Algo Diviser et règner
#
def divideToConquer(A,B): 
    tailleA = len(A)
    tailleB = len(B)
    sousTailleA = len(A)//2
    sousTailleB = len(B)//2
    if taille == 1:
        return [[A[0][0] *B[0][0]]]
    else :
        A1 = [[0 for x in range(sousTailleA)] for y in range(sousTailleA)]]
        A2 = [[0 for x in range(sousTailleA)] for y in range(sousTailleA)]]
        A3 = [[0 for x in range(sousTailleA)] for y in range(sousTailleA)]]
        A4 = [[0 for x in range(sousTailleA)] for y in range(sousTailleA)]]
        B1 = [[0 for x in range(sousTailleB)] for y in range(sousTailleB)]]
        B2 = [[0 for x in range(sousTailleB)] for y in range(sousTailleB)]]
        B3 = [[0 for x in range(sousTailleB)] for y in range(sousTailleB)]]
        B4 = [[0 for x in range(sousTailleB)] for y in range(sousTailleB)]]

        A1B1 = divideToConquer(A1,B1) #ae
        A1B2 = divideToConquer(A1,B1) #af
        A2B3 = divideToConquer(A1,B1) #bg
        A2B4 = divideToConquer(A1,B1) #bf
        A3B1 = divideToConquer(A1,B1) #ce
        A3B4 = divideToConquer(A1,B1) #cf
        A4B3 = divideToConquer(A1,B1) #dg
        A4B4 = divideToConquer(A1,B1) #dh

    
