import sys
import math
from collections import deque, namedtuple, defaultdict

nomFichier = sys.argv[1]  # Path de l'exemplaire
options = sys.argv[2:]

# Lecture du fichier source
fichier = open(nomFichier, 'r')
nCentreInterets = int(fichier.readline())
matriceAdjacente = [None] * nCentreInterets
niveauAppreciation = [None]*nCentreInterets

for i in range(nCentreInterets):
    line1 = fichier.readline().replace(' \n', '')
    matriceAdjacente[i] = line1.split(' ')

tempsMax = int(fichier.readline())

niveauAppreciation = fichier.readline().replace(' \n', '').split(' ')

# Class Graph

class Graph:
    def __init__(self, noeuds=[]):
        self.noeuds = set()
        self.arretes = defaultdict(list)
        self.temps = {}
        self.ratio = {}

    def ajouterNoeud(self, *noeud):
        [self.noeuds.add(n) for n in noeud]

    def ajouterArretes(self, depart, arrivee, temps):
        self.arretes[depart].append(arrivee)
        self.temps[(depart, arrivee)] = int(temps)
        self.ratio[(depart, arrivee)] = self.safe_div(int(niveauAppreciation[arrivee]), int(temps))

    def printGraph(self):
        print(self.temps)

    def safe_div(self, x, y):
        if y == 0:
            return 0
        return x / y

    def meilleurChemin(self, parcours, tabNoeuds, tempsMax):
        tempsParcouru = sum(parcours)
        depart = parcours[len(parcours)-1]
        print("somme list : " + str(tempsParcouru))

        cheminSelection = 0
        for i in range(len(tabNoeuds)):
            arrivee = tabNoeuds[i]
            if (tempsParcouru + self.temps[(depart, arrivee)] + self.temps[(arrivee, 0)]) < tempsMax:
                if self.ratio[(depart, cheminSelection)] < self.ratio[(depart, arrivee)]:
                    cheminSelection = arrivee
            else:
                print('END !!')

        tabNoeuds.remove(cheminSelection)
        return cheminSelection

    def getAppreciation(self, noeud):
        return niveauAppreciation[noeud]

    def getTemp(self, depart, arrivee):
        return self.temps[(depart, arrivee)]

    def getRatio(self, depart, arrivee):
        return self.ratio[(depart, arrivee)]

# Instanciation de la class graph

tabNoeuds = []
for i in range(nCentreInterets):
    tabNoeuds.append(i)

graph = Graph(noeuds=tabNoeuds)

N = len(matriceAdjacente)

for noeud in range(N):
    for voisin in range(N):
        graph.ajouterArretes(noeud, voisin, matriceAdjacente[noeud][voisin])

# Debut Algo
parcours = [0]
tabNoeuds.remove(0)

for index in range(15):
    parcours.append(graph.meilleurChemin(parcours, tabNoeuds, tempsMax))
    print(tabNoeuds)
    print(parcours)

# End

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
