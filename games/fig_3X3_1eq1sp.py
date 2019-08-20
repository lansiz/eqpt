import utils
import numpy as np

iters = 1 * 10 ** 5
rate = 10 ** -5

display_game = True
use_LH = True

annotate_game_details = True
png_name = '3X3-1eq1sp'
# str_row_init = utils.randomize_mixed_strategy(3)
# str_col_init = utils.randomize_mixed_strategy(3)
# payoff_matrix_row, payoff_matrix_col = utils.randomize_payoff_matrix(3, 3)

str_row_init_l = [np.array([0.2851, 0.4734, 0.2415])]
str_col_init_l = [np.array([0.746, 0.1667, 0.0873])]
# str_row_init_l = [np.array([0.39, 0.566, 0.044])]
# str_col_init_l = [np.array([0.0079, 0.2937, 0.6984])]

payoff_matrix_row = np.array([
    [-97.0, -99.0, -611.0],
    [595.0, 832.0, 832.0],
    [664.0, -96.0, -579.0]])
payoff_matrix_col = np.array([
    [200.0, 588.0, 584.0],
    [172.0, 695.0, 805.0],
    [-851.0, 481.0, 372.0]])

eqpts = [
    (np.array([0.0, 1.0, 0.0]), np.array([0.0, 0.0, 1.0]))]
