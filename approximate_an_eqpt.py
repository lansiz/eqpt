import argparse
import numpy as np
import importlib
from FPI_2P import FPI_2P

parser = argparse.ArgumentParser(description='Approximate a 2-Player Nash Eq. Pt. like a boss')
parser.add_argument(
    'settings', metavar='SETTING_PY_FILE_BASENAME', type=str, nargs='+',
    help='game setting .py file in `games` subdir: initial strategies, payoff matrices...')
args = parser.parse_args()
setting_file = args.settings[0]
settings = importlib.import_module('games.' + setting_file)

# algorithm settings
try:
    rate = settings.rate
except AttributeError:
    rate = 10 ** -5
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
try:
    contraction_test = settings.contraction_test
except AttributeError:
    contraction_test = False

fpi = FPI_2P([settings.str_row_init, settings.str_col_init], [settings.payoff_matrix_row, settings.payoff_matrix_col])
if display_game:
    fpi.print_game()
fpi.converge(rate, iters)
FPI_2P.display_eqpt(fpi.eqpt())
if use_LH:
    fpi.lemke_howson()
if contraction_test:
    pass

# ############################# contraction test #############################
if contraction_test:
    import contraction
    import utils
    rows, cols = settings.payoff_matrix_row.shape
    strategies_profile_1 = (utils.randomize_mixed_strategy(rows), utils.randomize_mixed_strategy(cols))
    strategies_profile_2 = (utils.randomize_mixed_strategy(rows), utils.randomize_mixed_strategy(cols))
    distance_function = contraction.distance_function_1
    payoff_matrices = (settings.payoff_matrix_row, settings.payoff_matrix_col)
    rate = settings.rate
    iters = settings.iters

    distance_l = []
    for i in range(iters):
        distance = distance_function(strategies_profile_1, strategies_profile_2)
        distance_l.append(np.log(distance))
        strategies_profile_1 = contraction.FPI_transformation_once(strategies_profile_1, payoff_matrices, rate)
        strategies_profile_2 = contraction.FPI_transformation_once(strategies_profile_2, payoff_matrices, rate)

    # plotting
    import matplotlib.pyplot as plt
    distance_a = np.array(distance_l)
    plt.plot(distance_a)
    plt.savefig('contraction.png')
    plt.show()
