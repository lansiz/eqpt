import numpy as np
from strategy import Strategy
import utils
import matplotlib.pyplot as plt
import multiprocessing

trails = 10
processes = 40
size = 6
iters = 10 * 10 ** 4
rate = 10 ** -4

init_strategy = utils.randomize_mixed_strategy(size)
vertex_payoff = utils.randomize_payoff_vector(size)


def approximation(x):
    strategy = Strategy(init_strategy, vertex_payoff * x, iters=iters, rate=rate, log=False)
    strategy.FPI()
    vgs = strategy.vertex_gain.sum()
    gamma = strategy.gamma
    return np.log(vgs), np.log(gamma), np.log(gamma / vgs)


np.random.seed()
worker_pool = multiprocessing.Pool(processes=processes)
xs = np.arange(-20, 21)
xs_e = np.apply_along_axis(lambda x: np.power(np.e, x), 0, xs)
results_l = [worker_pool.apply_async(approximation, (x,)).get() for x in xs_e]

fig, ax = plt.subplots(1, 1, figsize=(6, 2.5))
vertex_gain_a = [i[0] for i in results_l]
gamma_a = [i[1] for i in results_l]
steps_a = [i[2] for i in results_l]
ax.plot(xs, vertex_gain_a, marker='.', color='red', alpha=1, zorder=2)
ax.plot(xs, gamma_a, marker='.', color='green', alpha=1, zorder=2)
ax.plot(xs, steps_a, marker='.', color='blue', alpha=1, zorder=2)
ax.set_xlabel('ln(payoff scale)')
ax.set_ylabel('ln(VGS)')

ax.tick_params(labelsize=8)

plt.grid(True)
plt.tight_layout()
plt.savefig('approximation_by_payoff_scale.png')
plt.show()
