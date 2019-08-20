import numpy as np
import utils

np.printoptions(surpress=True)
np.set_printoptions(formatter={'all': lambda x: str(x)})


class Strategy(object):
    def __init__(self, init_strategy, vertex_payoff, iters, rate, log=True):
        self.init_strategy = init_strategy
        self.vertex_payoff = vertex_payoff
        self.iters = iters
        self.rate = rate
        if log:
            print('***')
            print('initial strategy:', self.init_strategy)
            print('vertex gain:', self.vertex_payoff)
            print('rate: %s iterations: %s' % (self.rate, self.iters))

    def FPI(self):
        s = self.init_strategy
        for i in range(self.iters):
            payoff = s.dot(self.vertex_payoff)
            vertex_gain = np.where((self.vertex_payoff - payoff) > 0, self.vertex_payoff - payoff, 0)
            # vertex_gain = np.apply_along_axis(lambda x: 10 ** 4 * x * x, 0, vertex_gain)
            vertex_gain = np.apply_along_axis(lambda x: x, 0, vertex_gain)
            s = utils.vector_update(s, vertex_gain, self.rate)
        self.vertex_gain = vertex_gain
        self.strategy = s
        self.angle = utils.vector_angle(self.strategy, self.vertex_gain)
        self.payoff = payoff
        self.gamma = vertex_gain.dot(vertex_gain) / (1 / self.rate + vertex_gain.sum())

    def stats(self):
        print('strategy: %s\nvertex gain: %s\npayoff: %s vertex gain sum: %s angle: %s gamma: %s' % (
            self.strategy.tolist(), self.vertex_gain.tolist(), self.payoff, self.vertex_gain.sum(), self.angle, self.gamma))
        print('***')


if __name__ == "__main__":
    size = 6
    strategy = Strategy(
        utils.randomize_mixed_strategy(size),
        utils.randomize_payoff_vector(size) * 100,
        200 * 10 ** 4,
        10 ** -3)

    strategy.FPI()
    strategy.stats()
