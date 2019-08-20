import numpy as np
import utils
from FPI_2P import FPI_2P_Stgy
import matplotlib.pyplot as plt
import contraction

plt.figure(figsize=(utils.xy_x, utils.xy_x))

settings = utils.read_settings()

# run the FPI
fpi = FPI_2P_Stgy([settings.str_row_init_l[0], settings.str_col_init_l[0]], [settings.payoff_matrix_row, settings.payoff_matrix_col])
if settings.display_game: fpi.print_game()
fpi.converge(settings.rate, settings.iters)
FPI_2P_Stgy.display_eqpt(fpi.eqpt())
if settings.use_LH: fpi.lemke_howson()

stats = fpi.get_stats()
str_row_l = stats['str_row_l']
str_col_l = stats['str_col_l']

d_l = []
for i in range(1, settings.iters):
    tuple_i = (str_row_l[i], str_col_l[i])
    tuple_i_minus_1 = (str_row_l[i - 1], str_col_l[i - 1])
    d_l.append(contraction.distance_function_1(tuple_i_minus_1, tuple_i))

q_l = []
for i in range(1, len(d_l)):
    q_l.append(d_l[i] / d_l[i - 1])


d_l = [np.log(i) for i in d_l]
d_a = np.array([None] + d_l)
# q_l = [np.log(i) for i in q_l]
q_a = np.array([None] + q_l + [None])

import matplotlib.pyplot as plt
plt.figure(figsize=utils.xy_16X9)
ax1 = plt.gca()
ax1.plot(d_a, color='blue', alpha=.5)
ax1.set_xlabel('iterations', size=utils.label_size)
ax1.set_ylabel(r'ln($\dot{d}$)', size=utils.label_size, color='blue')
ax1.tick_params('y', colors='blue')
ax2 = ax1.twinx()
ax2.plot(q_a, color='red', alpha=.5)
ax2.set_ylabel(r'$\dot{q}$', size=utils.label_size, color='red')
ax2.tick_params('y', colors='red')
# plt.grid(True)
plt.tight_layout()
plt.savefig(settings.png_name + '-metric.png', bbox_inches='tight')
# plt.show()
