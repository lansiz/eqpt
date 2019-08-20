import numpy as np
import utils

iters = 10 ** 5
rate = 10 ** -5
payoff_scale = 10 ** 0

display_game = True
use_LH = True

str_row_init = utils.randomize_mixed_strategy(3)
str_col_init = utils.randomize_mixed_strategy(3)
# str_row_init = np.array([0.4231, 0.1923, 0.3846])
# str_col_init = np.array([0.6209, 0.2745, 0.1046])

payoff_matrix_row = np.array([
    [-222, -532, -350],
    [-531, 272, 932],
    [-302, 807, -382]])
payoff_matrix_col = np.array([
    [478.0, -582.0, -104.0],
    [-133.0, -39.0, -449.0],
    [-355.0, 230.0, 288.0]])
