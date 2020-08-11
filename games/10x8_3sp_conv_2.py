import numpy as np
import utils

iters = 2 * 10 ** 5
rate = 10 ** -5
payoff_scale = 10 ** 0

display_game = True
use_LH = True

str_row_init = utils.randomize_mixed_strategy(10)
str_col_init = utils.randomize_mixed_strategy(8)
payoff_matrix_row = np.array(
    [[185.0, 170.0, - 916.0, 448.0, 509.0, - 578.0, - 355.0, - 498.0],
     [759.0, 570.0, 150.0, 855.0, 479.0, - 567.0, - 427.0, 646.0],
     [-92.0, 627.0, 950.0, 464.0, 171.0, - 926.0, 134.0, - 155.0],
     [-979.0, 158.0, - 566.0, 300.0, 823.0, - 788.0, - 947.0, - 786.0],
     [885.0, - 450.0, - 586.0, - 130.0, - 784.0, - 98.0, - 225.0, - 500.0],
     [-834.0, - 525.0, 376.0, - 392.0, - 134.0, - 853.0, 663.0, - 225.0],
     [410.0, - 805.0, 169.0, 626.0, 702.0, 58.0, 629.0, 779.0],
     [206.0, - 307.0, 724.0, 467.0, - 857.0, - 165.0, 107.0, 486.0],
     [592.0, 361.0, 93.0, 984.0, - 614.0, - 110.0, 644.0, - 173.0],
     [409.0, - 245.0, 971.0, - 120.0, - 197.0, - 776.0, - 463.0, 5.0]])
payoff_matrix_col = np.array(
    [[89.0, - 955.0, 291.0, - 948.0, 83.0, - 186.0, 134.0, - 118.0],
     [-410.0, 472.0, 321.0, 930.0, 392.0, - 842.0, 808.0, - 649.0],
     [301.0, - 234.0, - 232.0, - 386.0, 453.0, - 493.0, - 891.0, - 601.0],
     [-902.0, 79.0, 746.0, 436.0, - 515.0, - 721.0, 70.0, - 287.0],
     [714.0, 776.0, - 279.0, - 445.0, 74.0, - 760.0, - 127.0, - 540.0],
     [-473.0, 41.0, 885.0, 199.0, - 809.0, 968.0, 494.0, - 682.0],
     [-279.0, 452.0, 288.0, - 961.0, 510.0, 93.0, - 486.0, - 362.0],
     [-377.0, 286.0, - 360.0, - 230.0, - 12.0, 505.0, - 856.0, 439.0],
     [78.0, - 126.0, 269.0, - 492.0, - 398.0, 614.0, 678.0, 535.0],
     [-962.0, - 151.0, 378.0, - 91.0, 329.0, 428.0, - 770.0, - 114.0]])