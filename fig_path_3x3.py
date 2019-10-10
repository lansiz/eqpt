import sys
import numpy as np
import utils
from FPI_2P import FPI_2P_Stgy
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

plt.figure(figsize=(utils.xy_x, utils.xy_x))
ax = plt.gca()
triangle = mpatches.Polygon(np.array([[0, 0], [np.sqrt(2) / 2, np.sqrt(6) / 2], [np.sqrt(2), 0]]), fc="gray", alpha=.1)
ax.add_artist(triangle)

settings = utils.read_settings()


# run the FPI
for str_row_init, str_col_init in zip(settings.str_row_init_l, settings.str_col_init_l):
    if str_row_init.shape[0] != 3 or str_col_init.shape[0] != 3:
        print('the game must be 3x3 for plotting on 2D-simplex.')
        continue
    fpi = FPI_2P_Stgy([str_row_init, str_col_init], [settings.payoff_matrix_row, settings.payoff_matrix_col])
    if settings.display_game: fpi.print_game()
    fpi.converge(settings.rate, settings.iters)
    FPI_2P_Stgy.display_eqpt(fpi.eqpt())
    if settings.use_LH: fpi.lemke_howson()

    stats = fpi.get_stats()
    # essential: transform point in 2-simplex to 2-D plane
    row_x_a, row_y_a = utils.barycentric_to_cartesian(np.array(stats['str_row_l']))
    col_x_a, col_y_a = utils.barycentric_to_cartesian(np.array(stats['str_col_l']))
    plt.plot(row_x_a, row_y_a, color='red', alpha=.5, zorder=2)
    plt.plot(col_x_a, col_y_a, color='blue', alpha=.5, zorder=2)

for eqpt in settings.eqpts:
    x_row, y_row = utils.barycentric_to_cartesian(eqpt[0])
    x_col, y_col = utils.barycentric_to_cartesian(eqpt[1])
    markersize = 60
    plt.scatter(x_row, y_row, s=markersize, marker='x', color='black', zorder=5)
    plt.scatter(x_col, y_col, s=markersize, marker='x', color='black', zorder=5)


def build_annotation(settings, eqpt_approx):
    text_right = text_left = ''
    text_left += 'payoff matrix:\n'
    text_right += 'payoff matrix:\n'
    for r in settings.payoff_matrix_row:
        text_left += str(r.astype(np.int).tolist())[1:-1] + '\n'
    for r in settings.payoff_matrix_col:
        text_right += str(r.astype(np.int).tolist())[1:-1] + '\n'
    text_left += 'initial strategy:\n'
    text_right += 'initial strategy:\n'
    text_left += str(settings.str_row_init_l[0].tolist())[1:-1]
    text_right += str(settings.str_col_init_l[0].tolist())[1:-1]
    text_left += '\nadjust. rate:%f' % settings.rate
    text_right += '\nadjust. rate:%f' % settings.rate
    text_left += '\niterations:' + str(settings.iters)
    text_right += '\niterations:' + str(settings.iters)
    text_left += '\ntrue EqPt(s):\n'
    text_right += '\ntrue EqPt(s):\n'
    for eq in settings.eqpts:
         text_left += str(eq[0].round(4).tolist())[1:-1] + '\n'
         text_right += str(eq[1].round(4).tolist())[1:-1] + '\n'
    text_left += '\napprox. EqPt:\n'
    text_right += '\napprox. EqPt:\n'
    text_left += str(eqpt_approx[0].round(4).tolist())[1:-1]
    text_right += str(eqpt_approx[1].round(4).tolist())[1:-1]
    text_left += '\nregret sum:'
    text_right += '\nregret sum:'
    text_left += str(eqpt_approx[2].sum().round(4))
    text_right += str(eqpt_approx[3].sum().round(4))
    return text_left, text_right


if settings.annotate_game_details:
    text_l = build_annotation(settings, fpi.eqpt())
    ax.annotate(text_l[0], (0.01, np.sqrt(6) / 2 - 0.01), size=14, color='red', horizontalalignment='left', verticalalignment='top')
    ax.annotate(text_l[1], (np.sqrt(2) - 0.01, np.sqrt(6) / 2 - 0.01), size=14, color='blue', horizontalalignment='right', verticalalignment='top')

plt.setp(ax.get_xticklabels(), visible=False)
plt.setp(ax.get_yticklabels(), visible=False)
for tick in ax.xaxis.get_major_ticks(): tick.set_visible(False)
for tick in ax.yaxis.get_major_ticks(): tick.set_visible(False)
for tick in ax.xaxis.get_minor_ticks(): tick.set_visible(False)
for tick in ax.yaxis.get_minor_ticks(): tick.set_visible(False)
plt.axis('scaled')
plt.xlim(0, np.sqrt(2))
plt.ylim(0, np.sqrt(6) / 2)
plt.tight_layout()
plt.savefig(settings.png_name + '.png', bbox_inches='tight')
# plt.show()
