import sys

# Permet la lecture d'une matrice
# A besoin de path du fichier
path = './exemple/exemplaires/serie1/'
fileName = path + 'ex_2.1'

fichier = open(fileName, 'r')
N = int(fichier.readline())

print('N = ' + str(N))

matrice = [None]*(2**N)

for i in range(2**N):
    line = fichier.readline().replace('\t\n', '')
    matrice[i] = line.split('\t')

print('Ma matrice \n')
print(matrice)

# Algo Conventionnel
result = [[0 for x in range(2**N)] for y in range(2**N)]

for i in range(2**N):
    for j in range(2**N):
        for k in range(2**N):
            result[i][j] += int(matrice[i][k]) * int(matrice[k][j])
print('\n' + 'Result :')
print(result)
