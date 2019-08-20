import numpy as np
import utils

r = 10 ** -5
size = 3
iterations = 1 * 10 ** 4

s1 = utils.randomize_mixed_strategy(size)
s2 = utils.randomize_mixed_strategy(size)
print('initial strategy:', s1)
print('initial strategy:', s2)
vertex_payoff = utils.randomize_payoff_vector(size) * 1
print('payoff:', vertex_payoff)

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
    distance_ratio = distance / distance_old
    if distance >= distance_old:
        print(i, 'Lipschitz K>=1, wrong: %s > %s' % (distance, distance_old))
    if distance_ratio <= distance_ratio_old:
        print(i, 'Lipschitz K decreasing: %s > %s' % (distance_ratio, distance_ratio_old))
    distance_old = distance
    distance_ratio_old = distance_ratio

print('final strategy:', s1, s2)
print('final VG:', vertex_gain_1, vertex_gain_2)
