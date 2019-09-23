import numpy as np
import itertools
import utils


class Player(object):
    def __init__(self, pure_strategies_num):
        self.pure_strategies_num = pure_strategies_num
        self.vgs_l = []
        self.path_l = []

    def assign_payoff(self, product_space_size, po_min=-1000, po_max=1000):
        pool = np.arange(po_min, po_max)
        self.payoff_vector = np.random.choice(pool, product_space_size).astype(np.float64)

    def init_mixed_strategies(self):
        self.mixed_strategy = utils.randomize_mixed_strategy(self.pure_strategies_num)

    def run_one_iteration(self, game, rate, player_index):
        ''' the core of everything
        time complexity: (n-1)g^n multiplications,
        where g is the average of players' pure strategies number
        '''

        # step 1: evalute vertex payoff vector: \vec{v}
        v = []
        for j in np.arange(self.pure_strategies_num):
            vertex_prob_dist = game.compute_joint_dist_on_vertex(player_index, j)
            a_vertex_payoff = vertex_prob_dist.dot(self.payoff_vector)
            v.append(a_vertex_payoff)
        # step 2: compute payoff
        payoff = self.mixed_strategy.dot(v)
        # step 3: compute VGV
        temp = v - payoff
        self.VGV = np.where(temp > 0, temp, 0)
        # step 4: collect stats: VGS and path
        self.vgs_l.append(self.VGV.sum())
        self.path_l.append(self.mixed_strategy)
        # step 5: update strategies
        self.mixed_strategy = utils.vector_update(self.mixed_strategy, self.VGV, rate)


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

    def compute_joint_dist_on_vertex(self, player_index, pure_strategy_index):
        '''
        return the prob dist computed when the player changes its to the one
        specified in the parameter `pure_strategy_index` in the meantime the other
        players keep theirs unchanged.
        index i: for player
        index j: for pure strategies of player i
        index k: for the combination of pure strategies in `pure_product_space` and `prob_dict`
        time complexity: (n-1)g^(n-1) multiplications
        '''

        prob_dist = np.zeros(len(self.pure_product_space))
        for k, combi in enumerate(self.pure_product_space):
            # ignore those combination without `pure_strategy_index` in it,
            # leaving its prob. slot in `prob_dist` to zero
            if combi[player_index] != pure_strategy_index:
                continue
            prob = 1
            # there are g^(n-1) combinations surviving here
            for i, j in enumerate(combi):
                if i == player_index and j == pure_strategy_index:
                    # equivalent to multiplying by 1, which is the vertex prob.
                    pass
                else:
                    # real deal: there are n-1 multiplications
                    prob *= self.players[i].mixed_strategy[j]
            prob_dist[k] = prob
        return prob_dist

    def eqpt(self):
        eqpts = [p.mixed_strategy for p in self.players]
        vgs = [p.VGV for p in self.players]
        return eqpts, vgs

    def vgs_aggregation(self):
        return np.sum([p.VGV.sum() for p in self.players])

    def show_eqpt(self, eqpt):
        for i, (mixed, vgv) in enumerate(zip(eqpt[0], eqpt[1])):
            print("player %s:" % i, mixed.round(4).tolist())
            print("     VGV:", vgv.round(4).tolist())

    def let_run_one_iteration(self, rate):
        '''time complexity: n(n-1)g^n multiplications
        multiprocessing would be nice here, supposedly reducing O(n^2g^n) to O(ng^n)
        '''

        for i, player in enumerate(self.players):
            player.run_one_iteration(self, rate, i)


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
