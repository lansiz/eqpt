import utils

iters = 1 * 10 ** 5
rate = 10 ** -5
payoff_scale = 10 ** 0

display_game = True
use_LH = True

str_row_init = utils.randomize_mixed_strategy(3)
str_col_init = utils.randomize_mixed_strategy(3)
payoff_matrix_row, _ = utils.randomize_payoff_matrix(3, 3)
# nagtive matrix
payoff_matrix_col = - payoff_matrix_row
