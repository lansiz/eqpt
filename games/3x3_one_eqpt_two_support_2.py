import utils
import numpy as np

iters = 1 * 10 ** 5
rate = 10 ** -5
payoff_scale = 10 ** 0

display_game = True
use_LH = True

str_row_init = utils.randomize_mixed_strategy(3)
str_col_init = utils.randomize_mixed_strategy(3)

payoff_matrix_row = np.array([
    [-795.0, -989.0, -900.0],
    [-375.0, -279.0, -390.0],
    [80.0, -407.0, -707.0]])
payoff_matrix_col = np.array([
    [599.0, -326.0, -434.0],
    [-9.0, -756.0, -570.0],
    [-786.0, 572.0, -395.0]])
