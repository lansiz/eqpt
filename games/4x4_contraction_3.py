import utils
import numpy as np

iters = 1 * 10 ** 5
rate = 10 ** -5

display_game = True
use_LH = True
contraction_test = True

str_row_init = utils.randomize_mixed_strategy(4)
str_col_init = utils.randomize_mixed_strategy(4)

# str_row_init = np.array([0.114, 0.1678, 0.6242, 0.0940])
# str_col_init = np.array([0.1834, 0.3222, 0.1333, 0.3611])

payoff_matrix_row = np.array([
    [-419.0, 128.0, 832.0, 238.0],
    [-419.0, 843.0, -313.0, 780.0],
    [522.0, 4.0, -515.0, -358.0],
    [341.0, 329.0, -83.0, -849.0]])
payoff_matrix_col = np.array([
    [311.0, 102.0, -719.0, -500.0],
    [526.0, -312.0, 660.0, 991.0],
    [-752.0, -142.0, -640.0, -890.0],
    [-729.0, -209.0, 881.0, -981.0]])

eqpt_1 = (
    np.array([0.0, 1.0, 0.0, 0.0]),
    np.array([0.0, 0.0, 0.0, 1.0]))
eqpt_2 = (
    np.array([0.5654820263391568, 0.07935464123619633, 0.0, 0.3551633324246467]),
    np.array([0.23076923076923078, 0.47353184449958646, 0.29569892473118276, 0.0]))
eqpts = [eqpt_1, eqpt_2]
