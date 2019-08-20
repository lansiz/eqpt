import numpy as np
import itertools
import utils


class Player(object):
    def __init__(self, pure_strategies_num):
        self.pure_strategies_num = pure_strategies_num
        self.vgs_l = []

    def assign_payoff(self, product_space_size, po_min=-1000, po_max=1000):
        pool = np.arange(po_min, po_max)
        self.payoff_vector = np.random.choice(pool, product_space_size).astype(np.float64)

    def init_mixed_strategies(self):
        self.mixed_strategy = utils.randomize_mixed_strategy(self.pure_strategies_num)

    def run_one_iteration(self, game, rate):
        ''' the core of everything'''
        self.payoff = self.payoff_vector.dot(game.compute_prob_dist())

        prob_dist = np.apply_along_axis(game.compute_prob_dist, 0, np.identity(self.pure_strategies_num), self)
        vertex_payoff = self.payoff_vector.dot(prob_dist)
        temp = vertex_payoff - self.payoff
        self.target = np.where(temp > 0, temp, 0)

        self.mixed_strategy = utils.vector_update(self.mixed_strategy, self.target, rate)

        self.vgs_l.append(self.target.sum())


class Game(object):
    def __init__(self):
        self.players = []
        self.players_num = 0

    def let_join(self, player):
        self.players.append(player)
        self.players_num += 1

    def let_assign_payoff(self):
        for player in self.players:
            player.assign_payoff(len(self.pure_product_space))

    def let_init_mixed_strategies(self):
        for player in self.players:
            player.init_mixed_strategies()

    def build_product_space_of_pures(self):
        temp_l = []
        for player in self.players:
            temp_l.append(set(range(player.pure_strategies_num)))
        self.pure_product_space = list(itertools.product(*temp_l))

    def compute_prob_dist(self, mixed_strategy=None, player=None):
        '''
        when parameter `player` is not given:
        return the prob dist computed from all the players' mixed strategies.
        when parameter `player` is given:
        return the prob dist computed when the player changes its to the one
        specified in the parameter `mixed_strategy` in the meantime the other
        players keep theirs unchanged.
        '''
        prob_dist = np.zeros(len(self.pure_product_space))
        # i: the index of point in the prodcut space
        # j: the index of player
        # k: the index of the pure strategy of player i
        for i, combi in enumerate(self.pure_product_space):
            prob = 1
            for j, k in enumerate(combi):
                if self.players[j] is not player:
                    prob *= self.players[j].mixed_strategy[k]
                else:
                    prob *= mixed_strategy[k]
            prob_dist[i] = prob
        return prob_dist

    def eqpt(self):
        eqpts = [p.mixed_strategy for p in self.players]
        vgs = [p.target for p in self.players]
        return eqpts, vgs

    def vgs_aggregation(self):
        return np.sum([p.target.sum() for p in self.players])

    def show_eqpt(self, eqpt):
        for i, (mixed, vgv) in enumerate(zip(eqpt[0], eqpt[1])):
            print("player %s:" % i, mixed.round(4).tolist())
            print("     VGV:", vgv.round(4).tolist())

    def let_run_one_iteration(self, rate):
        for player in self.players:
            player.run_one_iteration(self, rate)


if __name__ == '__main__':
    rate = 10 ** -5

    game = Game()

    '''
    players_num = 5
    pure_strategies_num = 2
    for i in range(players_num):
        game.let_join(Player(pure_strategies_num))
    '''

    '''
    game.let_join(Player(3))
    game.let_join(Player(3))
    game.let_join(Player(3))
    game.let_join(Player(3))
    '''

    # '''
    game.let_join(Player(2))
    game.let_join(Player(3))
    game.let_join(Player(4))
    game.let_join(Player(5))
    game.let_join(Player(6))
    # '''

    '''
    game.let_join(Player(5))
    game.let_join(Player(6))
    game.let_join(Player(7))
    '''

    '''
    game.let_join(Player(8))
    game.let_join(Player(6))
    '''
    game.build_product_space_of_pures()
    game.let_assign_payoff()
    game.let_init_mixed_strategies()

    vgs_ag_old = 10 ** 10
    for i in range(utils.iterations):
        game.let_run_one_iteration(rate)
        vgs_ag_cur = game.vgs_aggregation()
        if vgs_ag_cur < vgs_ag_old:
            eqpt = game.eqpt()
        vgs_ag_old = vgs_ag_cur

    game.show_eqpt(eqpt)

    # plotting
    import matplotlib.pyplot as plt
    plt.figure(figsize=utils.xy_16X9)
    for player in game.players:
        plt.plot(np.log(player.vgs_l), alpha=.5)
    plt.xlabel('iterations', fontsize=utils.label_size)
    plt.ylabel('ln(VGS)', fontsize=utils.label_size)
    plt.tight_layout()
    plt.savefig('nP.png', bbox_inches='tight')
    plt.show()
