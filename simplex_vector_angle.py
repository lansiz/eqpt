import numpy as np
import strengthen_functions
# import sys
np.set_printoptions(linewidth=np.inf)
import utils

size = 10
r = 0.0001
iters = 3 * 10 ** 4

s = utils.randomize_mixed_strategy(size)
p = utils.randomize_mixed_strategy(size)


s = utils.randomize_mixed_strategy(size)
# s = np.array([.5, .25, 0.25, 0, 0, 0, 0, 0, 0, 0])
s = np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
p = utils.randomize_mixed_strategy(size)
p = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


def target_function(s):
    # t = 2 - s
    # s = np.where(p - s > 0, p - s, 0)
    # t = 0.95 * s + .05
    # t = strengthen_functions.PF15_(s)
    # t = s * p
    # t = strengthen_functions.PF12(s)
    t = strengthen_functions.PF30(s)
    # t = s * s * s + s * s + s
    # t = t / t.sum()
    return t


angle_old = -1
angle_l = []
target_l = []
for i in range(iters):
    target = target_function(s)
    # print(s, target)
    angle = utils.vector_angle(s, target)
    s = utils.vector_update(s, target, r)
    angle_l.append(angle)
    target_l.append((target ** 2).sum())
    if angle >= angle_old:
        print('+', angle_old, angle)
        # print('s', s)
        # print('p', p)
        # print('target', target)
    else:
        print('-', angle_old, angle)
        # print('s', s)
        # print('p', p)
        # print('target', target)
        # break
    angle_old = angle

import matplotlib.pyplot as plt

plt.plot(angle_l)
print('strategy:', s)
print('angle:', angle)
print('target:', target)
plt.plot(angle_l)
# plt.plot(target_l)
plt.grid(True)
plt.show()
