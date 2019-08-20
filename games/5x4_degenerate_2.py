import utils
import numpy as np

iters = 1 * 10 ** 5
rate = 10 ** -5
payoff_scale = 10 ** 0

display_game = True
use_LH = True

str_row_init = utils.randomize_mixed_strategy(5)
str_col_init = utils.randomize_mixed_strategy(4)
payoff_matrix_row, payoff_matrix_col = utils.randomize_payoff_matrix(5, 4)
payoff_matrix_row = np.array([
    [-218.0, 335.0, 376.0, -887.0],
    [403.0, -221.0, 719.0, -857.0],
    [-164.0, -93.0, 805.0, -196.0],
    [-777.0, -289.0, 90.0, -123.0],
    [-120.0, -505.0, -812.0, 6.0]])

payoff_matrix_col = np.array([
    [796.0, -630.0, 130.0, -477.0],
    [-333.0, 878.0, 514.0, -315.0],
    [-719.0, -977.0, -372.0, 986.0],
    [942.0, 0.0, -210.0, 681.0],
    [720.0, -89.0, 116.0, -945.0]])

eqpts = [(
    np.array([0.0, 0.13743347063557187, 0.4254301094719088, 0.0, 0.4371364198925194]),
    np.array([0.506891653390154, 0.0, 0.06702095589024501, 0.42608739071960094]))]
