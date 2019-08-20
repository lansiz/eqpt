import numpy as np
import sys
import utils

r = 10 ** -4
size = 10
iterations = 10 * 10 ** 4
s = utils.randomize_mixed_strategy(size)
vertex_payoff = utils.randomize_payoff_vector(size)
print('initial strategy:', s)
print('payoff:', vertex_payoff)


vg_old = 10 ** 8
angle_old = -1
payoff_old = - 10 ** 8
angle_decrease_iterations = 0
vgs_l = []
for i in range(iterations):
    payoff = s.dot(vertex_payoff)
    vertex_gain = np.where((vertex_payoff - payoff) > 0, vertex_payoff - payoff, 0)
    # important: vg must be decreasing all the time
    vg = vertex_gain.sum()
    if vg > vg_old:
        print(i, 'vg increases, and that is wrong!')
        sys.exit(1)
    # and meanwhile payoff should be increasing all the time
    if payoff < payoff_old:
        print(i, 'payoff decreases, and that is wrong!')
        sys.eixt(1)
    # print(payoff)
    # print(s.tolist(), vertex_gain.tolist())
    # print(vertex_gain.round(2))
    angle = utils.vector_angle(s, vertex_gain)
    # print(angle_old, angle)
    if angle > angle_old and i > 0:
        angle_decrease_iterations += 1
    '''
    if i > iterations - 1000:
        print(i, angle - angle_old)
    '''
    payoff_old = payoff
    angle_old = angle
    vg_old = vertex_gain.sum()
    vgs_l.append(vg_old)
    # step update of vector
    s = utils.vector_update(s, vertex_gain, r)
print('final strategy:', s)
print('final VG:', vertex_gain)
print('final angle:', angle)
print('angle decreases iterations: %s/%s' % (angle_decrease_iterations, iterations))

import matplotlib.pyplot as plt
# plt.plot(np.log(np.array(vgs_l)))
plt.plot(np.array(vgs_l))
plt.show()
