import utils

iters = 1 * 10 ** 5
rate = 10 ** -5

display_game = True
use_LH = True
contraction_test = True

str_row_init = utils.randomize_mixed_strategy(6)
str_col_init = utils.randomize_mixed_strategy(4)
payoff_matrix_row, payoff_matrix_col = utils.randomize_payoff_matrix(6, 4)
