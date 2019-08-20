#!/bin/bash
set -euo pipefail
trap "echo 'Script failed'" ERR
IFS=$'\n\t'

log='games_6x4.log'
echo '' > "$log"

i="0"

while ((i<1000))
do
    {
        python approximate_a_eqpt.py 6x4;
        echo '-------------------------------------------------------------------------------------------------------';
        echo;
    } >> "$log"
    ((i=i+1))
done
