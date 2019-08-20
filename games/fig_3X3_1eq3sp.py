import numpy as np
import utils

iters = 1 * 10 ** 5
rate = 10 ** -5
payoff_scale = 10 ** 0

display_game = True
use_LH = True

annotate_game_details = True
png_name = '3X3-1eq3sp'

str_row_init_l = [np.array([0.3619, 0.3905, 0.2476])]
str_col_init_l = [np.array([0.76, 0.04, 0.2])]

payoff_matrix_row = np.array([
    [678, 110, -33],
    [-673, 942, -995],
    [-683, 725, -372]])
payoff_matrix_col = np.array([
    [328.0, 976.0, 442.0],
    [-19.0, 669.0, 701.0],
    [587.0, -209.0, -55.0]])

eqpts = [
    (np.array([0.1555637623931138, 0.3850174710945712, 0.459418766512315]), np.array([0.2116999757925876, 0.5821356134801096, 0.20616441072730282]))]
