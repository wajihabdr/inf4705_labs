import sys
import math
from collections import deque, namedtuple, defaultdict

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

#Algo Dijkstra

class Graph :
    def __init__(self, noeuds = []):
        self.noeuds = set()
        self.arretes = defaultdict(list)
        self.temps = {}

    def ajouterNoeud(self, *noeud):
        [self.noeuds.add(n) for n in noeud]
    
    def ajouterArretes(self, depart, arrivee, temps):
        self.arretes[depart].append(arrivee)
        self.temps[(depart, arrivee)] = temps
    
    def printGraph(self):
        print(self.temps)
    
    def solution(self,graph, debut):
        visitees = {debut : 0}
        chemin = {}
        noeuds = set(graph.noeuds)
        print(graph.noeuds)

        while noeuds:
            noeudMinimal = None
            for noeud in range(noeuds): # integrer le temps max
                if noeud in visitees:
                    if noeudMinimal is None:
                        noeudMinimal = noeud
                    elif visitees[noeud] < visitees[noeudMinimal]: #ici on consideres le temps, à changer par ratio temps/appreciation et choisir celui avec le + grd ratio
                        noeudMinimal = noeud
            
            if noeudMinimal is None:
                break
            
            noeuds.remove(noeudMinimal)
            tempsActuel = visitees[noeudMinimal]

            for arrete in graph.arretes[noeudMinimal]:
                temps = tempsActuel + graph.temps[(noeudMinimal, arrete)]
                if arrete not in visitees or temps < tempsMax:
                    visitees[arrete] = temps
                    chemin[arrete] = noeudMinimal

        return visitees, chemin

tabNoeuds = []
for item in range(nCentreInterets):
    tabNoeuds.append(item)

graph = Graph(noeuds = tabNoeuds)

N = len(matriceAdjacente)

for noeud in range(N):
    for voisin in range(N):
        graph.ajouterArretes(noeud, voisin, matriceAdjacente[noeud][voisin])

# graph.printGraph()
print(graph.solution(graph,1))


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
