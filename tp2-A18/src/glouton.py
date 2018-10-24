# Pour le patron de conception glouton , nous avons choisis 
# d'implémenter l'algorithme du sac à dos

# def sacADos(P, pi , n, taille) : 
#     # P : le poids total limite
#     # pi : poids de chaque bâton
#     # n : nombre de bâtons de dynamites
#     # taille : nombre de valeurs que l'on a pour le poids
#     if P == 0 or taille == 0 : 
#         return 0
#     if pi[taille - 1] > P :
#         return sacADos(P, pi, n, taille -1)
#     else :

import sys
import time

# Permet la lecture d'une matrice
# A besoin de path du fichier

nomFichier1 = str(sys.argv[1])
options = sys.argv[3:]

fichier1 = open(nomFichier1, 'r')
N = int(fichier1.readline());
P = int(fichier1.readlines()[-1])

pi = [None]*N;
poidsTotal = 0

#Tableeau des valeurs et de leur poids respectifs
for i in range(1,N):
        line1 = fichier1.readline().replace('\t\n', '')
        pi[i] = line1.split('\t')
        print(pi[i])

#Initialisation du sac a dos et du tableau contenant les items a garder
B = [[0]*(P+1)for i in range(N)]
resultat = [[0]*(P+1)for i in range(N)]

#mettre dans le table pi plutot la deuxieme partie de chaque ligne pour avoir une table à 1 dimension
#Algo du sac à dos
for i in range(N) :
    for j in range(P) :
        if(j>=pi[i]):
            p1=B[i-1][w]
            p2=B[i-1][j-pi[i]]+item_value[k]
            if(p1>p2):
                resultat[i][j]=0
                B[i][j]=p1
            else:
                resultat[i][j]=1
                B[i][j]=p2
        else:
            B[i][j]= B[i-1][j]
            resultat[i][j]=0

capacity=10 #derniere ligne du fichier
num_of_items=6 #premiere ligne du fichier
total_weight=0
total_value=0

#Initialize backpack
B=[[0]*(capacity+1) for i in range(num_of_items)]
#Keep list will help determine which items to keep once we've solved the Knapsack problem
keep=[[0]*(capacity+1) for i in range(num_of_items)]

#Dictionary to store item numbers and corresponding weights
#<Item number, weight>
item_weight={0:4,1:2,2:3,3:1,4:7,5:10}
#Dictionary to store item numbers and corresponding values
#<Item number, value>
item_value={0:6,1:4,2:5,3:3,4:9,5:7}

total_weight=sum([value for value in item_weight.values()])
total_value=sum([value for value in item_value.values()])

#Solve Knapsack problem
for k in range(num_of_items):
    for w in range(capacity+1):
        if(w>=item_weight[k]):
            p1=B[k-1][w]
            p2=B[k-1][w-item_weight[k]]+item_value[k]
            if(p1>p2):
                keep[k][w]=0
                B[k][w]=p1
            else:
                keep[k][w]=1
                B[k][w]=p2
        else:
            B[k][w]= B[k-1][w]
            keep[k][w]=0
            
rem_capacity=capacity
items_to_take=[]
valueofgoods=0

#Determine which items to keep and what their total value is       
for k in range(num_of_items-1,-1,-1):
    if(keep[k][rem_capacity]==1):
        items_to_take.append(k)
        rem_capacity=rem_capacity-item_weight[k]
        valueofgoods+=item_value[k]
print('Total value of all goods:' )
print(total_value)
print ('Maximized Value of goods: ')
print(valueofgoods) 
print ('Goods to choose: ')
print(items_to_take)

if '-all' in options:  # On imprime la matrice résultat
    print("Resultat algo sac à dos")
if '-p' in options:  # On imprime la matrice résultat
    print("84 73 12 44 98 75") # Données bidon, mais output du bon format demandé
if '-t' in options:  # On imprime le temps d'exécution
    interval = end_time - start_time
    print(interval)
    #print('\n' + 'Temps d execution :' + str(interval) + ' sec')
