import numpy as np
import utils
from FPI_2P import FPI_2P_Stgy

settings = utils.read_settings()

# run the FPI
fpi = FPI_2P_Stgy([settings.str_row_init, settings.str_col_init], [settings.payoff_matrix_row, settings.payoff_matrix_col])
fpi.converge(settings.rate, settings.iters)
FPI_2P_Stgy.display_eqpt(fpi.eqpt())

stats = fpi.get_stats()
# transform the trajectory to 2-D plane with PCA
print('*** transform trategy vectors to 3-D with PCA ...')
str_row_a = utils.pca_3d(np.array(stats['str_row_l']))
str_col_a = utils.pca_3d(np.array(stats['str_col_l']))

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(utils.xy_x, utils.xy_x))
ax = fig.gca(projection='3d')

ax.plot(
    [i[0] for i in str_row_a],
    [i[1] for i in str_row_a],
    zs=[i[2] for i in str_row_a],
    zdir='z', color='red', alpha=.5)
end = str_row_a[-1]
ax.scatter([end[0]], [end[1]], s=16, zs=[end[2]], zdir='z', color='red', alpha=1)

ax.plot(
    [i[0] for i in str_col_a],
    [i[1] for i in str_col_a],
    zs=[i[2] for i in str_col_a],
    zdir='z', color='blue', alpha=.5)
end = str_col_a[-1]
ax.scatter([end[0]], [end[1]], s=16, zs=[end[2]], zdir='z', color='blue', alpha=1)

plt.tight_layout()
plt.savefig(settings.png_name + '.png', bbox_inches='tight')
# plt.show()
