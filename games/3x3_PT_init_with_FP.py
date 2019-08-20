import numpy as np
import utils

iters = 1 * 10 ** 5
rate = 10 ** -5
payoff_scale = 10 ** 0

display_game = True
use_LH = True

# Lemke-Lowson gives:
str_row_init = np.array([0.15556376239311384, 0.3850174710945712, 0.459418766512315])
str_col_init = np.array([0.2116999757925876, 0.5821356134801097, 0.2061644107273028])

# let the initial strategies deviate the given f.p. a slight bit
# str_row_init = np.array([0.1555, 0.3851, 0.4594])
# str_col_init = np.array([0.2116, 0.5821, 0.2063])
# str_row_init = np.array([0.15556376241, 0.385017471096, 0.45941876653])
# str_col_init = np.array([0.21169997579, 0.582135613481, 0.20616441072])

payoff_matrix_row = np.array([
    [678, 110, -33],
    [-673, 942, -995],
    [-683, 725, -372]])
payoff_matrix_col = np.array([
    [328.0, 976.0, 442.0],
    [-19.0, 669.0, 701.0],
    [587.0, -209.0, -55.0]])
