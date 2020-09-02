#!/bin/bash

log='games_nP.log'
echo '' > "$log"

i="0"

while ((i<1000))
do
    {
        echo 'round' "$i"' ----------------------------------------------------------------';
        python FPI_nP_path.py;
        mv png/nP-path.png png/nP-path-"$i".png
        # python FPI_nP.py;
        # mv png/nP.png png/nP-"$i".png
    } >> "$log"
    ((i=i+1))
done
