import numpy as np
import utils
import importlib
from FPI_2P import FPI_2P_Stgy

settings = importlib.import_module('games.3x3_PT_init_with_FP')
rows, cols = settings.payoff_matrix_row.shape

# algorithm settings
rate = 10 ** -5
iters = 2 * 10 ** 5


import matplotlib.pyplot as plt
for _ in range(5):
    # str_row_init = utils.randomize_mixed_strategy(rows)
    # str_col_init = utils.randomize_mixed_strategy(cols)
    devi = 0.00001
    str_row_init = utils.pick_a_neighour(settings.str_row_init, devi=devi)
    str_col_init = utils.pick_a_neighour(settings.str_col_init, devi=devi)
    print('pick a neighbour close to eqpt:', str_row_init, str_col_init)
    fpi = FPI_2P_Stgy([str_row_init, str_col_init], [settings.payoff_matrix_row, settings.payoff_matrix_col])
    fpi.converge(rate, iters)
    FPI_2P_Stgy.display_eqpt(fpi.eqpt())
    row_x_a, row_y_a = utils.barycentric_to_cartesian(np.array(fpi.get_stats()['str_row_l']))
    col_x_a, col_y_a = utils.barycentric_to_cartesian(np.array(fpi.get_stats()['str_col_l']))
    plt.plot(row_x_a, row_y_a, color='red', alpha=.5)
    plt.plot(col_x_a, col_y_a, color='blue', alpha=.5)
    # plt.axvline(row_x_a[-1], color='red', linestyle='dotted', alpha=.3, zorder=-1)
    # plt.axhline(row_y_a[-1], color='red', linestyle='dotted', alpha=.3, zorder=-1)
    # plt.axvline(col_x_a[-1], color='blue', linestyle='dotted', alpha=.3, zorder=-1)
    # plt.axhline(col_y_a[-1], color='blue', linestyle='dotted', alpha=.3, zorder=-1)

import matplotlib.patches as mpatches
ax = plt.gca()
triangle = mpatches.Polygon(np.array([[0, 0], [np.sqrt(2) / 2, np.sqrt(6) / 2], [np.sqrt(2), 0]]), fc="gray", alpha=.2)
ax.add_artist(triangle)
plt.axis('scaled')
plt.xlim(0, np.sqrt(2))
plt.ylim(0, np.sqrt(6) / 2)
plt.tight_layout()
plt.savefig('tunnel_repeller.png')
plt.show()
