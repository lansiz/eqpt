import numpy as np
import argparse
import multiprocessing
import importlib
from FPI_2P import FPI_2P

parser = argparse.ArgumentParser(description='VGS vs. iterations')
parser.add_argument(
    'settings', metavar='SETTING_PY_FILE_BASENAME', type=str, nargs=1,
    help='game setting .py file in `games` subdir: initial strategies, payoff matrices...')
args = parser.parse_args()
setting_file = args.settings[0]
settings = importlib.import_module('games.' + setting_file)

# algorithm settings
rate = 10 ** -6
iters = 10 ** 5


def approximation(x):
    fpi = FPI_2P([settings.str_row_init, settings.str_col_init], [settings.payoff_matrix_row, settings.payoff_matrix_col])
    print('-' * 30)
    fpi.converge(rate, x)
    eqpt = fpi.eqpt()
    print(eqpt)
    return eqpt


np.random.seed()
worker_pool = multiprocessing.Pool(processes=8)
xs = np.linspace(10 ** 4, 100 * 10 ** 4, 50, endpoint=False)
results_l = [worker_pool.apply_async(approximation, (int(x),)).get() for x in xs]

import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1, figsize=(6, 2.5))
vgs_row = np.array([i[2].sum() for i in results_l])
vgs_col = np.array([i[3].sum() for i in results_l])
# ax.plot(xs, np.log(vgs_row + vgs_col), marker='.', color='green', linestyle='dotted', alpha=1, zorder=2)
ax.plot(xs, np.log(vgs_row), marker='.', color='red', alpha=1, zorder=2)
ax.plot(xs, np.log(vgs_col), marker='.', color='blue', alpha=1, zorder=2)
ax.set_xlabel('iterations')
ax.set_ylabel('ln(VGS)')
ax.tick_params(labelsize=8)
plt.grid(True)
plt.tight_layout()
plt.savefig('vgs_MP_iterations.png')
plt.show()
