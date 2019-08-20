import numpy as np
import utils

rate = 10 ** -5
iters = 10 ** 5

use_LH = True
contraction_test = True
str_row_init = utils.randomize_mixed_strategy(3)
str_col_init = utils.randomize_mixed_strategy(3)

payoff_matrix_row = np.array([
    [806.0, -592.0, -783.0],
    [-441.0, -67.0, -667.0],
    [350.0, -956.0, -139.0]])

payoff_matrix_col = np.array([
    [137.0, 769.0, -226.0],
    [138.0, 126.0, 566.0],
    [895.0, 812.0, 678.0]])

eqpt_1 = (
    np.array([0.08085829227999261, 0.35473691577190525, 0.564404791948102]),
    np.array([0.20853337310368875, 0.41132270792256187, 0.3801439189737494]))

eqpts = [eqpt_1]
