import numpy as np
import sys
import utils

r = 10 ** -8
size = 10
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
for i in range(iterations):
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
        print(i, 'distance is not decreasing!')
        sys.exit(1)
    if distance_ratio <= distance_ratio_old:
        print(i, 'distance_ratio is not increasing')
        # sys.exit(1)
    distance_old = distance
    distance_ratio_old = distance_ratio

print('final strategy:', s1, s2)
print('final VG:', vertex_gain_1, vertex_gain_2)

print(distance_ratio_l[-100:])

import matplotlib.pyplot as plt
plt.plot(np.log(np.array(distance_ratio_l)))
plt.show()
