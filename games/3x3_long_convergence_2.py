import numpy as np
import utils

iters = 5 * 10 ** 5
rate = 10 ** -5
payoff_scale = 10 ** 0

display_game = True
use_LH = True

# [0.0988 0.5679 0.3333]
# [0.5466 0.2674 0.186]


str_row_init = utils.randomize_mixed_strategy(3)  # np.array([0.2811, 0.4424, 0.2765])
str_col_init = utils.randomize_mixed_strategy(3)  # np.array([0.3251, 0.3086, 0.3663])

payoff_matrix_row = np.array([
    [786.0, 54.0, -148.0],
    [671.0, 132.0, -610.0],
    [-66.0, 600.0, 297.0]])
payoff_matrix_col = np.array([
    [-28.0, 953.0, -82.0],
    [-229.0, 703.0, 171.0],
    [948.0, 14.0, -830.0]])

# [0.204 0.2434 0.5526]
# [0.3138 0.4734 0.2128]
