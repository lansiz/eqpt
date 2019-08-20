import utils
import numpy as np

iters = 2 * 10 ** 5
rate = 10 ** -5
payoff_scale = 10 ** 3

display_game = True
use_LH = True

str_row_init = utils.randomize_mixed_strategy(3)
str_col_init = utils.randomize_mixed_strategy(3)

# degenerate game example from nashpy docs
payoff_matrix_row = np.array([
    [0, -1, 1],
    [-1, 0, 1],
    [-1, 0, 1]]) * payoff_scale
payoff_matrix_col = np.array([
    [0, 1, -1],
    [1, 0, -1],
    [1, 0, -1]]) * payoff_scale


eqpt_3 = (
    np.array([0.5, 0.5, 0]), np.array([0.5, 0.5, 0]))

eqpt_4 = (
    np.array([.5, 0, .5]), np.array([.5, .5, 0]))

eqpts = [eqpt_3, eqpt_4]
