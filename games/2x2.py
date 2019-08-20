import utils

iters = 1 * 10 ** 5
rate = 10 ** -5
payoff_scale = 10 ** 0

str_row_init = utils.randomize_mixed_strategy(2)
str_col_init = utils.randomize_mixed_strategy(2)
payoff_matrix_row, payoff_matrix_col = utils.randomize_payoff_matrix(2, 2)
