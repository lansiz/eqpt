import utils
import numpy as np

iters = 1 * 10 ** 5
rate = 10 ** -5
payoff_scale = 10 ** 3

display_game = True
use_LH = True

str_row_init = utils.randomize_mixed_strategy(3)
str_col_init = utils.randomize_mixed_strategy(3)
payoff_matrix_row = np.array([
    [0, 0, 1],
    [1, 0, 0],
    [0, 1, 0]])
payoff_matrix_col = np.array([
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 0]])
payoff_matrix_row = payoff_matrix_row * payoff_scale
payoff_matrix_col = payoff_matrix_col * payoff_scale
