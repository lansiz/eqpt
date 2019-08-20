import numpy as np
import utils

iters = 10 ** 5
rate = 10 ** -5
payoff_scale = 10 ** 0

display_game = True
use_LH = True

annotate_game_details = True
png_name = '3X3-2eq2sp'

# str_row_init = utils.randomize_mixed_strategy(3)
# str_col_init = utils.randomize_mixed_strategy(3)
# str_row_init = np.array([0.2372, 0.4233, 0.3395])
# str_col_init = np.array([0.5481, 0.3365, 0.1154])

str_row_init_l = [np.array([0.2372, 0.4233, 0.3395]), np.array([0.1076, 0.4191, 0.4733])]
str_col_init_l = [np.array([0.5481, 0.3365, 0.1154]), np.array([0.2, 0.4176, 0.3824])]

payoff_matrix_row = np.array([
    [-231.0, -505.0, 525.0],
    [-552.0, 831.0, -928.0],
    [-74.0, -96.0, -604.0]])
payoff_matrix_col = np.array([
    [175.0, -350.0, -770.0],
    [-641.0, -222.0, -189.0],
    [302.0, 504.0, 767.0]])

eqpts = [
    (np.array([0.3297872340425532, 0.0, 0.6702127659574468]), np.array([0.8779160186625193, 0.0, 0.12208398133748055])),
    (np.array([0.0728476821192053, 0.9271523178807947, 0.0]), np.array([0.0, 0.5209752599498029, 0.4790247400501973]))]
