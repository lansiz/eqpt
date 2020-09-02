#!/bin/bash
set -euo pipefail
trap "echo 'Script failed'" ERR
IFS=$'\n\t'

log=$1
egrep 'OverallRegretSum' $1 | awk -F ' ' '{print $2}' > temp.csv
python -c '
import pandas as pd;
import matplotlib.pyplot as plt;
df = pd.read_csv("./temp.csv", header=None, delimiter=" ");
plt.hist(df[0], bins=100);
plt.show()'
