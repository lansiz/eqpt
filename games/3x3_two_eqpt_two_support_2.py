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
    [-231.0, -505.0, 525.0],
    [-552.0, 831.0, -928.0],
    [-74.0, -96.0, -604.0]])
payoff_matrix_col = np.array([
    [175.0, -350.0, -770.0],
    [-641.0, -222.0, -189.0],
    [302.0, 504.0, 767.0]])
