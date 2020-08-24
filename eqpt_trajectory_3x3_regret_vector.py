import sys
import numpy as np
import argparse
import importlib
import utils
from FPI_2P import FPI_2P_Regret_Vector

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

if settings.str_row_init.shape[0] != 3 or settings.str_col_init.shape[0] != 3:
    print('the game must be 3x3 for plotting on simplex.')
    sys.exit(1)


fpi = FPI_2P_Regret_Vector(
    [settings.str_row_init, settings.str_col_init],
    [settings.payoff_matrix_row, settings.payoff_matrix_col])
if display_game:
    fpi.print_game()
fpi.converge(r, iters)
FPI_2P_Regret_Vector.display_eqpt(fpi.eqpt())
if use_LH:
    fpi.lemke_howson()

stats = fpi.get_stats()
# essential: transform point in 2-simplex to 2-D plane
row_x_a, row_y_a = utils.barycentric_to_cartesian(np.array(stats['str_row_l']))
col_x_a, col_y_a = utils.barycentric_to_cartesian(np.array(stats['str_col_l']))
temp_a = np.array(stats['vgv_row_l'])
temp_a = np.apply_along_axis(lambda x: x / x.sum(), 1, temp_a)
row_rv_x_a, row_rv_y_a = utils.barycentric_to_cartesian(temp_a)
temp_a = np.array(stats['vgv_col_l'])
temp_a = np.apply_along_axis(lambda x: x / x.sum(), 1, temp_a)
col_rv_x_a, col_rv_y_a = utils.barycentric_to_cartesian(temp_a)

import matplotlib.pyplot as plt
plt.plot(row_x_a, row_y_a, color='red', alpha=.5)
plt.plot(row_rv_x_a, row_rv_y_a, color='red', linestyle='--', alpha=.5)
plt.plot(col_x_a, col_y_a, color='blue', alpha=.5)
plt.plot(col_rv_x_a, col_rv_y_a, color='blue', linestyle='--', alpha=.5)
plt.axvline(row_x_a[-1], color='red', linestyle='dotted', alpha=.3, zorder=-1)
plt.axhline(row_y_a[-1], color='red', linestyle='dotted', alpha=.3, zorder=-1)
plt.axvline(col_x_a[-1], color='blue', linestyle='dotted', alpha=.3, zorder=-1)
plt.axhline(col_y_a[-1], color='blue', linestyle='dotted', alpha=.3, zorder=-1)
import matplotlib.patches as mpatches
ax = plt.gca()
triangle = mpatches.Polygon(np.array([[0, 0], [np.sqrt(2) / 2, np.sqrt(6) / 2], [np.sqrt(2), 0]]), fc="gray", alpha=.2)
ax.add_artist(triangle)
plt.axis('scaled')
# plt.xlim(0, np.sqrt(2))
# plt.ylim(0, np.sqrt(6) / 2)
plt.xlim(-.05, np.sqrt(2) + .05)
plt.ylim(-.05, np.sqrt(6) / 2 + .05)
plt.tight_layout()
plt.savefig('trajectory_3x3.png')
plt.show()
