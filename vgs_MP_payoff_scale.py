import numpy as np
import argparse
import multiprocessing
import importlib
from FPI_2P import FPI_2P

parser = argparse.ArgumentParser(description='VGS vs. payoff scale')
parser.add_argument(
    'settings', metavar='SETTING_PY_FILE_BASENAME', type=str, nargs=1,
    help='game setting .py file in `games` subdir: initial strategies, payoff matrices...')
args = parser.parse_args()
setting_file = args.settings[0]
settings = importlib.import_module('games.' + setting_file)

# algorithm settings
rate = 10 ** -5
iters = 2 * 10 ** 5


def approximation(x):
    print('-' * 30)
    print('payoff scale:', x)
    fpi = FPI_2P([settings.str_row_init, settings.str_col_init], [settings.payoff_matrix_row * x, settings.payoff_matrix_col * x])
    fpi.converge(rate, iters)
    eqpt = fpi.eqpt()
    print(eqpt)
    return eqpt


np.random.seed()
worker_pool = multiprocessing.Pool(processes=8)
# xs = np.linspace(-10, 20, 40, endpoint=False)
xs = np.arange(-20, 21)
xs_e = np.apply_along_axis(lambda x: np.power(np.e, x), 0, xs)
results_l = [worker_pool.apply_async(approximation, (x,)).get() for x in xs_e]

import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1, figsize=(6, 2.5))
vgs_row = np.array([i[2].sum() for i in results_l])
vgs_row /= xs_e
vgs_col = np.array([i[3].sum() for i in results_l])
vgs_col /= xs_e
# ax.plot(xs, np.log(vgs_row + vgs_col), marker='.', color='green', linestyle='dotted', alpha=1, zorder=2)
ax.plot(xs, np.log(vgs_row), marker='.', color='red', alpha=1, zorder=2)
ax.plot(xs, np.log(vgs_col), marker='.', color='blue', alpha=1, zorder=2)
ax.set_xlabel('ln(payoff scale)')
ax.set_ylabel('ln(VGS)')
ax.tick_params(labelsize=8)
plt.grid(True)
plt.tight_layout()
plt.savefig('vgs_MP_payoff_scale.png')
plt.show()
