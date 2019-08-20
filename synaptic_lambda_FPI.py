import numpy as np
import strengthen_functions
import utils

# s = utils.randomize_mixed_strategy(2)
s = np.random.rand()
s = np.array([s, 1 - s])
print(s)
s_l = []
for i in range(10 ** 5):
    target = strengthen_functions.PF80(s[0])
    target = np.array([target, 1 - target])
    s = utils.vector_update(s, target, 10 ** -4)
    s_l.append(s)

import matplotlib.pyplot as plt

print(s_l[-1])
plt.scatter([i[0] for i in s_l], [i[1] for i in s_l])
plt.show()
