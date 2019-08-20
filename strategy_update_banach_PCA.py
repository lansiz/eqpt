import numpy as np
from sklearn.decomposition import PCA
import sys
import utils

r = 10 ** 3
size = 20
iterations = 5 * 10 ** 4

s1 = utils.randomize_mixed_strategy(size)
s2 = utils.randomize_mixed_strategy(size)
# s1 = np.array([.5, .5, 0, 0, 0, 0])
# s2 = np.array([0, 0, 0, 0, .5, .5])
print('initial strategy:', s1)
print('initial strategy:', s2)

vertex_payoff = utils.randomize_payoff_vector(size)
# dvertex_payoff = np.array([-383, 843, 843])
vertex_payoff *= 1
print('payoff:', vertex_payoff)

distance_ratio_l = []
distance_old = 10 ** 8
distance_ratio_old = 0
s1_l = []
s2_l = []
for i in range(iterations):
    s1_l.append(s1)
    s2_l.append(s2)
    distance = np.linalg.norm(s1 - s2)
    payoff_1 = s1.dot(vertex_payoff)
    payoff_2 = s2.dot(vertex_payoff)
    vertex_gain_1 = np.where((vertex_payoff - payoff_1) > 0, vertex_payoff - payoff_1, 0)
    vertex_gain_2 = np.where((vertex_payoff - payoff_2) > 0, vertex_payoff - payoff_2, 0)
    s1 = utils.vector_update(s1, vertex_gain_1, r)
    s2 = utils.vector_update(s2, vertex_gain_2, r)
    # print(distance)
    distance_ratio = distance / distance_old
    distance_ratio_l.append(distance_ratio)
    # print(distance_ratio)
    if distance >= distance_old:
        print(i, 'Lipschitz K>=1, wrong!')
        sys.exit(1)
    if distance_ratio <= distance_ratio_old:
        print(i, 'Lipschitz K decreasing, unexpected!')
        # sys.exit(1)
    distance_old = distance
    distance_ratio_old = distance_ratio

print('final strategy:', s1, s2)
print('final VG:', vertex_gain_1, vertex_gain_2)


# transform the trajectory to 2-D plane with PCA
print('*** transform trategy vectors to 2-D with PCA ...')
str_row_a = np.array(np.array(s1_l))
pca_row = PCA(n_components=2)
pca_row.fit(str_row_a)
str_row_a = pca_row.transform(str_row_a)

str_col_a = np.array(np.array(s2_l))
pca_col = PCA(n_components=2)
pca_col.fit(str_col_a)
str_col_a = pca_col.transform(str_col_a)

import matplotlib.pyplot as plt
plt.plot([i[0] for i in str_row_a], [i[1] for i in str_row_a], color='red', alpha=.5)
plt.axvline(str_row_a[-1][0], color='red', linestyle='dotted', alpha=.3, zorder=-1)
plt.axhline(str_row_a[-1][1], color='red', linestyle='dotted', alpha=.3, zorder=-1)
plt.plot([i[0] for i in str_col_a], [i[1] for i in str_col_a], color='blue', alpha=.5)
plt.axvline(str_col_a[-1][0], color='blue', linestyle='dotted', alpha=.3, zorder=-1)
plt.axhline(str_col_a[-1][1], color='blue', linestyle='dotted', alpha=.3, zorder=-1)
plt.tight_layout()
plt.savefig('trajectory_PCA_banach.png')
plt.show()
