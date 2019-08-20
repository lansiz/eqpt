import numpy as np
import sys
sys.path.append('../')
import utils

iters = 10 * 10 ** 4
rate = 10 ** -4
payoff_scale = 10 ** 0

png_name = '60X40-conv-temp'

rows = 60
cols = 40

str_row_init = utils.randomize_mixed_strategy(rows)
str_col_init = utils.randomize_mixed_strategy(cols)

payoff_matrix_row, payoff_matrix_col = utils.randomize_payoff_matrix(rows, cols)

