import numpy as np
import utils

rate = 10 ** -5
iters = 10 ** 5

use_LH = True
contraction_test = True

str_row_init = utils.randomize_mixed_strategy(3)
str_col_init = utils.randomize_mixed_strategy(3)

payoff_matrix_row = np.array([
    [991, -491, 516],
    [-685, 657, -696],
    [-852, 617, -580]])

payoff_matrix_col = np.array([
    [218.0, 974.0, -520.0],
    [-213.0, -815.0, 983.0],
    [830.0, -954.0, -875.0]])

eqpt_1 = (
    np.array([0.5075978877997206, 0.41852907359450886, 0.07387303860577048]),
    np.array([0.11440242940356413, 0.5360520030691753, 0.34954556752726057]))

eqpts = [eqpt_1]
