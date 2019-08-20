import utils
import numpy as np

iters = 1 * 10 ** 5
rate = 10 ** -5

display_game = True
use_LH = True
contraction_test = True

str_row_init = utils.randomize_mixed_strategy(6)
str_col_init = utils.randomize_mixed_strategy(4)

payoff_matrix_row = np.array([
    [680.0, 49.0, 175.0, -444.0],
    [425.0, 763.0, -66.0, 920.0],
    [86.0, -132.0, -696.0, -984.0],
    [976.0, 312.0, -269.0, 355.0],
    [-20.0, 449.0, -874.0, 374.0],
    [-185.0, -25.0, -846.0, -561.0]])
payoff_matrix_col = np.array([
    [740.0, 491.0, 124.0, 834.0],
    [371.0, 70.0, 691.0, -320.0],
    [850.0, 183.0, -628.0, 226.0],
    [-26.0, 520.0, -643.0, 236.0],
    [-449.0, -213.0, 201.0, 144.0],
    [687.0, 736.0, -880.0, -398.0]])

eqpt_1 = (
    np.array([0.0, 0.6446280991735537, 0.0, 0.3553719008264463, 0.0, 0.0]),
    np.array([0.45009980039920156, 0.5499001996007985, 0.0, 0.0]))

eqpts = [eqpt_1]
