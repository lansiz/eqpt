import numpy as np
import argparse
import multiprocessing
from nn import NeuralNetwork
# from gene import Gene
import strengthen_functions
import matplotlib as mpl
mpl.use('Agg', warn=False)
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('-t', action="store", dest="transform_func", default='step')
parser.add_argument('-f', action="store", dest="plasticity_func", default='step')
parser.add_argument('-i', action="store", dest="trails", default=10)
args = parser.parse_args()
transform_func = str(args.transform_func)
plasticity_func = str(args.plasticity_func)
trails = int(args.trails)
pf = plasticity_func

N = 8
delta = 1. / 10 ** 2
# connection_matrix = Gene(N, .7).connections
connection_matrix = np.array([
    [0, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 1, 1],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0]])
# neurons_stimulated_probs = np.random.normal(.6, 0, N)
neurons_stimulated_probs = np.array([.8, .3, .2, .6, .5, .7, .4, .9])


def seek_fp(x):
    nn = NeuralNetwork(connection_matrix, transmission_history_len=10**4)
    nn.set_strengthen_functions(strengthen_functions.__dict__['PF' + str(pf)])
    nn.initialize_synapses_strength(x, .1)
    nn.strengthen_rate = delta
    strength_stats = []
    for _ in range(200000):
        neurons_stimulated = set(np.where(neurons_stimulated_probs > np.random.rand(N))[0])
        nn.propagate_once(neurons_stimulated, transform_func)
        strength_stats.append(nn.stats()['strength'])
    return strength_stats


np.random.seed()
worker_pool = multiprocessing.Pool(processes=10)
xs = np.linspace(0, 1, trails)
results_l = worker_pool.map(seek_fp, xs)

fig, ax = plt.subplots(1, 1, figsize=(6, 2))
for t in range(trails):
    ax.plot(results_l[t])
ax.tick_params(labelsize=8)

# ax.set_ylim(0, 1)
plt.savefig('./png/nn_test_01_pf%s_%s.png' % (pf, transform_func))
# plt.show()
