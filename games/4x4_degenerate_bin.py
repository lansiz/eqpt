import utils
import numpy as np

iters = 1 * 10 ** 5
rate = 10 ** -5
payoff_scale = 10 ** 0

display_game = True

str_row_init = utils.randomize_mixed_strategy(4)
str_col_init = utils.randomize_mixed_strategy(4)
payoff_matrix_row = np.array([
    [100, 200, 300, 400],
    [100, 200, 300, 400],
    [100, 200, 300, 400],
    [100, 200, 300, 400]])

payoff_matrix_col = np.array([
    [-200, 100, 300, -300],
    [-200, 100, 300, -300],
    [-200, 100, 300, -300],
    [-200, 100, 300, -300]]).T

eqpt_1 = (
    np.array([0.2926, 0.4472, 0.2195, 0.0407]),
    np.array([0.5449, 0.3241, 0.0207, 0.1103]))

eqpt_2 = (
    np.array([0.2, 0.1, 0, 0.7]),
    np.array([0.1, 0, 0.2, 0.7]))

eqpt_3 = (
    np.array([0.2, 0.8, 0, 0]),
    np.array([0, 0, 0.3, 0.7]))

eqpts = [eqpt_1, eqpt_2, eqpt_3]
