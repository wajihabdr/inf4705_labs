#!/bin/bash:

algo="glouton"
directory="10-10"

for file in $(ls "../jeux_de_donnees/$directory"); do
    echo "Go ----> ${file}"
    t=$(./tp.sh -a $algo -e ../jeux_de_donnees/$directory/$file -test)
    echo $t >> ./resultats/${directory%%.*}.csv
done

read -p "Appuyer sur une touche pour continuer ..."
echo Fin
