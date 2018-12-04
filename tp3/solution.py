import sys
import math

nomFichier = sys.argv[1] # Path de l'exemplaire
options = sys.argv[2:]

# Lecture du fichier source
fichier = open(nomFichier,'r')
nCentreInterets = int(fichier.readline())
matriceAdjacente = [None] *nCentreInterets
niveauAppreciation = [None]*nCentreInterets

for i in range(nCentreInterets):
    line1 = fichier.readline().replace(' \n', '')
    matriceAdjacente[i] = line1.split(' ')

tempsMax = int(fichier.readline())

niveauAppreciation = fichier.readline().replace(' \n', '').split(' ')

def genererArretes(graphe) :
    arretes = []
    N = len(graphe)
    for noeud in range(N):
        M = len(graphe[noeud])
        for voisin in range(M):
            arretes.append((noeud,voisin))
    return arretes
        

def printMatrice(matrice):
    N = len(matrice)
    for i in range(N):
        line = ''
        for j in range(N):
            line += matrice[i][j] + '\t'
        print(line)

if '-test' in options:
    print(nCentreInterets)
    print()
    printMatrice(matriceAdjacente)
    print()
    print(tempsMax)
    print()
    print(niveauAppreciation)
    print()
    print(genererArretes(matriceAdjacente))
