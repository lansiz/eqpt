#!/bin/bash
set -euo pipefail
trap "echo 'Script failed'" ERR
IFS=$'\n\t'

i=0

while ((i<100))
do
    {
        python FPI_nP.py;
        cp png/nP.png  png/np_"$i".png
    }
    ((i=i+1))
done
