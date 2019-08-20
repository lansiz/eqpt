import numpy as np
import utils

iters = 10 ** 5
rate = 10 ** -5
payoff_scale = 10 ** 0

display_game = True
use_LH = True

str_row_init = utils.randomize_mixed_strategy(3)
str_col_init = utils.randomize_mixed_strategy(3)

payoff_matrix_row = np.array([
    [-365.0, 174.0, 107.0],
    [138.0, 398.0, -926.0],
    [-248.0, 955.0, -643.0]])
payoff_matrix_col = np.array([
    [-867.0, 561.0, 496.0],
    [-560.0, -36.0, 742.0],
    [530.0, -744.0, 986.0]])
