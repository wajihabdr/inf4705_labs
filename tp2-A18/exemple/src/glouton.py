import sys

ex_path = sys.argv[1] # Path de l'exemplaire

# Lecture du fichier source
fichier = open(ex_path,'r')
taille = int(fichier.readline())
batons = []
for i in range(taille):
    ligne = fichier.readline().replace('\t\n', '')
    data = ligne.split('\t')
    batons.append(int(data[1]))
poidTotal = int(fichier.readline())

options = sys.argv[2:]
if '-p' in options: # On imprime la solution
    print("84 73 12 44 98 75") # Données bidon, mais output du bon format demandé
if '-t' in options: # On imprime le temps d'exécution
    print("4.1347628746") # Données bidon, mais output du bon format demandé
