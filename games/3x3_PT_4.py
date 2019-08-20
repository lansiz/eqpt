import numpy as np
import utils

rate = 10 ** -5
iters = 10 ** 5

use_LH = True
contraction_test = True

str_row_init = utils.randomize_mixed_strategy(3)
str_col_init = utils.randomize_mixed_strategy(3)

payoff_matrix_row = np.array([
    [314.0, -760.0, -613.0],
    [-111.0, 118.0, -220.0],
    [22.0, -858.0, 814.0]])

payoff_matrix_col = np.array([
    [-246.0, -446.0, 349.0],
    [695.0, -243.0, -887.0],
    [339.0, 858.0, 67.0]])

eqpt_1 = (
    np.array([0.4880457156539655, 0.11537071410075421, 0.3965835702452804]),
    np.array([0.6205274449647193, 0.23627103088894924, 0.1432015241463315]))

eqpts = [eqpt_1]
