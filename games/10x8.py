import numpy as np
import utils

iters = 3 * 10 ** 5
rate = 10 ** -5
payoff_scale = 10 ** 0

display_game = True
use_LH = True

str_row_init = utils.randomize_mixed_strategy(10)
str_col_init = utils.randomize_mixed_strategy(8)
payoff_matrix_row, payoff_matrix_col = utils.randomize_payoff_matrix(10, 8)
