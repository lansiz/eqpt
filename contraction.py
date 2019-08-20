import utils
import numpy as np


def distance_function_1(strategies_profile_1, strategies_profile_2):
    ''' Euclidean distance function'''
    return np.linalg.norm(strategies_profile_1[0] - strategies_profile_2[0])
    + np.linalg.norm(strategies_profile_1[1] - strategies_profile_2[1])


def distance_function_2(strategies_profile_1, strategies_profile_2):
    ''' derived "max{d1, d2, d3, ...}" distance function'''
    return np.max((
        np.linalg.norm(strategies_profile_1[0] - strategies_profile_2[0]),
        np.linalg.norm(strategies_profile_1[1] - strategies_profile_2[1])))


def FPI_transformation_once(strategies_profile, payoff_matrices, rate):

    str_row, str_col = strategies_profile
    rows = str_row.shape[0]
    cols = str_col.shape[0]
    payoff_matrix_row, payoff_matrix_col = payoff_matrices

    payoff_row = str_row.dot(payoff_matrix_row).dot(str_col.T)
    vertex_payoff_row = np.identity(rows).dot(payoff_matrix_row).dot(str_col.T)
    payoff_gain_row = vertex_payoff_row - payoff_row
    lambda_row = np.where(payoff_gain_row > 0, payoff_gain_row, 0)

    payoff_col = str_col.dot(payoff_matrix_col.T).dot(str_row.T)
    vertex_payoff_col = np.identity(cols).dot(payoff_matrix_col.T).dot(str_row.T)
    payoff_gain_col = vertex_payoff_col - payoff_col
    lambda_col = np.where(payoff_gain_col > 0, payoff_gain_col, 0)

    if False:
        rate_in_use = rate * np.random.rand() * 100
    else:
        rate_in_use = rate

    # alpha function on VGV entrywisely
    # lambda_row_in_use = np.apply_along_axis(alpha, 0, lambda_row)
    # lambda_col_in_use = np.apply_along_axis(alpha, 0, lambda_col)

    # update mixed strategies
    str_row = utils.vector_update(str_row, lambda_row, rate_in_use)
    str_col = utils.vector_update(str_col, lambda_col, rate_in_use)

    return (str_row, str_col)
