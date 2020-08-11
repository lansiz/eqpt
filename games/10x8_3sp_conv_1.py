import numpy as np
import utils

iters = 2 * 10 ** 5
rate = 10 ** -5
payoff_scale = 10 ** 0

display_game = True
use_LH = True

str_row_init = utils.randomize_mixed_strategy(10)
str_col_init = utils.randomize_mixed_strategy(8)
payoff_matrix_row = np.array([[481.0, -589.0, 829.0, 214.0, 826.0, -880.0, -849.0, 129.0],
                              [800.0, 474.0, -426.0, -33.0, 839.0, 485.0, 287.0, 87.0],
                              [694.0, -227.0, -590.0, -939.0, -805.0, 985.0, -568.0, 600.0],
                              [-475.0, 191.0, 331.0, -334.0, -312.0, -932.0, -597.0, -286.0],
                              [930.0, -433.0, -777.0, -734.0, -324.0, 898.0, 877.0, -956.0],
                              [438.0, -399.0, -835.0, 188.0, -825.0, -698.0, -178.0, -92.0],
                              [-277.0, -905.0, 605.0, 447.0, 95.0, 884.0, -947.0, 646.0],
                              [-292.0, -136.0, 155.0, 110.0, 642.0, -689.0, 297.0, -620.0],
                              [284.0, -836.0, 122.0, 717.0, -604.0, 688.0, 415.0, 856.0],
                              [818.0, 821.0, -479.0, -115.0, 529.0, 76.0, -515.0, 816.0]])
payoff_matrix_col = np.array([[-92.0, -426.0, 62.0, 929.0, 695.0, 510.0, -745.0, -793.0],
                              [624.0, -300.0, -65.0, -309.0, -917.0, 215.0, -153.0, 369.0],
                              [871.0, 640.0, -723.0, 332.0, 820.0, -556.0, 7.0, 642.0],
                              [-279.0, -210.0, 690.0, 95.0, 626.0, 997.0, 730.0, -236.0],
                              [501.0, 33.0, 52.0, 189.0, -352.0, -738.0, -878.0, -152.0],
                              [-424.0, 154.0, 581.0, 32.0, -978.0, -524.0, 52.0, 35.0],
                              [-995.0, -588.0, 618.0, 682.0, -824.0, 603.0, 253.0, 530.0],
                              [97.0, -3.0, 705.0, -805.0, 882.0, -394.0, 791.0, -844.0],
                              [-207.0, -437.0, -845.0, -715.0, 458.0, -563.0, 473.0, 429.0],
                              [-145.0, 335.0, 715.0, -774.0, -952.0, 305.0, 147.0, -952.0]])
