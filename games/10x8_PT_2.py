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
    [110.0, -870.0, -896.0, -480.0, -510.0, 983.0, 45.0, 740.0],
    [373.0, 331.0, 308.0, -569.0, 110.0, -743.0, -416.0, -824.0],
    [-988.0, -177.0, -348.0, -210.0, -28.0, -307.0, 40.0, -804.0],
    [56.0, 922.0, -349.0, 190.0, 203.0, -733.0, 803.0, 217.0],
    [669.0, -880.0, -169.0, 227.0, 648.0, -838.0, -390.0, 755.0],
    [-63.0, -56.0, 219.0, 98.0, -119.0, 738.0, 763.0, -291.0],
    [256.0, 116.0, -750.0, 75.0, 13.0, 991.0, 276.0, -410.0],
    [372.0, 753.0, -5.0, -760.0, 169.0, -447.0, -273.0, 187.0],
    [640.0, -631.0, 333.0, -84.0, 722.0, -749.0, 968.0, 566.0],
    [-486.0, 433.0, 401.0, 429.0, 743.0, 939.0, -207.0, -23.0]])

payoff_matrix_col = np.array([
    [-400.0, 90.0, -700.0, 465.0, -838.0, 850.0, 426.0, -696.0],
    [-738.0, -235.0, -252.0, -68.0, -76.0, -671.0, 466.0, 966.0],
    [-835.0, 981.0, 235.0, 991.0, -583.0, -643.0, -468.0, 467.0],
    [-163.0, 463.0, -579.0, -173.0, -73.0, -863.0, 747.0, 786.0],
    [-50.0, -815.0, 969.0, -437.0, -646.0, -197.0, 595.0, 461.0],
    [-14.0, 673.0, 278.0, -21.0, -491.0, -921.0, -825.0, -467.0],
    [287.0, -545.0, 707.0, 633.0, 166.0, 510.0, 698.0, 577.0],
    [819.0, -101.0, 391.0, 933.0, 927.0, 477.0, 541.0, -761.0],
    [-877.0, 974.0, 951.0, -469.0, -253.0, 735.0, -982.0, 836.0],
    [374.0, 547.0, -727.0, 714.0, 585.0, -951.0, 253.0, 741.0]])
