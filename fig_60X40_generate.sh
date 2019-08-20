#!/bin/bash
set -euo pipefail
trap "echo 'Script failed'" ERR
IFS=$'\n\t'

i=0

while ((i<100))
do
    {
        python fig_path_PCA.py fig_60X40_conv;
        convert 60X40-conv-temp.png -crop 790x705+0+50 png/"$i".png;
    }
    ((i=i+1))
done
