import numpy as np
import utils

iters = 1 * 10 ** 5
rate = 10 ** -5
payoff_scale = 10 ** 0

display_game = True
use_LH = True

str_row_init = utils.randomize_mixed_strategy(3)
str_col_init = utils.randomize_mixed_strategy(3)

payoff_matrix_row = np.array([
    [-351, 727, -193],
    [107, -715, 332],
    [478, -332, -315]])
payoff_matrix_col = np.array([
    [316.0, -816.0, -814.0],
    [36.0, 635.0, 130.0],
    [761.0, -51.0, 899.0]])
