import numpy as np
from FPI_nP import Game, Player
import utils


rate = 10 ** -5

game = Game()

game.let_join(Player(3))
game.let_join(Player(3))
game.let_join(Player(3))
game.let_join(Player(3))
game.let_join(Player(3))
game.let_join(Player(3))

game.build_product_space_of_pures()
game.let_assign_payoff()
game.let_init_mixed_strategies()

vgs_ag_old = 10 ** 10
for i in range(utils.iterations):
    game.let_run_one_iteration(rate)
    vgs_ag_cur = game.vgs_aggregation()
    if vgs_ag_cur < vgs_ag_old:
        eqpt = game.eqpt()
        vgs_ag_old = vgs_ag_cur

game.show_eqpt(eqpt)

# plotting
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
plt.figure(figsize=(utils.xy_x, utils.xy_x))
ax = plt.gca()
triangle = mpatches.Polygon(np.array([[0, 0], [np.sqrt(2) / 2, np.sqrt(6) / 2], [np.sqrt(2), 0]]), fc="gray", alpha=.1)
ax.add_artist(triangle)

plt.setp(ax.get_xticklabels(), visible=False)
plt.setp(ax.get_yticklabels(), visible=False)
for tick in ax.xaxis.get_major_ticks(): tick.set_visible(False)
for tick in ax.yaxis.get_major_ticks(): tick.set_visible(False)
for tick in ax.xaxis.get_minor_ticks(): tick.set_visible(False)
for tick in ax.yaxis.get_minor_ticks(): tick.set_visible(False)
plt.axis('scaled')
plt.xlim(0, np.sqrt(2))
plt.ylim(0, np.sqrt(6) / 2)

data = []
for aplayer in game.players:
    x_a, y_a = utils.barycentric_to_cartesian(np.array(aplayer.path_l))
    ax.plot(x_a, y_a, alpha=.5, zorder=2)
    data.append((np.array(aplayer.path_l).transpose(), np.array(aplayer.vgs_l).round(2)))

plt.tight_layout()
# plt.savefig('nP-path.png', bbox_inches='tight')
plt.show()
utils.write_pickle(data, 'animation_data.pkl')
