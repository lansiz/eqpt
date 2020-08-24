import numpy as np
import argparse
import importlib
# import utils
from FPI_2P import FPI_2P_VGS

parser = argparse.ArgumentParser(description='FPI trajetory')
parser.add_argument(
    'settings', metavar='SETTING_PY_FILE_BASENAME', type=str, nargs=1,
    help='game setting .py file in `games` subdir: initial strategies, payoff matrices...')
args = parser.parse_args()
setting_file = args.settings[0]
settings = importlib.import_module('games.' + setting_file)


# algorithm settings
try:
    r = settings.rate
except AttributeError:
    r = 10 ** -5
try:
    iters = settings.iters
except AttributeError:
    iters = 10 ** 5
try:
    display_game = settings.display_game
except AttributeError:
    display_game = False
try:
    use_LH = settings.use_LH
except AttributeError:
    use_LH = False

fpi = FPI_2P_VGS(
    [settings.str_row_init, settings.str_col_init],
    [settings.payoff_matrix_row, settings.payoff_matrix_col])
if display_game:
    fpi.print_game()
fpi.converge(r, iters)
FPI_2P_VGS.display_eqpt(fpi.eqpt())
if use_LH:
    fpi.lemke_howson()

stats = fpi.get_stats()

import matplotlib.pyplot as plt
plt.plot(np.log(np.array(stats['vgs_row_l'])), color='red', alpha=.6)
plt.plot(np.log(np.array(stats['vgs_col_l'])), color='blue', alpha=.6)
plt.xlabel('iterations')
plt.ylabel('ln(regret sum)')
plt.grid(True)
plt.tight_layout()
plt.savefig('trajectory_vgs.png')
plt.show()
