import argparse
import numpy as np
import utils
import importlib
from FPI_2P import FPI_2P_Stgy

parser = argparse.ArgumentParser(description='tunnel on 3x3 game')
parser.add_argument(
    'settings', metavar='SETTING_PY_FILE_BASENAME', type=str, nargs=1,
    help='game setting .py file in `games` subdir: initial strategies, payoff matrices...')
args = parser.parse_args()
setting_file = args.settings[0]
settings = importlib.import_module('games.' + setting_file)

rows, cols = settings.payoff_matrix_row.shape

# algorithm settings
rate = 10 ** -5
iters = 2 * 10 ** 5


import matplotlib.pyplot as plt
for _ in range(10):
    str_row_init = utils.randomize_mixed_strategy(rows)
    str_col_init = utils.randomize_mixed_strategy(cols)
    fpi = FPI_2P_Stgy([str_row_init, str_col_init], [settings.payoff_matrix_row, settings.payoff_matrix_col])
    fpi.converge(rate, iters)
    eqpt = fpi.eqpt()
    FPI_2P_Stgy.display_eqpt(eqpt)
    row_x_a, row_y_a = utils.barycentric_to_cartesian(np.array(fpi.get_stats()['str_row_l']))
    col_x_a, col_y_a = utils.barycentric_to_cartesian(np.array(fpi.get_stats()['str_col_l']))
    plt.plot(row_x_a, row_y_a, color='red', alpha=.5)
    plt.plot(col_x_a, col_y_a, color='blue', alpha=.5)

import matplotlib.patches as mpatches
ax = plt.gca()
triangle = mpatches.Polygon(np.array([[0, 0], [np.sqrt(2) / 2, np.sqrt(6) / 2], [np.sqrt(2), 0]]), fc="gray", alpha=.2)
ax.add_artist(triangle)
plt.axis('scaled')
plt.xlim(0, np.sqrt(2))
plt.ylim(0, np.sqrt(6) / 2)
plt.tight_layout()
plt.savefig('tunnel_3x3.png')
plt.show()
