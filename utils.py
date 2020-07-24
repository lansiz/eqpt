import numpy as np
from sklearn.decomposition import PCA
import argparse
import importlib
import pickle

np.printoptions(surpress=True)
np.set_printoptions(formatter={'all': lambda x: str(x)})
np.random.seed()

label_size = 14
iterations = 10 ** 5
xy_16X9 = (8, 4.5)
xy_x = 8


def read_settings():
    parser = argparse.ArgumentParser(description='Approximate a 2-Player Nash Eq. Pt.')
    parser.add_argument(
        'settings', metavar='GAME_SETTING_PY_FILE_BASENAME', type=str, nargs=1,
        help='game setting .py file in subdir `games` ...')
    args = parser.parse_args()
    setting_python_file = args.settings[0]
    settings = importlib.import_module('games.' + setting_python_file)
    return settings


# prepare the initial strategies
# and the str_max parameter decides how 'skew' the prob. proportion is.
def randomize_mixed_strategy(n, str_max=100):
    pool = np.arange(1, str_max)
    str_ = np.random.choice(pool, n)
    str_ = str_ / str_.sum()
    str_ = str_.round(4)
    str_[0] += 1 - str_.sum()
    return str_.astype(np.float64)


def randomize_payoff_matrix(rows, cols, po_min=-1000, po_max=1000):
    pool = np.arange(po_min, po_max)
    return (
        np.random.choice(pool, rows * cols).reshape((rows, cols)).astype(np.float64),
        np.random.choice(pool, rows * cols).reshape((rows, cols)).astype(np.float64))


def randomize_payoff_vector(n, po_min=-1000, po_max=1000):
    pool = np.arange(po_min, po_max)
    return np.random.choice(pool, n).astype(np.float64)


def vector_angle(a, b):
    if a.sum() * b.sum():
        angle = (a * b).sum() / ((a ** 2).sum() ** 0.5) / ((b ** 2).sum() ** 0.5)
        return np.min((angle, 1))  # sometimes numpy give cos value exceeding 1
    else:
        return 0


def vector_update(a, b, r):
    a = a + r * b
    a = a / a.sum()  # transform it to point in simplex
    # a = a / np.linalg.norm(a)  # transform it to unit vector
    return a


def barycentric_to_cartesian(strategy_a):
    barycentric_x = np.array([0, np.sqrt(2) / 2, np.sqrt(2)]).T
    barycentric_y = np.array([0, np.sqrt(6) / 2, 0]).T
    return strategy_a.dot(barycentric_x), strategy_a.dot(barycentric_y)


def pca_2d(data):
    pca = PCA(n_components=2)
    pca.fit(data)
    return pca.transform(data)


def pca_3d(data):
    pca = PCA(n_components=3)
    pca.fit(data)
    return pca.transform(data)


def pick_a_neighour(arr, devi=.01):
    size = arr.shape[0]
    disc = (np.random.rand(size) - .5) * 2 * devi
    added = arr + disc
    return added / added.sum()


def read_pickle(file_name):
    try:
        f = open('./' + file_name, 'rb')
        o = pickle.load(f)
        f.close()
        return o
    except:
        return None


def write_pickle(o, file_name):
    try:
        f = open('./' + file_name, 'wb')
        pickle.dump(o, f, pickle.HIGHEST_PROTOCOL)
        f.close()
        return True
    except:
        return False
