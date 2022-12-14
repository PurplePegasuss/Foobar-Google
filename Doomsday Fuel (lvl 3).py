from fractions import Fraction

def check_if_terminal(state,state_id=0):
    clean_terminal = [0]*len(state)
    loop_terminal = list(clean_terminal)
    loop_terminal[state_id] = 1
    if state == loop_terminal or state == clean_terminal:
        return True
    else:
        return False

def identity_matrix(n):
    return [[1 if i==j else 0 for j in range(n)] for i in range(n)]

def obtain_submatrix(matrix, rows, columns):
    submatrix = []
    for row in rows:
        new_row = []
        for col in columns:
            new_row.append(matrix[row][col])
        submatrix.append(new_row)
    return submatrix

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
    non_terminal_states = []
    if n_states == 1:
        return [1,1]
#   matrix = sort_states(matrix)
    for i in range(n_states):
        if check_if_terminal(matrix[i],i):
            terminal_states.append(i)
        else:
            non_terminal_states.append(i)

    probs_matrix = [calculate_probs(matrix[i]) for i in range(n_states)]
    n_terminal_states = len(terminal_states)

    q = obtain_submatrix(matrix,non_terminal_states,non_terminal_states)
    r = obtain_submatrix(matrix,non_terminal_states,terminal_states)
    i = [calculate_probs(matrix[i])[n_states-n_terminal_states:] for i in range(n_terminal_states-1,n_states)]

    m = substract_two_matrices(identity_matrix(n_states-n_terminal_states),q)
    n = inverse(m)
    b = [[0 for i in range(len(r[0]))] for i in range(len(n))]
    for i in range(len(n[0])):
        for j in range(len(r[0])):
            for k in range(len(r)):
                b[i][j] += n[i][k] * r[k][j]
   
    common_denum_b  = []


    for i in range(len(b[0])):
        common_denum_b.append(b[0][i].denominator)

    lcm = lcm_list(common_denum_b,0)

    results = []
    for i in range(len(b[0])):
        coef = lcm/b[0][i].denominator
        results.append(int(b[0][i].numerator*coef))
    results.append(lcm)

    return results

def gcdd(dem1, dem2):
    if (dem1 == 0):
        return dem2
    else:
        return gcdd(dem2 % dem1, dem1)
 
def lcm_list(array, i):
    if (i+1 == len(array)):
        return array[i]
    b = lcm_list(array, i + 1)
    return int(array[i]*b/gcdd(array[i],b))


def calculate_probs(state_array):
    array_sum = sum(state_array)
    for i in range(len(state_array)):
        if state_array[i] != 0:
            state_array[i] = Fraction(state_array[i],array_sum)
    return state_array

def sort_states(matrix):
    for j in range(1,len(matrix)):
        for i in range(1,len(matrix)):
            prev_state = check_if_terminal(matrix[i-1])
            cur_state = check_if_terminal(matrix[i])
            if prev_state == True and cur_state == False:
                matrix[i-1],matrix[i] = matrix[i],matrix[i-1]
    return matrix


print(solution([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))

