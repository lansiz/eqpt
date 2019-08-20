#!/bin/bash
set -euo pipefail
trap "echo 'Script failed'" ERR
IFS=$'\n\t'

i=0

while ((i<100))
do
    {
        python eqpt_trajectory_VGS.py 60x40
        cp png/trajectory_vgs.png png/trajectory_vgs_"$i".png
    }
    ((i=i+1))
done
