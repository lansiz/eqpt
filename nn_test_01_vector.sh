#!/bin/sh

echo '' > nn_test_01.log
transforms="vector"
pfs="12 15 30 32 80 81 16 17 18"
for t in $transforms; do
    for f in $pfs; do
        python nn_test_01.py -t $t -f $f -i 10 >> nn_test_01.log 2>&1 &
    done
done

