#!/bin/bash
set -euo pipefail
trap "echo 'Script failed'" ERR
IFS=$'\n\t'

i=0

while ((i<100))
do
    {
        python FPI_nP.py;
        # python FPI_nP_path.py;
        cp png/nP.png  png/nP-"$i".png
    }
    ((i=i+1))
done
