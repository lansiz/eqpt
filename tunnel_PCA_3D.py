import numpy as np
import argparse
from sklearn.decomposition import PCA
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
iters = 1 * 10 ** 5

stats_l = []
for _ in range(10):
    str_row_init = utils.randomize_mixed_strategy(rows)
    str_col_init = utils.randomize_mixed_strategy(cols)
    fpi = FPI_2P_Stgy(
        [str_row_init, str_col_init],
        [settings.payoff_matrix_row, settings.payoff_matrix_col])
    fpi.converge(rate, iters)
    eqpt = fpi.eqpt()
    FPI_2P_Stgy.display_eqpt(eqpt)
    stats_l.append((fpi.get_stats()['str_row_l'], fpi.get_stats()['str_col_l']))
    print(eqpt)

# combine all data into one to fit PCA, then transform them to 3D
str_row_combined_l = str_col_combined_l = []
for item in stats_l:
    str_row_combined_l += item[0]
    str_col_combined_l += item[1]
pca_row = PCA(n_components=3)
pca_col = PCA(n_components=3)
pca_row.fit(np.array(str_row_combined_l))
pca_col.fit(np.array(str_col_combined_l))

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.gca(projection='3d')
for item in stats_l:
    str_row_a = pca_row.transform(np.array(item[0]))
    str_col_a = pca_col.transform(np.array(item[1]))

    ax.plot(str_row_a[:, 0], str_row_a[:, 1], zs=str_row_a[:, 2], zdir='z', color='red', alpha=.5)
    ax.plot(str_col_a[:, 0], str_col_a[:, 1], zs=str_col_a[:, 2], zdir='z', color='blue', alpha=.5)

plt.tight_layout()
plt.savefig('tunnel_PCA_3D.png')
plt.show()
