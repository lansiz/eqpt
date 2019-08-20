import utils
import numpy as np

iters = 1 * 10 ** 5
rate = 10 ** -5
payoff_scale = 10 ** 0

display_game = True
use_LH = True

str_row_init = utils.randomize_mixed_strategy(3)
str_col_init = utils.randomize_mixed_strategy(3)
# payoff_matrix_row, payoff_matrix_col = utils.randomize_payoff_matrix(3, 3)

# str_row_init = np.array([0.0613, 0.5706, 0.3681])
# str_col_init = np.array([0.3721, 0.0814, 0.5465])
payoff_matrix_row = np.array([
    [-97.0, -99.0, -611.0],
    [595.0, 832.0, 832.0],
    [664.0, -96.0, -579.0]])
payoff_matrix_col = np.array([
    [200.0, 588.0, 584.0],
    [172.0, 695.0, 805.0],
    [-851.0, 481.0, 372.0]])

