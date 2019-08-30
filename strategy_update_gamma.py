import numpy as np
import utils

r = 10 ** -4
size = 6
iterations = 1 * 10 ** 4
s = utils.randomize_mixed_strategy(size)
vertex_payoff = utils.randomize_payoff_vector(size)
# vertex_payoff = np.array([0.1, 0.7, 0.7, 0.7, -2, -1])
vertex_payoff *= 1000
print('initial strategy:', s)
print('payoff:', vertex_payoff)

payoff_old = - 10 ** 8
for i in range(1000):
    payoff = s.dot(vertex_payoff)
    vertex_gain_origin = np.where((vertex_payoff - payoff) > 0, vertex_payoff - payoff, 0)
    vertex_gain = np.apply_along_axis(lambda x: x ** 2, 0, vertex_gain_origin)
    # vertex_gain = np.apply_along_axis(lambda x: x, 0, vertex_gain_origin) #  the vanila
    s = utils.vector_update(s, vertex_gain, r)
    payoff_new = s.dot(vertex_payoff)
    gamma = vertex_gain.dot(vertex_gain_origin) / (1.0 / r + vertex_gain.sum())
    print(payoff_new - payoff - gamma)


print('final strategy:', s)
print('final VG:', vertex_gain)
