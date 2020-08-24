import numpy as np
import utils

iters = 2 * 10 ** 5
rate = 10 ** -5
payoff_scale = 10 ** 0

display_game = True
use_LH = True
contraction_test = True

str_row_init = utils.randomize_mixed_strategy(3)
str_col_init = utils.randomize_mixed_strategy(3)

# str_row_init = np.array([0.1667, 0.5, 0.3333])
# str_col_init = np.array([0.3333, 0.5, 0.1667])

payoff_matrix_row = np.array([
    [-517.0, 494.0, 885.0],
    [-212.0, 41.0, 722.0],
    [720.0, - 316.0, - 758.0]])
payoff_matrix_col = np.array([
    [517.0, - 494.0, - 885.0],
    [212.0, - 41.0, - 722.0],
    [-720.0, 316.0, 758.0]])
