#!/bin/bash:

algo="glouton"

for directory in $(ls "../jeux_de_donnees"); do
    echo "Go ----> ${directory}"
    echo "--  ${directory} --" >> ./resultats/${algo}.csv
    for file in $(ls "../jeux_de_donnees/$directory"); do
        t=$(./tp.sh -a $algo -e ../jeux_de_donnees/$directory/$file -test)
        echo $t >> ./resultats/${algo}.csv
    done
done

echo Fin
