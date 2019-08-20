# import sys
# import numpy as np
import argparse
import importlib
# import utils
# from FPI_2P import FPI_2P_Stgy
# import matplotlib as mpl

parser = argparse.ArgumentParser(description='degenerate test')
parser.add_argument(
    'settings', metavar='SETTING_PY_FILE_BASENAME', type=str, nargs='+',
    help='game setting .py file in `games` subdir: initial strategies, payoff matrices...')
args = parser.parse_args()
setting_file = args.settings[0]
settings = importlib.import_module('games.' + setting_file)

for (eqpt_row, eqpt_col) in settings.eqpts:
    print(settings.payoff_matrix_row.dot(eqpt_col.T).tolist(), settings.payoff_matrix_col.T.dot(eqpt_row.T).tolist())
