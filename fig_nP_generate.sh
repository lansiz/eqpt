#!/bin/bash
set -euo pipefail
trap "echo 'Script failed'" ERR
IFS=$'\n\t'

i=0

while ((i<100))
do
    {
        python FPI_nP_path.py;
        cp _png/nP-path.png  png/nP-path-"$i".png
    }
    ((i=i+1))
done
