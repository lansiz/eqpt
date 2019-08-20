import utils
import numpy as np

iters = 10 ** 5
rate = 10 ** -5

display_game = True
use_LH = True
contraction_test = True

str_row_init = utils.randomize_mixed_strategy(4)
str_col_init = utils.randomize_mixed_strategy(4)
payoff_matrix_row = np.array([
    [-715.0, -152.0, 886.0, 763.0],
    [-823.0, 353.0, -863.0, 664.0],
    [-291.0, 835.0, 855.0, 175.0],
    [154.0, -428.0, -963.0, -283.0]])
payoff_matrix_col = np.array([
    [281.0, 971.0, 635.0, -672.0],
    [952.0, 408.0, -229.0, 491.0],
    [-377.0, -929.0, 952.0, 100.0],
    [-350.0, -699.0, 70.0, 573.0]])

eqpt_1 = (
    np.array([0.8484438430311231, 0.0, 0.15155615696887687, 0.0]),
    np.array([0.0, 0.030451866404715127, 0.9695481335952848, 0.0]))

eqpts = [eqpt_1]
