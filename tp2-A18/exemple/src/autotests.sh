#!/bin/bash

# Ce script automatise l'exécution d'une batterie de tests
# Notez la structure des fichiers et répertoires pour cet exemple

for algo in {"glouton","progdyn1","progdyn2"}; do
   # counter=4
    for ex1 in $(ls "jeux_de_donnees/"); do
        # for ex2 in $(ls "exemplaires/$serie" | tail -n $counter); do
        t=$(./tp.sh -a $algo -e jeux_de_donnees/$ex1 -t)
        echo $t >> ./resultats/${algo}.csv
        done
        # ((counter--))
    done
    echo "./resultats/${algo}.csv"
done
echo Fin