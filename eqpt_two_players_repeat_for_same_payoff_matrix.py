import numpy as np

# settings
rows = 4
cols = 3
r = 0.01
str_max = 4
payoff_min = -100
payoff_max = 100
# iters = 20000
iters = 4

# prepare the input
pool = np.arange(1, str_max)
str_row = np.random.choice(pool, rows)
str_row = str_row / str_row.sum()
str_col = np.random.choice(pool, cols)
str_col = str_col / str_col.sum()

# pool = np.arange(payoff_min, payoff_max)
# payoff_matrix_row = np.random.choice(pool, rows * cols).reshape((rows, cols))
# payoff_matrix_col = np.random.choice(pool, rows * cols).reshape((cols, rows))

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

print("initial row player strategy:", str_row.round(2))
print("initial column player strategy:", str_col.round(2))
# print("row player payoff matrix:\n", payoff_matrix_row)
# print("column player payoff matrix:\n", payoff_matrix_col.T)

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

    # print(str_row.round(2), str_col.round(2), lambda_row.round(2), lambda_col.round(2))
    # print(str_row, str_col, lambda_row, lambda_col)

    # update mixed strategies of both
    str_row = str_row + r * lambda_row
    str_row = str_row / str_row.sum()

    str_col = str_col + r * lambda_col
    str_col = str_col / str_col.sum()

print(str_row.round(2), str_col.round(2))
print(lambda_row.round(2), lambda_col.round(2))
