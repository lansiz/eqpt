import numpy as np
import strengthen_functions
# import sys
import utils

r = 10 ** -5
size = 2
iterations = 1 * 10 ** 4
lambda_function = strengthen_functions.PF12
s1 = utils.randomize_mixed_strategy(size)
s2 = utils.randomize_mixed_strategy(size)
# s1 = np.array([0.5, 0.5, 0, 0, 0, 0])
# s2 = np.array([0, 0, 0, 0, 0.5, 0.5])
print('initial strategy:', s1)
print('initial strategy:', s2)

distance_l = []
distance_old = 10 ** 8
for i in range(iterations):
    target_1 = np.array([lambda_function(s1[0]), 1 - lambda_function(s1[0])])
    target_2 = np.array([lambda_function(s2[0]), 1 - lambda_function(s2[0])])
    s1 = utils.vector_update(s1, target_1, r)
    s2 = utils.vector_update(s2, target_2, r)
    distance = np.linalg.norm(s1 - s2)
    distance_l.append(distance / distance_old)
    if distance > distance_old:
        print(i, '+', distance_old, distance)
    else:
        print(i, '-', distance_old, distance)
    distance_old = distance
    # print(distance)

print(distance_l[-100:])
print('final strategy:', s1.round(2), s2.round(2))
# print('final VG:', vertex_gain_1, vertex_gain_2)
# import matplotlib.pyplot as plt
# plt.plot(distance_l)
# plt.show()
