import utils
import numpy as np

iters = 1 * 10 ** 5
rate = 10 ** -5
payoff_scale = 10 ** 0

display_game = True
use_LH = True

str_row_init = utils.randomize_mixed_strategy(3)
str_col_init = utils.randomize_mixed_strategy(3)

payoff_matrix_row = np.array([
    [860.0, -545.0, -355.0],
    [-118.0, 342.0, -788.0],
    [-156.0, -879.0, 562.0]])
payoff_matrix_col = np.array([
    [-937.0, 984.0, -70.0],
    [931.0, 169.0, 269.0],
    [-42.0, 347.0, -723.0]])
