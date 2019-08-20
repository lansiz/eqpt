import numpy as np
import sys
import utils

r = 10 ** -3
size = 3
iterations = 10 * 10 ** 4

s1 = utils.randomize_mixed_strategy(size)
s2 = utils.randomize_mixed_strategy(size)
# s1 = np.array([.5, .5, 0, 0, 0, 0])
# s2 = np.array([0, 0, 0, 0, .5, .5])
print('initial strategy:', s1)
print('initial strategy:', s2)

vertex_payoff = utils.randomize_payoff_vector(size)
# vertex_payoff = np.array([-383, 843, 843])
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
        print(i, 'Lipschitz K>=1, wrong: %s >= %s' % (distance, distance_old))
        sys.exit(1)
    if distance_ratio <= distance_ratio_old:
        print(i, 'Lipschitz K decreasing, unexpected!')
        # sys.exit(1)
    distance_old = distance
    distance_ratio_old = distance_ratio

print('final strategy:', s1, s2)
print('final VG:', vertex_gain_1, vertex_gain_2)


# essential: transform point in 2-simplex to 2-D plane
s1_x_a, s1_y_a = utils.barycentric_to_cartesian(np.array(s1_l))
s2_x_a, s2_y_a = utils.barycentric_to_cartesian(np.array(s2_l))

import matplotlib.pyplot as plt
plt.plot(s1_x_a, s1_y_a, color='red', alpha=.5)
plt.plot(s2_x_a, s2_y_a, color='blue', alpha=.5)
plt.axvline(s1_x_a[-1], color='red', linestyle='dotted', alpha=.3, zorder=-1)
plt.axhline(s1_y_a[-1], color='red', linestyle='dotted', alpha=.3, zorder=-1)
plt.axvline(s2_x_a[-1], color='blue', linestyle='dotted', alpha=.3, zorder=-1)
plt.axhline(s2_y_a[-1], color='blue', linestyle='dotted', alpha=.3, zorder=-1)
import matplotlib.patches as mpatches
ax = plt.gca()
triangle = mpatches.Polygon(np.array([[0, 0], [np.sqrt(2) / 2, np.sqrt(6) / 2], [np.sqrt(2), 0]]), fc="gray", alpha=.2)
ax.add_artist(triangle)
plt.axis('scaled')
plt.xlim(0, np.sqrt(2))
plt.ylim(0, np.sqrt(6) / 2)
plt.tight_layout()
plt.savefig('trajectory_3x3_banach.png')
plt.show()
