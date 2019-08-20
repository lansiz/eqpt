import numpy as np
import utils
from FPI_2P import FPI_2P_VGS

settings = utils.read_settings()

fpi = FPI_2P_VGS(
    [settings.str_row_init_l[0], settings.str_col_init_l[0]],
    [settings.payoff_matrix_row, settings.payoff_matrix_col])
if settings.display_game: fpi.print_game()
fpi.converge(settings.rate, settings.iters)
FPI_2P_VGS.display_eqpt(fpi.eqpt())
if settings.use_LH:
    fpi.lemke_howson()

stats = fpi.get_stats()

import matplotlib.pyplot as plt
plt.figure(figsize=utils.xy_16X9)
plt.plot(np.log(np.array(stats['vgs_row_l'])), color='red', alpha=.5)
plt.plot(np.log(np.array(stats['vgs_col_l'])), color='blue', alpha=.5)
plt.xlabel('iterations', fontsize=utils.label_size)
plt.ylabel('ln(VGS)', fontsize=utils.label_size)
plt.tight_layout()
plt.savefig(settings.png_name + '-vgs.png', bbox_inches='tight')
# plt.show()
