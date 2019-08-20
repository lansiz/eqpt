import numpy as np
import utils

iters = 3 * 10 ** 5
rate = 10 ** -5
payoff_scale = 10 ** 0

str_row_init = utils.randomize_mixed_strategy(8)
str_col_init = utils.randomize_mixed_strategy(8)
payoff_matrix_row = np.array([
    [326, -69, -15, -652, -611, 458, -164, 114],
    [527, -259, -206, -371, 532, 920, 469, 102],
    [-969, -173, 0, -600, -800, -850, -953, 835],
    [-447, -181, -764, -803, 786, -64, 347, -86],
    [675, -469, 398, -265, -121, 679, -99, -876],
    [630, 18, -280, 574, 556, -5, 124, -210],
    [661, 781, -340, 659, -683, -155, -877, 823],
    [481, -802, 913, -938, -825, -663, 498, 367]]) * payoff_scale

payoff_matrix_col = np.array([
    [-350, -530, -586, 870, -492, 556, 930, -852],
    [749, 622, 726, -641, 155, -196, -663, 615],
    [-382, -668, 819, -358, 923, 998, 104, 935],
    [538, -329, 999, 19, 619, -441, 229, 458],
    [-910, 766, -541, 520, -370, 141, -831, -418],
    [-176, -66, 944, -269, 929, 963, 663, 908],
    [182, -754, -760, -867, 62, -833, -409, -379],
    [316, 539, -607, 813, 346, 254, -219, 472]]) * payoff_scale