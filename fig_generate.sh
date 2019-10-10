#!/bin/bash
set -euo pipefail
trap "echo 'Script failed'" ERR
IFS=$'\n\t'

python FPI_nP.py
exit 0

python fig_path_3x3.py fig_3X3_1eq1sp
python fig_path_3x3.py fig_3X3_1eq2sp
python fig_path_3x3.py fig_3X3_2eq2sp
python fig_path_3x3.py fig_3X3_1eq3sp

python fig_VGS_vs_rate.py
python fig_VGS_vs_scale.py

python fig_VGS.py fig_3X3_1eq1sp
python fig_VGS.py fig_3X3_1eq2sp
python fig_VGS.py fig_3X3_2eq2sp
python fig_VGS.py fig_3X3_1eq3sp

python fig_path_3x3.py fig_3X3_1eq2sp_attractor
python fig_path_3x3.py fig_3X3_2eq2sp_attractor
python fig_path_3x3.py fig_3X3_1eq3sp_repellor



python fig_metric.py fig_3X3_1eq1sp
python fig_metric.py fig_3X3_1eq2sp
python fig_metric.py fig_3X3_2eq2sp
python fig_metric.py fig_3X3_1eq3sp



python fig_path_PCA.py fig_60X40_conv
