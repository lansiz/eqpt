import numpy as np
import utils

rate = 10 ** -5
iters = 10 ** 5

use_LH = True
contraction_test = True

str_row_init = utils.randomize_mixed_strategy(3)
str_col_init = utils.randomize_mixed_strategy(3)

payoff_matrix_row = np.array([
    [231, -590, 850],
    [550, -714, -56],
    [214, 854, -756]])
payoff_matrix_col = np.array([
    [993.0, 679.0, 611.0],
    [657.0, 925.0, 818.0],
    [-157.0, 464.0, 962.0]])

eqpt_1 = (
    np.array([0.5463885404111217, 0.3119736960781902, 0.141637763510688]),
    np.array([0.6044981416813573, 0.21162375503879446, 0.18387810327984816]))
eqpts = [eqpt_1]
