import sys
import time

# Permet la lecture d'une matrice
# A besoin de path du fichier

fileName1 = str(sys.argv[1])
fileName2 = str(sys.argv[2])
options = sys.argv[3:]

fichier1 = open(fileName1, 'r')
fichier2 = open(fileName2, 'r')

expoMatrice1 = int(fichier1.readline())
expoMatrice2 = int(fichier2.readline())

# LEAF_SIZE : taille à partir de laquelle on arrête de faire une multiplication à l'aide de  
# l'algorithme de strassen pour en faire une avec l'algo conventionnel
LEAF_SIZE = 1

# fonction pour imprimer une matrice
def printMatrice(matrice, N):
    for i in range(N):
        line = ''
        for j in range(N):
            line += str(matrice[i][j]) + '\t'
        print(line)

# addition conventionnelle
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

#multiplication conventionnelle ==> algo conventionnelle
def produitMatriceConventionnelle(A, B) :
    taille = len(A)
    C = [[0 for x in range(taille)] for y in range(taille)]
    for i in range(taille):
        for j in range(taille):
            for k in range(taille):
                C[i][j] += int(A[i][k]) * int(B[k][j])
    return C

if expoMatrice1 == expoMatrice2:
    N = 2**expoMatrice1

    A = [None]*N
    B = [None]*N

    for i in range(N):
        line1 = fichier1.readline().replace('\t\n', '')
        A[i] = line1.split('\t')

        line2 = fichier2.readline().replace('\t\n', '')
        B[i] = line2.split('\t')

    #
    # Algo Strassen
    #

    # multiplication de matrice à l'aide de l'algorithme de strassen
    def strassen(A,B):
        N = len(A)
        taille = int(N/2)
        if N <= LEAF_SIZE : 
            return produitMatriceConventionnelle(A,B)
        else : 
            # division de la matrice en 4 sous-matrices
            taille = int(N/2)
            A11 = [[0 for x in range(0,taille)] for y in range(0,taille)]
            A12 = [[0 for x in range(0,taille)] for y in range(0,taille)]
            A21 = [[0 for x in range(0,taille)] for y in range(0,taille)]
            A22 = [[0 for x in range(0,taille)] for y in range(0,taille)]
            B11 = [[0 for x in range(0,taille)] for y in range(0,taille)]
            B12 = [[0 for x in range(0,taille)] for y in range(0,taille)]
            B21 = [[0 for x in range(0,taille)] for y in range(0,taille)]
            B22 = [[0 for x in range(0,taille)] for y in range(0,taille)]

            for i in range(0,taille):
                for j in range(0,taille):
                    A11[i][j] = A[i][j]  #haut à gauche
                    A12[i][j] = A[i][j + taille] #haut à droite
                    A21[i][j] = A[i + taille][j] #bas à droite 
                    A22[i][j] = A[i + taille][j + taille] #bas à gauche

                    B11[i][j] = B[i][j]  #haut à gauche
                    B12[i][j] = B[i][j + taille] #haut à droite
                    B21[i][j] = B[i + taille][j] #bas à droite 
                    B22[i][j] = B[i + taille][j + taille] #bas à gauche
            
            aResultatMatrice = [[0 for x in range (0,taille)] for y in range(0,taille)]
            bResultatMatrice = [[0 for x in range (0,taille)] for y in range(0,taille)]

            #Calculs des différentes multiplications M
            aResultatMatrice = additionConventionnelle(A11,A22)
            bResultatMatrice = additionConventionnelle(B11,B22)
            M1 = strassen(aResultatMatrice,bResultatMatrice) 

            aResultatMatrice = additionConventionnelle(A21,A22)
            M2 = strassen(aResultatMatrice,B11)   

            bResultatMatrice = soustractionConventionnelle(B12,B22)
            M3 = strassen(A11,bResultatMatrice)

            bResultatMatrice = soustractionConventionnelle(B21,B11)
            M4 = strassen(A22,bResultatMatrice) 

            aResultatMatrice = additionConventionnelle(A11,A12)
            M5 = strassen(aResultatMatrice,B22)  

            aResultatMatrice = soustractionConventionnelle(A21,A11)
            bResultatMatrice = additionConventionnelle(B11,B12)
            M6 = strassen(aResultatMatrice,bResultatMatrice)

            aResultatMatrice = soustractionConventionnelle(A12,A22)
            bResultatMatrice = additionConventionnelle(B21,B22)
            M7 = strassen(aResultatMatrice,bResultatMatrice)

            #calculs des différentes parties de la matrice résultat
            aResultatMatrice = additionConventionnelle(M1,M4)
            bResultatMatrice = soustractionConventionnelle(aResultatMatrice,M5)
            C11 = additionConventionnelle(bResultatMatrice, M7)

            C12 = additionConventionnelle(M3,M5)
            C21 = additionConventionnelle(M2,M4)

            aResultatMatrice = soustractionConventionnelle(M1,M2)
            bResultatMatrice = additionConventionnelle(aResultatMatrice,M3)
            C22 = additionConventionnelle(bResultatMatrice,M6)

            #matrice resultat
            C = [[0 for x in range(N)] for y in range(N)]
            for i in range(taille):
                for j in range(taille):
                    C[i][j] = C11[i][j]
                    C[i][j + taille] = C12[i][j]
                    C[i + taille][j] = C21[i][j]
                    C[i + taille][j + taille] = C22[i][j]
            return C

    start_time = time.time()
    resultat = strassen(A,B)
    end_time = time.time()

    if '-all' in options:  # On imprime la matrice résultat
        print('Matrice 1 :')
        printMatrice(A, len(A))

        print('\n' + 'Matrice 2 :')
        printMatrice(B, len(B))

        print('\n' + 'Result :')
        printMatrice(resultat, len(resultat))

    if '-p' in options:  # On imprime la matrice résultat
        print('Result :')
        printMatrice(resultat, len(resultat))

    if '-t' in options:  # On imprime le temps d'exécution
        interval = end_time - start_time
        print(interval)
        #print('\n' + 'Temps d execution :' + str(interval) + ' sec')

else:
    print('ERREUR !!!')
    print('Les deux matrices sont de taille differentes')

