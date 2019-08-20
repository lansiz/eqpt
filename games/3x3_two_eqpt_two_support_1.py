import utils
import numpy as np

iters = 2 * 10 ** 5
rate = 10 ** -5
payoff_scale = 10 ** 0

display_game = True
use_LH = True

# given random initial strategies, the first eqpt 99% will be the attractor.
# EQPT 1: (array([0.14903620122237893, 0.0, 0.8509637987776211]), array([0.0, 0.5507541785568691, 0.4492458214431309]))
# meanwhile the second one is barely reachable
# EQPT 2: (array([0.0, 0.9790575916230366, 0.020942408376963352]), array([0.8223480947476828, 0.1776519052523172, 0.0]))

# str_row_init = utils.randomize_mixed_strategy(3)
# str_col_init = utils.randomize_mixed_strategy(3)

# str_row_init = np.array([0.14903620122237893, 0.0, 0.8509637987776211])
# str_col_init = np.array([0.0, 0.5507541785568691, 0.4492458214431309])

# the following will go to the second eqpt
# str_row_init = np.array([0.0, 0.9790575916230366, 0.020942408376963352])
# str_col_init = np.array([0.8223480947476828, 0.1776519052523172, 0.0])
str_row_init = np.array([0.0, 0.97, 0.03])
str_col_init = np.array([0.8, 0.2, 0.0])


payoff_matrix_row = np.array([
    [-316, -244, 799],
    [-48, -739, -830],
    [-393, 858, -552]])
payoff_matrix_col = np.array([
    [-608.0, 999.0, -811.0],
    [198.0, 202.0, 65.0],
    [224.0, 37.0, 354.0]])

eqpt_1 = (
    np.array([0.14903620122237893, 0.0, 0.8509637987776211]),
    np.array([0.0, 0.5507541785568691, 0.4492458214431309]))
eqpt_2 = (
    np.array([0.0, 0.9790575916230366, 0.020942408376963352]),
    np.array([0.8223480947476828, 0.1776519052523172, 0.0]))

eqpts = [eqpt_1, eqpt_2]
