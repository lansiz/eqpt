import nashpy as nash
import numpy as np


payoff_matrix_row = np.array([
    [-55, 75, 64],
    [-44, 84, -68],
    [37, 14, -62],
    [-76, 78, -30]])
payoff_matrix_col = np.array([
    [22, -33, -17],
    [-53, 73, 31],
    [-8, -39, 34],
    [-30, -69, -33]])

game = nash.Game(payoff_matrix_row, payoff_matrix_col)

print(payoff_matrix_row)
print(payoff_matrix_col)

for i in game.support_enumeration():
    str_row, str_col = i
    payoff_row = str_row.dot(payoff_matrix_row).dot(str_col.T)
    payoff_col = str_col.dot(payoff_matrix_col.T).dot(str_row.T)
    str_row, str_col = (i[0].round(2), i[1].round(2))
    print(str_row, str_col, payoff_row, payoff_col)
