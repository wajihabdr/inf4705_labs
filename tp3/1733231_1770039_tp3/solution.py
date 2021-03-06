import sys
import math
import atexit   
import time
import threading
from collections import defaultdict

nomFichier = sys.argv[1]  # Path de l'exemplaire
options = sys.argv[2:]

# Lecture du fichier source
fichier = open(nomFichier, 'r')
nCentreInterets = int(fichier.readline())
matriceAdjacente = [None] * nCentreInterets
niveauAppreciation = [None] * nCentreInterets

for i in range(nCentreInterets):
    line1 = fichier.readline().replace(' \n', '')
    matriceAdjacente[i] = line1.split(' ')

tempsMax = int(fichier.readline())

niveauAppreciation = fichier.readline().replace(' \n', '').split(' ')

# Class Parcours
class Parcours:
    def __init__(self):
        self.tempsParcouru = 0
        self.noeuds = [0]

    def getTempsParcouru(self):
        return self.tempsParcouru

    def getNoeuds(self):
        return self.noeuds

    def getLastNoeud(self):
        return self.noeuds[len(self.noeuds)-1]

    def ajouterNoeud(self, noeud, temps):
        self.noeuds.append(noeud)
        self.tempsParcouru += temps

    def printParcours(self):
        line = ''
        for i in range(len(self.noeuds)):
            line += str(self.noeuds[i]) + ' '
        if len(self.noeuds) > 1 and self.noeuds[len(self.noeuds)-1] != 0:
            line += '0'
        print(line)

# Class Graph
class Graph:
    def __init__(self, noeuds=[]):
        self.noeuds = set()
        self.arretes = defaultdict(list)
        self.temps = {}
        self.ratio = {}

    def ajouterArretes(self, depart, arrivee, temps):
        self.arretes[depart].append(arrivee)
        self.temps[(depart, arrivee)] = int(temps)
        self.ratio[(depart, arrivee)] = self.safe_div(int(niveauAppreciation[arrivee]), int(temps))

    def safe_div(self, x, y):
        if y == 0:
            return 0
        return x / y

    def meilleurChemin(self, Parcours, tabNoeuds, tempsMax):
        depart = parcours.getLastNoeud()

        cheminSelection = 0
        for i in range(len(tabNoeuds)):
            arrivee = tabNoeuds[i]
            if (Parcours.getTempsParcouru() + self.temps[(depart, arrivee)] + self.temps[(arrivee, 0)]) <= tempsMax:
                if self.ratio[(depart, cheminSelection)] < self.ratio[(depart, arrivee)]:
                    cheminSelection = arrivee

        if cheminSelection in tabNoeuds:
            tabNoeuds.remove(cheminSelection)
            parcours.ajouterNoeud(cheminSelection, self.temps[(depart, cheminSelection)])
        return parcours

    def getAppreciation(self, noeud):
        return niveauAppreciation[noeud]

    def getTemps(self, depart, arrivee):
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
parcours = Parcours()

#Code pour le thread source : https://stackoverflow.com/questions/11758555/python-do-something-until-keypress-or-timeout
def parcoursGraphe():
    parcours = Parcours()
    parcours.printParcours()
    T0 = time.clock()
    while (time.clock() - T0) < 60 and not e.isSet(): 
        parcours = graph.meilleurChemin(parcours, tabNoeuds, tempsMax)
        if '-p' in options:
            parcours.printParcours()
        time.sleep(1)

thread = threading.Thread(target=parcoursGraphe, args=())
e = threading.Event()
thread.start()
while thread.isAlive():
    try: 
        time.sleep(1)
        input()
    except KeyboardInterrupt: 
        e.set()
        thread.join()

