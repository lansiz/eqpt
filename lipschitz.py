import numpy as np


def distance(n):
    return (1 - 1.0 / n) ** n / (1.0 / n)


a = np.arange(2, 10000)

a = np.apply_along_axis(distance, 0, a)

import matplotlib.pyplot as plt

plt.plot(a)

plt.show()
