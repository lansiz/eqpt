#!/bin/bash
set -euo pipefail
trap "echo 'Script failed'" ERR
IFS=$'\n\t'

log='games_2P.log'
echo '' > "$log"

i="0"

while ((i<1000))
do
    {
        python approximate_an_eqpt.py $1;
        echo '-------------------------------------------------------------------------------------------------------';
        echo;
    } >> "$log"
    ((i=i+1))
done
