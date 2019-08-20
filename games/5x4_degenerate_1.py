import utils
import numpy as np

iters = 1 * 10 ** 5
rate = 10 ** -5
payoff_scale = 10 ** 0

display_game = True
use_LH = True

str_row_init = utils.randomize_mixed_strategy(5)
str_col_init = utils.randomize_mixed_strategy(4)
# payoff_matrix_row, payoff_matrix_col = utils.randomize_payoff_matrix(5, 4)
payoff_matrix_row = np.array([
    [585.0, -752.0, -349.0, 288.0],
    [-424.0, 464.0, -296.0, 875.0],
    [864.0, -787.0, 914.0, -255.0],
    [592.0, 58.0, -484.0, -179.0],
    [273.0, -748.0, -105.0, 576.0]])

payoff_matrix_col = np.array([
    [-932.0, -309.0, -186.0, 533.0],
    [958.0, -452.0, 708.0, -13.0],
    [-104.0, 548.0, -631.0, -452.0],
    [-227.0, -41.0, 281.0, 754.0],
    [718.0, -742.0, -89.0, -131.0]])

eqpt_1 = (
    np.array([0.36689714779602417, 0.0, 0.0, 0.0, 0.6331028522039758]),
    np.array([0.47999999999999987, 0.0, 0.0, 0.5200000000000001]))

eqpts = [eqpt_1]
