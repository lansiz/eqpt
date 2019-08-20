import contraction
import utils
import argparse
import importlib
import numpy as np

parser = argparse.ArgumentParser(description='FPI contraction')
parser.add_argument(
    'settings', metavar='SETTING_PY_FILE_BASENAME', type=str, nargs=1,
    help='game setting .py file in `games` subdir: initial strategies, payoff matrices...')
args = parser.parse_args()
setting_file = args.settings[0]
settings = importlib.import_module('games.' + setting_file)

rows, cols = settings.payoff_matrix_row.shape
strategies_profile = (utils.randomize_mixed_strategy(rows), utils.randomize_mixed_strategy(cols))
distance_function = contraction.distance_function_1
payoff_matrices = (settings.payoff_matrix_row, settings.payoff_matrix_col)
rate = settings.rate
iters = settings.iters

distance_l = []
for i in range(iters):
    strategies_profile_new = contraction.FPI_transformation_once(
        strategies_profile, payoff_matrices, rate)
    distance = distance_function(strategies_profile, strategies_profile_new)
    distance_l.append(np.log(distance))
    strategies_profile = strategies_profile_new

# plotting
import matplotlib.pyplot as plt
distance_a = np.array(distance_l)
plt.plot(distance_a)
plt.savefig('contraction.png')
plt.show()
