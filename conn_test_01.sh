#!/bin/sh

echo '' > conn_test_01.log
transforms="step target converge uniform between"
pfs="12 15 30 32 80 81 16 17 18"
for t in $transforms; do
    for f in $pfs; do
        python conn_test_01.py -t $t -f $f >> conn_test_01.log 2>&1 &
    done
done

