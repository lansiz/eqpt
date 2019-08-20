import numpy as np
import utils

iters = 1 * 10 ** 5
rate = 10 ** -5
payoff_scale = 10 ** 0

display_game = True
use_LH = True

# [0.0988 0.5679 0.3333]
# [0.5466 0.2674 0.186]

# [0.4285 0.1429 0.4286]
# [0.4286 0.2857 0.2857]
str_row_init = utils.randomize_mixed_strategy(3)  # np.array([0.2811, 0.4424, 0.2765])
str_col_init = utils.randomize_mixed_strategy(3)  # np.array([0.3251, 0.3086, 0.3663])

payoff_matrix_row = np.array([
    [845, -193, 971],
    [-642, 430, 549],
    [-594, -794, -14]])
payoff_matrix_col = np.array([
    [-200.0, 455.0, 795.0],
    [602.0, -287.0, -753.0],
    [-192.0, 589.0, 434.0]])
