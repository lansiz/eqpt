import sys
import numpy as np
import argparse
import importlib
import matplotlib.pyplot as plt
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

if settings.str_row_init.shape[0] != 3 or settings.str_col_init.shape[0] != 3:
    print('the game must be 3x3 for plotting on simplex.')
    sys.exit(1)


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
# row_x_a, row_y_a = utils.barycentric_to_cartesian(np.array(stats['str_row_l']))
# col_x_a, col_y_a = utils.barycentric_to_cartesian(np.array(stats['str_col_l']))
str_path_row = np.array(stats['str_row_l'])
str_path_col = np.array(stats['str_col_l'])

# Attaching 3D axis to the figure
fig = plt.figure()
ax = fig.add_subplot(projection="3d")

# Setting the axes properties
ax.set_xlim3d([0.0, 1.0])
ax.set_xlabel('pure stgy 1')
ax.set_ylim3d([0.0, 1.0])
ax.set_ylabel('pure stgy 2')
ax.set_zlim3d([0.0, 1.0])
ax.set_zlabel('pure stgy 3')
# ax.set_title('Geometrical Regret Matching')

# plot the probability simplex
ax.plot((1, 0), (0, 1), (0, 0), linestyle='dotted', color='grey')
ax.plot((1, 0), (0, 0), (0, 1), linestyle='dotted', color='grey')
ax.plot((0, 0), (1, 0), (0, 1), linestyle='dotted', color='grey')

ax.plot(str_path_row[:, 0], str_path_row[:, 1], zs=str_path_row[:, 2], color='red')
ax.plot(str_path_col[:, 0], str_path_col[:, 1], zs=str_path_col[:, 2], color='blue')

plt.show()
# line_ani.save('./animation.mp4')
