#!/bin/bash

OPTIONS=""
while [[ $# -gt 0 ]]
do
key="$1"

case $key in
    -e)
    EX_PATH=$2
    shift
    ;;
    -p)
    OPTIONS="${OPTIONS}${1} "
    ;;
    *)
        echo "Argument inconnu: ${1}"
        exit
    ;;
esac
shift
done

python3 solution.py "$EX_PATH" $OPTIONS
read -p "Appuyer sur une touche pour fermer ..."
