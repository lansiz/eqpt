import numpy as np
import sys
sys.path.append('../')
import utils

iters = 10 * 10 ** 4
rate = 10 ** -4
payoff_scale = 10 ** 0

# settings
rows = 200
cols = 150

str_row_init = utils.randomize_mixed_strategy(rows) * payoff_scale
str_col_init = utils.randomize_mixed_strategy(cols) * payoff_scale

payoff_matrix_row, payoff_matrix_col = utils.randomize_payoff_matrix(rows, cols)

