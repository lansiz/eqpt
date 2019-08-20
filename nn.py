# !/usr/bin/env python
#  -*- coding: utf-8 -*-
from __future__ import print_function
import numpy as np
import strengthen_functions


class Queue_(object):
    def __init__(self, qlen):
        self.records = np.array([0] * qlen, dtype=np.int8)


class NeuralNetwork(object):
    def __init__(self, connection_matrix, transmission_history_len=10**4):
        if connection_matrix.shape[0] != connection_matrix.shape[1]:
            print('connection matrix should be squared')
            return None
        self.connection_matrix = connection_matrix
        self.N = self.connection_matrix.shape[0]
        self.connections_number = self.connection_matrix.sum()
        # print(N)
        # each synapse has a recording queue for its transmission in the tempral order.
        # value 1 represents the occurance of transmission
        self.transmission_history_len = transmission_history_len
        self.transmission_history_pointer = 0
        self.transmission_history_m = self.connection_matrix.copy().astype(object)
        for i in range(self.N):
            for j in range(self.N):
                if self.connection_matrix[i][j] == 1:
                    self.transmission_history_m[i][j] = Queue_(self.transmission_history_len)
                else:
                    self.transmission_history_m[i][j] = None
        # interations already done.
        self.strengthen_rate = 1. / self.transmission_history_len
        self.iter = 0

    def initialize_synapses_strength(self, mean=.5, std=.3):
        '''
        initialized N ** 2 synaptic stength
        the strength of no-exisiting synapse are set to NaN.
        this method should be reimplemented in sub-class.
        '''
        tmp_m = np.random.normal(mean, std, (self.N, self.N))
        tmp_m = np.where(tmp_m <= 1, tmp_m, 1)
        tmp_m = np.where(tmp_m >= 0, tmp_m, 0)
        self.connection_strength_m = np.where(self.connection_matrix == 1, tmp_m, -1)
        # self.connection_strength_m_origin = self.connection_strength_m.copy()

    def initialize_synapses_strength_uniform(self):
        tmp_m = np.random.normal(0, 1, (self.N, self.N))
        self.connection_strength_m = np.where(self.connection_matrix == 1, tmp_m, -1)

    def set_strengthen_functions(self, pf=strengthen_functions.PF34):
        '''
        initialized N ** 2 strengthen functions
        the functions of no-exisiting synapse are set to NaN.
        this method should be reimplemented in sub-class.
        '''
        self.strengthen_functions_m = np.where(
            self.connection_matrix == 1, pf, '----')

    def show_strengthen_functions_matrix(self):
        ''' display strengthen functions in prettier matrix '''
        strengthen_functions_m = self.strengthen_functions_m.copy()
        for i in range(self.N):
            for j in range(self.N):
                val = self.strengthen_functions_m[i][j]
                if val != '----':
                    strengthen_functions_m[i][j] = val.func_name
        print(strengthen_functions_m)

    def propagate_once(self, neurons_stimulated, func_name='step'):
        '''
        This is the core of things.
        propagate all stimulus in a pool at a once.
        and update connections strength according to their transmission frequency.
        '''
        self.iter += 1
        neurons_fired = neurons_stimulated
        neurons_newly_propagated = neurons_fired
        for i in range(self.N):
            for j in range(self.N):
                if self.transmission_history_m[i][j]:
                    self.transmission_history_m[i][j].records[self.transmission_history_pointer] = 0
        while len(neurons_newly_propagated):
            neurons_propagated = set([])
            for i in neurons_newly_propagated:
                for j, strength in enumerate(self.connection_strength_m[i]):
                    if strength < 0:
                        continue
                    r = np.random.rand()
                    if strength > r:
                        neurons_propagated.add(j)
                        self.transmission_history_m[i][j].records[self.transmission_history_pointer] = 1
            neurons_newly_propagated = neurons_propagated - neurons_fired
            neurons_fired = neurons_fired.union(neurons_propagated)
        if self.iter > self.transmission_history_len:
            for i in range(self.N):
                for j in range(self.N):
                    if not self.connection_matrix[i][j]: continue
                    frequency = self.transmission_history_m[i][j].records.sum() / float(self.transmission_history_len)
                    target_strength = self.strengthen_functions_m[i][j](frequency)
                    current_strength = self.connection_strength_m[i][j]

                    # here different transformation is tested
                    self.connection_strength_m[i][j] = self.__getattribute__('transform_' + func_name)(current_strength, target_strength)

        self.transmission_history_pointer = (self.transmission_history_pointer + 1) % self.transmission_history_len

    def transform_step(self, current, target):
        if target > current:
            return np.min((current + self.strengthen_rate, 1))
        else:
            return np.max((0, current - self.strengthen_rate))

    def transform_target(self, current, target):
        return target

    def transform_converge(self, current, target):
        if target > current:
            return np.min((current + self.strengthen_rate, target))
        else:
            return np.max((target, current - self.strengthen_rate))

    def transform_uniform(self, current, target):
        if target > current:
            return np.random.uniform(current, 1)
        else:
            return np.random.uniform(0, current)

    def transform_between(self, current, target):
        if target > current:
            return np.random.uniform(current, target)
        else:
            return np.random.uniform(target, current)

    # addtion of step vector: a/(1+a)
    def transform_vector(self, current, target):
        a = .01
        return current + a / (1 + a) * (target - current)

    def get_transmission_frequency(self):
        '''
        reduce the history record of connections transmission to frequency scalar.
        '''
        transmission_frequency = np.zeros((self.N, self.N))
        for i in range(self.N):
            for j in range(self.N):
                if self.transmission_history_m[i][j]:
                    transmission_frequency[i][j] = self.transmission_history_m[i][j].records.sum() / float(self.transmission_history_len)
        return transmission_frequency.round(4)

    def stats(self):
        connection_strength_m = np.where(self.connection_strength_m >= 0, self.connection_strength_m, 0)
        return {
            'strength_matrix': self.connection_strength_m,
            'strength': connection_strength_m.sum() / self.connections_number}

    def stats_square_mean(self):
        connection_strength_m = np.where(self.connection_strength_m >= 0, self.connection_strength_m, 0)
        return {
            'strength_matrix': self.connection_strength_m,
            'strength': np.square(connection_strength_m).sum() / self.connections_number}

    def propagate_test(self, neurons_stimulated):
        neurons_fired = neurons_stimulated
        neurons_newly_propagated = neurons_fired
        connections_propagated = 0
        while len(neurons_newly_propagated):
            neurons_propagated = set([])
            for i in neurons_newly_propagated:
                for j, strength in enumerate(self.connection_strength_m[i]):
                    if strength < 0:
                        continue
                    r = np.random.rand()
                    if strength > r:
                        neurons_propagated.add(j)
                        connections_propagated += 1
            neurons_newly_propagated = neurons_propagated - neurons_fired
            neurons_fired = neurons_fired.union(neurons_propagated)
        return connections_propagated


if __name__ == "__main__":
    pass
