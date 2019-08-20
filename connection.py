# !/usr/bin/env python
#  -*- coding: utf-8 -*-
import numpy as np
import strengthen_functions


class Queue_(object):
    def __init__(self, qlen):
        self.records = np.array([0] * qlen, dtype=np.int8)


class Connection(object):
    def __init__(self, init_strength=np.random.rand(), pf=strengthen_functions.PF34, transmission_history_len=10**4):
        # value 1 represents the occurance of transmission
        self.strength = init_strength
        self.transmission_history_len = transmission_history_len
        self.transmission_history_pointer = 0
        self.transmission_history = Queue_(self.transmission_history_len)
        self.strengthen_function = pf
        self.strengthen_rate = float(1) / self.transmission_history_len
        self.iter = 0

    def propagate_once(self, stimulus_prob, func_name='step', debug=False, return_target_strength=False):
        self.iter += 1
        target_strength = 0
        frequency = 0
        self.transmission_history.records[self.transmission_history_pointer] = 0
        if stimulus_prob > np.random.rand():
            if self.strength > np.random.rand():
                self.transmission_history.records[self.transmission_history_pointer] = 1
        if self.iter > self.transmission_history_len:
            frequency = self.transmission_history.records.sum() / float(self.transmission_history_len)
            target_strength = self.strengthen_function(frequency)
            current_strength = self.strength

            # here different transformation is tested
            self.strength = self.__getattribute__('transform_' + func_name)(current_strength, target_strength)

        self.transmission_history_pointer = (self.transmission_history_pointer + 1) % self.transmission_history_len

        if return_target_strength: return target_strength, frequency

    def get_frequency(self):
        return self.transmission_history.records.sum() / float(self.transmission_history_len)

    def get_strength(self):
        return self.strength

    # the original one used for the paper
    def transform_step(self, current, target):
        if target > current:
            return np.min((current + self.strengthen_rate, 1))
        else:
            return np.max((0, current - self.strengthen_rate))

    # fixed point iteration. Failed to simulate strength divergence for PF16-18
    def transform_target(self, current, target):
        return target

    # convergence: make sure s' is between s and s^*
    def transform_converge(self, current, target):
        if target > current:
            return np.min((current + self.strengthen_rate, target))
        else:
            return np.max((target, current - self.strengthen_rate))

    # convergence: make sure s' is between s and s^*
    def transform_between(self, current, target):
        if target > current:
            return np.random.uniform(current, target)
        else:
            return np.random.uniform(target, current)

    # simulation shows convergence anyway, which sucks.
    def transform_uniform(self, current, target):
        if target > current:
            return np.random.uniform(current, 1)
        else:
            return np.random.uniform(0, current)

    # addtion of step vector: a/(1+a)
    def transform_vector(self, current, target):
        a = 1
        return current + a / (1 + a) * (target - current)


if __name__ == "__main__":
    pass
