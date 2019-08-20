import utils
import numpy as np

iters = 1 * 10 ** 5
rate = 10 ** -5

display_game = True
use_LH = True
contraction_test = True

str_row_init = utils.randomize_mixed_strategy(4)
str_col_init = utils.randomize_mixed_strategy(4)
payoff_matrix_row = np.array([
    [628.0, 468.0, 436.0, -638.0],
    [-465.0, -291.0, 137.0, -118.0],
    [-420.0, -445.0, 123.0, -484.0],
    [-89.0, -506.0, -316.0, -643.0]])
payoff_matrix_col = np.array([
    [-259.0, -290.0, -117.0, 19.0],
    [-469.0, 789.0, 175.0, -853.0],
    [32.0, -707.0, 81.0, -751.0],
    [628.0, -913.0, 97.0, -514.0]])

eqpt_1 = (
    np.array([0.8831615120274914, 0.11683848797250859, 0.0, 0.0]),
    np.array([0.0, 0.0, 0.6349206349206349, 0.36507936507936506]))

eqpts = [eqpt_1]
