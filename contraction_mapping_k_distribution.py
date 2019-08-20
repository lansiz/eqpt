import numpy as np
import utils

r = 10 ** -3
size = 3
samples = 100 * 10 ** 4

vertex_payoff = utils.randomize_payoff_vector(size) * 1
# vertex_payoff = [-685, 808, 415, -805, -342, 620, 242, 153, 739, -468, -968, 236, 734, 214, 565, 194, 189, -456, 596, 183]
print('payoff:', vertex_payoff)


k_l = []
for i in range(samples):
    s1 = utils.randomize_mixed_strategy(size)
    s2 = utils.randomize_mixed_strategy(size)
    distance = np.linalg.norm(s1 - s2)
    payoff_1 = s1.dot(vertex_payoff)
    payoff_2 = s2.dot(vertex_payoff)
    vertex_gain_1 = np.where((vertex_payoff - payoff_1) > 0, vertex_payoff - payoff_1, 0)
    vertex_gain_2 = np.where((vertex_payoff - payoff_2) > 0, vertex_payoff - payoff_2, 0)
    s1_ = utils.vector_update(s1, vertex_gain_1, r)
    s2_ = utils.vector_update(s2, vertex_gain_2, r)
    distance_ = np.linalg.norm(s1_ - s2_)
    k = distance_ / distance
    k_l.append(k)

k_a = np.array(k_l)
print('max %s min %s' % (k_a.max(), k_a.min()))

import matplotlib.pyplot as plt
plt.hist(k_a, bins=50)
plt.show()
