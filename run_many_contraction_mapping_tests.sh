#!/bin/bash
set -euo pipefail
# trap "echo 'Script failed'" ERR
IFS=$'\n\t'


logfile='contraction_mapping_verify.log'
echo > $logfile

i="0"

while [ $i -lt 1000 ]
do
    {
        python contraction_mapping_iterated.py;
        echo '-------------------------------------------------------------------------------------------------------';
        echo;
    } >> $logfile
    ((i=i+1))
done
