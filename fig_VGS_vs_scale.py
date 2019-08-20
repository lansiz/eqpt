import numpy as np
import utils
import multiprocessing
import importlib
from FPI_2P import FPI_2P

settings = importlib.import_module('games.fig_3X3_1eq3sp')

# algorithm settings
rate = 10 ** -5
iters = 10 ** 5


def approximation(x):
    print('-' * 30)
    print('payoff scale:', x)
    fpi = FPI_2P(
        [settings.str_row_init_l[0], settings.str_col_init_l[0]],
        [settings.payoff_matrix_row * x, settings.payoff_matrix_col * x])
    fpi.converge(rate, iters)
    eqpt = fpi.eqpt()
    print(eqpt)
    return eqpt


np.random.seed()
worker_pool = multiprocessing.Pool(processes=8)
xs = np.arange(-20, 21)
xs_e = np.apply_along_axis(lambda x: np.power(np.e, x), 0, xs)
results_l = [worker_pool.apply_async(approximation, (x,)).get() for x in xs_e]

import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1, figsize=utils.xy_16X9)
vgs_row = np.array([i[2].sum() for i in results_l])
vgs_col = np.array([i[3].sum() for i in results_l])
vgs_row /= xs_e
vgs_col /= xs_e
ax.plot(xs, np.log(vgs_row), marker='.', color='red', alpha=.6, zorder=2)
ax.plot(xs, np.log(vgs_col), marker='.', color='blue', alpha=.6, zorder=2)
ax.set_xlabel('ln(payoff scale)', fontsize=utils.label_size)
ax.set_ylabel('ln(VGS)', fontsize=utils.label_size)
# ax.tick_params(labelsize=8)
plt.grid(True)
plt.tight_layout()
plt.savefig('vgs-vs-scale.png', bbox_inches='tight')
# plt.show()
