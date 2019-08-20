import numpy as np
import nashpy

# np.printoptions(surpress=True)
np.set_printoptions(formatter={'all': lambda x: str(x)})
np.random.seed()

# settings
rows = 8
cols = 8
r = 0.00001
str_max = 4
payoff_min = -1000
payoff_max = 1000
iters = 400000
# iters = 4

# prepare the input
pool = np.arange(1, str_max)
str_row = np.random.choice(pool, rows)
str_row = str_row / str_row.sum()
str_col = np.random.choice(pool, cols)
str_col = str_col / str_col.sum()
str_row_orig = str_row
str_col_orig = str_col
# print(str_row.round(2), str_col.round(2))
# print("initial row player strategy:", str_row.round(2))
# print("initial column player strategy:", str_col.round(2))

pool = np.arange(payoff_min, payoff_max)
payoff_matrix_row = np.random.choice(pool, rows * cols).reshape((rows, cols))
payoff_matrix_col = np.random.choice(pool, rows * cols).reshape((cols, rows))

'''
payoff_matrix_row = np.array([
    [-55, 75, 64],
    [-44, 84, -68],
    [37, 14, -62],
    [-76, 78, -30]])
payoff_matrix_col = np.array([
    [22, -33, -17],
    [-53, 73, 31],
    [-8, -39, 34],
    [-30, -69, -33]]).T
'''
# print("row player payoff matrix:\n", payoff_matrix_row)
# print("column player payoff matrix:\n", payoff_matrix_col.T)


def vector_angle(a, b):
    return (a * b).sum() / ((a ** 2).sum() ** 0.5) / ((b ** 2).sum() ** 0.5)


# stats
angle_row = []
angle_col = []
SVG_row = []  # sum of vertex gain
SVG_col = []
# here we go for iterations
for i in range(iters):
    payoff_row = str_row.dot(payoff_matrix_row).dot(str_col.T)
    payoff_pure_row = np.identity(rows).dot(payoff_matrix_row).dot(str_col.T)
    payoff_gain = payoff_pure_row - payoff_row
    lambda_row = np.where(payoff_gain > 0, payoff_gain, 0)

    payoff_col = str_col.dot(payoff_matrix_col).dot(str_row.T)
    payoff_pure_col = np.identity(cols).dot(payoff_matrix_col).dot(str_row.T)
    payoff_gain = payoff_pure_col - payoff_col
    lambda_col = np.where(payoff_gain > 0, payoff_gain, 0)

    angle_row.append(vector_angle(str_row, lambda_row))
    angle_col.append(vector_angle(str_col, lambda_col))
    SVG_row.append(lambda_row.sum())
    SVG_col.append(lambda_col.sum())

    if iters - i < 10:
        print(str_row.round(4), str_col.round(4), lambda_row.round(4), lambda_col.round(4))
    # print(str_row, str_col, lambda_row, lambda_col)

    # the following transformation to point in simplex has two aspects:
    # 1. 1-norm of target vector is constantly 1 and hence doesn't shrink to zero.
    # 2. It brings the zero-vector difficulties, which make the lambda equation conditional.
    if False:
        if lambda_row.sum():
            lambda_row = lambda_row / lambda_row.sum()
        else:
            # lambda is zero vector
            pass
        if lambda_col.sum():
            lambda_col = lambda_col / lambda_col.sum()
        else:
            # lambda is zero vector
            pass

    # update mixed strategies of both
    str_row = str_row + r * lambda_row
    str_row = str_row / str_row.sum()

    str_col = str_col + r * lambda_col
    str_col = str_col / str_col.sum()

np.save('angle_row', angle_row)
np.save('angle_col', angle_col)
np.save('SVG_row', SVG_row)
np.save('SVG_col', SVG_col)
print(str_row_orig.round(4), str_col_orig.round(4))
print(payoff_matrix_row)
print(payoff_matrix_col.T)

game = nashpy.Game(payoff_matrix_row, payoff_matrix_col.T)
for i, item in enumerate(game.support_enumeration()):
    str_row_, str_col_ = item
    payoff_row = str_row_.dot(payoff_matrix_row).dot(str_col_.T).round(2)
    payoff_col = str_col_.dot(payoff_matrix_col).dot(str_row_.T).round(2)
    payoff_pure_row = np.identity(rows).dot(payoff_matrix_row).dot(str_col_.T)
    payoff_pure_col = np.identity(cols).dot(payoff_matrix_row).dot(str_row_.T)
    str_row_, str_col_ = (item[0].round(4), item[1].round(4))
    payoff_gain = payoff_pure_row - payoff_row
    lambda_row_ = np.where(payoff_gain > 0, payoff_gain, 0)
    lambda_col_ = np.where(payoff_gain > 0, payoff_gain, 0)
    payoff_gain = payoff_pure_col - payoff_col
    print('EQPT %s: ' % i, str_row_, str_col_, 'DIFF', lambda_row_.round(8), lambda_col_.round(8))

print('We found:')
print(str_row.round(4), str_col.round(4), lambda_row.round(4), lambda_col.round(4))
