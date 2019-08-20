import utils
import numpy as np

iters = 1 * 10 ** 5
rate = 10 ** -5
payoff_scale = 10 ** 0

display_game = True
use_LH = True

str_row_init = utils.randomize_mixed_strategy(3)
str_col_init = utils.randomize_mixed_strategy(3)

payoff_matrix_row = np.array([
    [-441.0, -458.0, -298.0],
    [-973.0, 165.0, -114.0],
    [-908.0, 970.0, 870.0]])
payoff_matrix_col = np.array([
    [-989.0, 980.0, -805.0],
    [846.0, 125.0, 535.0],
    [746.0, -388.0, -952.0]])
