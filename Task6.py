from fractions import Fraction, gcd
import math
from functools import reduce

def check_if_terminal(state,state_id):
    clean_terminal = [0]*len(state)
    loop_terminal = list(clean_terminal)
    loop_terminal[state_id] = 1
    if state == loop_terminal or state == clean_terminal:
        return True
    else:
        return False

def identity_matrix(n):
    return [[1 if i==j else 0 for j in range(n)] for i in range(n)]


def transpose_matrix(matrix):
    return map(list,zip(*matrix))

def substract_rows(row1, row2, column_number, pivot):
    if not isinstance(row2[column_number], Fraction):
        row2[column_number] = Fraction.from_float(row2[column_number])
    if not isinstance(row1[column_number], Fraction):
        row1[column_number] = Fraction.from_float(row1[column_number])
    if not isinstance(pivot, Fraction):
        pivot = Fraction.from_float(pivot)

    coefficient = (row2[column_number] - pivot) / row1[column_number]
    for i in range(len(row1)):
        row2[i] -= coefficient * row1[i]

def gauss(matrix):
    for i in range(len(matrix)):
        if matrix[i][i] == 0:
            for j in range(i+1, len(matrix)):
                if matrix[i][j] != 0:
                    matrix[i], matrix[j] = matrix[j], matrix[i]
                    break
        for j in range(i+1, len(matrix)):
            substract_rows(matrix[i], matrix[j], i,0)
    for i in range(len(matrix)-1, -1, -1):
        for j in range(i-1, -1, -1):
            substract_rows(matrix[i], matrix[j], i,0)
    for i in range(len(matrix)):
        substract_rows(matrix[i], matrix[i], i, 1)
    return matrix

def inverse(matrix):
    matrix_inverse = [[0 for j in range(len(matrix)*2)] for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)*2):
            if j >= len(matrix):
                if i == j - len(matrix):
                    matrix_inverse[i][j] = 1
            if j < len(matrix):
                matrix_inverse[i][j] = matrix[i][j]
    gauss(matrix_inverse)
    result = []
    for i in range(len(matrix_inverse)):
        result.append(matrix_inverse[i][len(matrix_inverse[i])//2:])
    return result

def substract_two_matrices(matrix1,matrix2):
    n = len(matrix1)
    new_matrix = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            new_matrix[i][j] = matrix1[i][j] - matrix2[i][j]
    return new_matrix

def solution(matrix):
    n_states = len(matrix)
    terminal_states = []
    
    for i in range(n_states):
        if check_if_terminal(matrix[i],i):
            terminal_states.append(i)
    probs_matrix = [calculate_probs(matrix[i]) for i in range(n_states)]
    n_terminal_states = len(terminal_states)
    q = [calculate_probs(matrix[i])[:n_states-n_terminal_states] for i in range(n_states-n_terminal_states)]
    r = [calculate_probs(matrix[i])[n_states-n_terminal_states:] for i in range(n_states-n_terminal_states)]
    i = [calculate_probs(matrix[i])[n_states-n_terminal_states:] for i in range(n_terminal_states-1,n_states)]

    m = substract_two_matrices(identity_matrix(n_states-n_terminal_states),q)
    n = inverse(m)
    b = [[0 for i in range(len(r[0]))] for i in range(len(n))]
    for i in range(len(n[0])):
        for j in range(len(r[0])):
            for k in range(len(r)):
                b[i][j] += n[i][k] * r[k][j]
    x = reduce(gcd, [9,3])
    array_of_denums = []
    for i in range(len(b[0])):
        array_of_denums.append(b[0][i].denominator)

def calculate_probs(state_array):
    array_sum = sum(state_array)
    for i in range(len(state_array)):
        if state_array[i] != 0:
            state_array[i] = Fraction(state_array[i],array_sum)
    return state_array

solution([[0, 2, 1, 0, 0],
          [0, 0, 0, 3, 4],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0]])

