import sys
import math

nomFichier = sys.argv[1] # Path de l'exemplaire
options = sys.argv[2:]

# Lecture du fichier source
fichier = open(nomFichier,'r')
nCentreInterets = int(fichier.readline())
matriceAdjacente = [None]*nCentreInterets
niveauAppreciation = []

for i in range(nCentreInterets):
    line1 = fichier.readline().replace('\t\n', '')
    matriceAdjacente[i] = line1.split('\t')

temps = int(fichier.readline())

for i in range(nCentreInterets):
    niveauAppreciation.append(fichier.readline().split('\t'))
   # niveauAppreciation[i] = line.split('\t')

def printMatrice(matrice, N):
    for i in range(N):
        line = ''
        for j in range(N):
            line += str(matrice[i][j]) + '\t'
        print(line)
print(niveauAppreciation)
#printMatrice(matriceAdjacente,nCentreInterets)