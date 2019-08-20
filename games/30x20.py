import numpy as np
import utils

iters = 3 * 10 ** 5
rate = 10 ** -5
payoff_scale = 10 ** 0

use_LH = False

str_row_init = utils.randomize_mixed_strategy(30)
str_col_init = utils.randomize_mixed_strategy(20)
payoff_matrix_row, payoff_matrix_col = utils.randomize_payoff_matrix(30, 20)
