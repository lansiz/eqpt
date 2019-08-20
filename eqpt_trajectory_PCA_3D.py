import numpy as np
import argparse
import importlib
import utils
from FPI_2P import FPI_2P_Stgy

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

fpi = FPI_2P_Stgy(
    [settings.str_row_init, settings.str_col_init],
    [settings.payoff_matrix_row, settings.payoff_matrix_col])
if display_game:
    fpi.print_game()
fpi.converge(r, iters)
FPI_2P_Stgy.display_eqpt(fpi.eqpt())
if use_LH:
    fpi.lemke_howson()

stats = fpi.get_stats()
# transform the trajectory to 2-D plane with PCA
print('*** transform trategy vectors to 3-D with PCA ...')
str_row_a = utils.pca_3d(np.array(stats['str_row_l']))
str_col_a = utils.pca_3d(np.array(stats['str_col_l']))

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.gca(projection='3d')
# ax.plot(x, y, zs=zs, zdir='z', label='curve in (x,y)')
ax.plot([i[0] for i in str_row_a], [i[1] for i in str_row_a], zs=[i[2] for i in str_row_a], zdir='z', color='red', alpha=.5)
end = str_row_a[-1]
ax.scatter([end[0]], [end[1]], s=16, zs=[end[2]], zdir='z', color='red', alpha=.5)
# plt.axvline(str_row_a[-1][0], color='red', linestyle='dotted', alpha=.3, zorder=-1)
# plt.axhline(str_row_a[-1][1], color='red', linestyle='dotted', alpha=.3, zorder=-1)
ax.plot([i[0] for i in str_col_a], [i[1] for i in str_col_a], zs=[i[2] for i in str_col_a], zdir='z', color='blue', alpha=.5)
end = str_col_a[-1]
ax.scatter([end[0]], [end[1]], s=16, zs=[end[2]], zdir='z', color='blue', alpha=.5)
# plt.axvline(str_col_a[-1][0], color='blue', linestyle='dotted', alpha=.3, zorder=-1)
# plt.axhline(str_col_a[-1][1], color='blue', linestyle='dotted', alpha=.3, zorder=-1)
# plt.axis('scaled')
plt.tight_layout()
plt.savefig('trajectory_PCA_3D.png')
plt.show()
