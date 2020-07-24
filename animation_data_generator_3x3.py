import sys
import numpy as np
import argparse
import importlib
import utils
from FPI_2P import FPI_2P_Animation

parser = argparse.ArgumentParser(description='EQPT ANIMATION DATA GENERATOR')
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

if settings.str_row_init.shape[0] != 3 or settings.str_col_init.shape[0] != 3:
    print('the game must be 3x3 for plotting on simplex.')
    sys.exit(1)


fpi = FPI_2P_Animation(
    [settings.str_row_init, settings.str_col_init],
    [settings.payoff_matrix_row, settings.payoff_matrix_col])
if display_game:
    fpi.print_game()
fpi.converge(r, iters)
FPI_2P_Animation.display_eqpt(fpi.eqpt())
if use_LH:
    fpi.lemke_howson()

stats = fpi.get_stats()
data = [
    (np.array(stats['str_row_l']).transpose(), np.array(stats['vgs_row_l']).round(2)),
    (np.array(stats['str_col_l']).transpose(), np.array(stats['vgs_col_l']).round(2))]
utils.write_pickle(data, 'animation_data.pkl')
