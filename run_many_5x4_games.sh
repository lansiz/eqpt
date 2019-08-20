#!/bin/bash
set -euo pipefail
# trap "echo 'Script failed'" ERR
IFS=$'\n\t'

log='games_5x4.log'
echo '' > "$log"

i="0"

while ((i<1000))
do
    {
        python approximate_an_eqpt.py 5x4;
        echo '-------------------------------------------------------------------------------------------------------';
        echo;
    } >> "$log"
    ((i=i+1))
done
