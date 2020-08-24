import utils
import numpy as np

iters = 1 * 10 ** 5
rate = 10 ** -5
payoff_scale = 10 ** 0

display_game = True
# use_LH = True

str_row_init = utils.randomize_mixed_strategy(4)
str_col_init = utils.randomize_mixed_strategy(4)
payoff_matrix_row = np.array([
    [100, 200, 300, 400],
    [100, 200, 300, 400],
    [100, 200, 300, 400],
    [400, 200, 300, 400]])

payoff_matrix_col = np.array([
    [-200, 100, 300, -300],
    [-200, 100, 300, -300],
    [-200, 100, 300, -300],
    [-200, 100, 300, -300]])
eqpt_1 = (
    np.array([0.1504, 0.0406, 0.1098, 0.6992]),
    np.array([0.00, 0.000, 1, 0.000]))

eqpts = [eqpt_1]
