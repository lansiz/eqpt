import numpy as np
import utils

iters = 1 * 10 ** 5
rate = 10 ** -5
payoff_scale = 10 ** 0

display_game = True
use_LH = True

rows = 50
cols = 40

str_row_init = utils.randomize_mixed_strategy(rows)
str_col_init = utils.randomize_mixed_strategy(cols)
payoff_matrix_row, payoff_matrix_col = utils.randomize_payoff_matrix(rows, cols)
