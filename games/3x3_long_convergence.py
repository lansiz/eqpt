import numpy as np
import utils

iters = 1 * 10 ** 5
rate = 10 ** -5
payoff_scale = 10 ** 0

display_game = True
use_LH = True

# [0.0988 0.5679 0.3333]
# [0.5466 0.2674 0.186]


str_row_init = utils.randomize_mixed_strategy(3)  # np.array([0.2811, 0.4424, 0.2765])
str_col_init = utils.randomize_mixed_strategy(3)  # np.array([0.3251, 0.3086, 0.3663])

payoff_matrix_row = np.array([
    [181, -325, 201],
    [-528, 732, -285],
    [509, -789, -227]])
payoff_matrix_col = np.array([
    [-415.0, 967.0, -128.0],
    [491.0, -342.0, 308.0],
    [-230.0, -899.0, 670.0]])
