import datetime
import numpy as np
import utils

np.printoptions(surpress=True)
np.set_printoptions(formatter={'all': lambda x: str(x)})
np.random.seed()


class FPI_2P(object):
    def __init__(self, init_strategies, payoff_matrices):

        self.str_row, self.str_col = init_strategies
        self.payoff_matrix_row, self.payoff_matrix_col = payoff_matrices
        self.rows = self.str_row.shape[0]
        self.cols = self.str_col.shape[0]

        self.stats = {}

        self.use_random_rate = False

    def print_game(self):
        print('*** game settings:')
        print(self.str_row.round(4))
        print(self.str_col.round(4))
        print(self.payoff_matrix_row)
        print(self.payoff_matrix_col)

    # this is the core of algorithm
    def converge(self, rate, iterations):
        vgss_old = 10 ** 15
        start_time = datetime.datetime.now()
        self.init_stats()
        for i in range(iterations):
            vertex_payoff_row = self.payoff_matrix_row.dot(self.str_col.T)
            payoff_row = self.str_row.dot(vertex_payoff_row)
            payoff_gain_row = vertex_payoff_row - payoff_row
            self.lambda_row = np.where(payoff_gain_row > 0, payoff_gain_row, 0)

            vertex_payoff_col = self.payoff_matrix_col.T.dot(self.str_row.T)
            payoff_col = self.str_col.dot(vertex_payoff_col)
            payoff_gain_col = vertex_payoff_col - payoff_col
            self.lambda_col = np.where(payoff_gain_col > 0, payoff_gain_col, 0)

            # update the sucklest strategy that has the smallest VGS
            vgss = self.lambda_row.sum() + self.lambda_col.sum()
            if vgss < vgss_old:
                self.eqpt_row = self.str_row
                self.eqpt_col = self.str_col
                self.eqpt_lambda_row = self.lambda_row
                self.eqpt_lambda_col = self.lambda_col
                vgss_old = vgss

            # collect stats to return
            self.collect_stats()

            '''
            # if random rate is used, it is not FPI anymore since there is no fixed function to be considered.
            if self.use_random_rate:
                rate_in_use = rate * np.random.rand() * 100
            else:
                rate_in_use = rate
            '''

            # alpha function on VGV entrywisely
            lambda_row_in_use = np.apply_along_axis(self.alpha, 0, self.lambda_row)
            lambda_col_in_use = np.apply_along_axis(self.alpha, 0, self.lambda_col)

            # update mixed strategies
            if type(rate) is list or type(rate) is tuple:
                self.str_row = utils.vector_update(self.str_row, lambda_row_in_use, rate[0])
                self.str_col = utils.vector_update(self.str_col, lambda_col_in_use, rate[1])
            else:
                self.str_row = utils.vector_update(self.str_row, lambda_row_in_use, rate)
                self.str_col = utils.vector_update(self.str_col, lambda_col_in_use, rate)

        stop_time = datetime.datetime.now()
        print('*** rate: %s iters: %s time: %s' % (rate, iterations, stop_time - start_time))

    def alpha(self, x):
        """ alpha helps little on approximation precision. """
        """ it will make the math more interpretable though. """
        # return 0.01 * x * x
        # return 0.1 * x
        # return 10 ** 4 * x
        # return 0.01 * x
        return x

    def init_stats(self):
        pass

    def collect_stats(self):
        pass

    def get_stats(self):
        return self.stats

    def eqpt(self):
        try:
            return (self.eqpt_row, self.eqpt_col, self.eqpt_lambda_row, self.eqpt_lambda_col)
            # return (self.eqpt_row, self.eqpt_col, self.eqpt_lambda_row.sum(), self.eqpt_lambda_col.sum())
        except AttributeError:
            return (None, None, None, None)

    def lemke_howson(self, method='lemke_howson'):
        try:
            import nashpy
        except ModuleNotFoundError:
            print('Error: Python library `nashpy` must be installed to use Lemke-Howson algorithm.')
            print('       And command `pip install nashpy` will install it.')
            import sys
            sys.exit(1)
        game = nashpy.Game(self.payoff_matrix_row, self.payoff_matrix_col)
        if method == 'lemke_howson':
            eqpts = game.lemke_howson_enumeration()
        elif method == 'support_enumeration':
            eqpts = game.support_enumeration()
        elif method == 'vertex_enumeration':
            eqpts = game.vertex_enumeration()
        else:
            print('whatever')
            import sys
            sys.exit(1)
        print(method, 'algorithm found:')
        for i, item in enumerate(eqpts):
            print('EQPT %s:' % i, item)

    @classmethod
    def display_eqpt(cls, eqpt_l):
        print('rEQPT:', eqpt_l[0].round(4).tolist())
        print('rVGV: ', eqpt_l[2].round(4).tolist())
        print('cEQPT:', eqpt_l[1].round(4).tolist())
        print('cVGV: ', eqpt_l[3].round(4).tolist())
        print('VGS:  %s %s' % (np.round(np.sum(eqpt_l[2]), 4), np.round(np.sum(eqpt_l[3]), 4)))


class FPI_2P_Stgy(FPI_2P):
    def init_stats(self):
        self.stats['str_row_l'] = []
        self.stats['str_col_l'] = []

    def collect_stats(self):
        self.stats['str_row_l'].append(self.str_row)
        self.stats['str_col_l'].append(self.str_col)


class FPI_2P_VGS(FPI_2P):
    def init_stats(self):
        self.stats['vgs_row_l'] = []
        self.stats['vgs_col_l'] = []

    def collect_stats(self):
        self.stats['vgs_row_l'].append(self.lambda_row.sum())
        self.stats['vgs_col_l'].append(self.lambda_col.sum())
