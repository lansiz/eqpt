import numpy as np
import utils

iters = 1 * 10 ** 5
rate = 10 ** -5
payoff_scale = 10 ** 0

display_game = True
use_LH = True

str_row_init = utils.randomize_mixed_strategy(3)  # np.array([0.2811, 0.4424, 0.2765])
str_col_init = utils.randomize_mixed_strategy(3)  # np.array([0.3251, 0.3086, 0.3663])

payoff_matrix_row = np.array([
    [-503, -349, 177],
    [-868, 855, -199],
    [660, 429, 206]])

payoff_matrix_col = np.array([
    [49.0, 780.0, -105.0],
    [789.0, -404.0, 226.0],
    [387.0, 642.0, -756.0]])
