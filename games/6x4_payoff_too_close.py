import numpy as np
import utils

iters = 1 * 10 ** 5
rate = 10 ** -5
payoff_scale = 10 ** 0

display_game = True
use_LH = True

str_row_init = utils.randomize_mixed_strategy(6)
str_col_init = utils.randomize_mixed_strategy(4)
# payoff_matrix_row, payoff_matrix_col = utils.randomize_payoff_matrix(4, 4)

payoff_matrix_row = np.array([
    [904.0, 191.0, -914.0, -700.0],
    [643.0, 285.0, 268.0, -113.0],
    [110.0, 661.0, -840.0, 644.0],
    # the eqpt takes the first and fourth row as supports
    # here 903 is too close to the 904 in the first row
    # which makes the approximate too far from the true one
    # this can be seen as a degenerate game
    [903.0, 745.0, -432.0, 511.0],
    [547.0, 736.0, 324.0, 320.0],
    [773.0, 744.0, 350.0, -606.0]])

payoff_matrix_col = np.array([
    [677.0, 942.0, 990.0, 442.0],
    [-430.0, -420.0, 98.0, -772.0],
    [-6.0, -67.0, 986.0, 917.0],
    [895.0, 178.0, 598.0, -268.0],
    [606.0, 713.0, 336.0, -25.0],
    [981.0, 388.0, -88.0, 308.0]])

eqpt_3 = (
    np.array([0.242, 0.0, 0.0004, 0.7563, 0.001, 0.0003]),
    np.array([0.9984, 0.0004, 0.0006, 0.0006]))

eqpt_1 = (
    np.array([0.4868852459016394, 0.0, 0.0, 0.5131147540983607, 0.0, 0.0]),
    np.array([0.9979296066252589, 0.0, 0.0020703933747411862, 0.0]))

eqpt_2 = (
    np.array([0.2132, 0.0002, 0.0002, 0.7844, 0.0013, 0.0007]),
    np.array([0.9982, 0.0002, 0.001, 0.0006]))

eqpts = [eqpt_1, eqpt_2, eqpt_3]
