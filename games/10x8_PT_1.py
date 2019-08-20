import numpy as np
import utils

iters = 3 * 10 ** 5
rate = 10 ** -6
payoff_scale = 10 ** 0

use_LH = True

str_row_init = utils.randomize_mixed_strategy(10)
str_col_init = utils.randomize_mixed_strategy(8)

'''
'''
payoff_matrix_row = np.array([
    [-902.0, 405.0, -236.0, 971.0, -392.0, 697.0, 105.0, -879.0],
    [-689.0, 613.0, -963.0, 104.0, 35.0, -723.0, 375.0, 479.0],
    [751.0, 157.0, -44.0, 130.0, -190.0, 707.0, 262.0, 352.0],
    [334.0, -707.0, 378.0, 229.0, -665.0, 140.0, 35.0, 916.0],
    [716.0, 493.0, 290.0, 919.0, -787.0, -587.0, -613.0, 328.0],
    [345.0, -445.0, 347.0, -329.0, -779.0, 301.0, -626.0, 789.0],
    [-992.0, -111.0, -929.0, -772.0, 658.0, -285.0, -671.0, 257.0],
    [-609.0, 177.0, -745.0, -35.0, -159.0, 257.0, -749.0, 529.0],
    [394.0, 211.0, -478.0, 75.0, 863.0, 66.0, -382.0, 667.0],
    [-528.0, -858.0, -418.0, -653.0, -341.0, 122.0, -141.0, -780.0]])

payoff_matrix_col = np.array([
    [-235.0, -658.0, 306.0, -526.0, -134.0, 791.0, -84.0, 31.0],
    [611.0, -85.0, -466.0, -787.0, -638.0, 631.0, -40.0, -883.0],
    [918.0, 464.0, 632.0, -331.0, 980.0, -163.0, 408.0, 304.0],
    [689.0, 263.0, -528.0, 0.0, -14.0, 24.0, -555.0, 92.0],
    [-283.0, 526.0, 693.0, -509.0, 410.0, 702.0, -331.0, -516.0],
    [830.0, 546.0, -204.0, 706.0, -713.0, 523.0, -604.0, 636.0],
    [87.0, 26.0, -106.0, -920.0, -707.0, -916.0, -350.0, -161.0],
    [-331.0, -768.0, -467.0, -527.0, -689.0, -799.0, -327.0, -386.0],
    [-852.0, 852.0, 113.0, 123.0, -949.0, 576.0, -244.0, 353.0],
    [-150.0, 967.0, -151.0, 841.0, 971.0, 602.0, 159.0, -680.0]])
