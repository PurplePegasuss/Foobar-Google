from queue import PriorityQueue
import copy

class Node:
    def __init__(self, position, g,h):
        self.position = position
        self.h = h
        self.g = g
        self.f = g + h

    def __lt__(self, other):
        return (self.f < other.f)

    def __le__(self, other):
        return (self.f < other.f) or (self.f == other.f)


def manhattan_distance(node1_indeces,node2_indeces):
    return abs(node1_indeces[0] - node2_indeces[0]) + \
           abs(node1_indeces[1] - node2_indeces[1])


def choose_direction(dir_number,cur_node):
    if dir_number == 0:
        return [cur_node.position[0]+1,cur_node.position[1]]
    elif dir_number == 1:               
        return [cur_node.position[0],cur_node.position[1]+1]
    elif dir_number == 2:               
        return [cur_node.position[0]-1,cur_node.position[1]] 
    elif dir_number == 3:               
        return [cur_node.position[0],cur_node.position[1]-1]

def check_boundaries(i,j,l,w):
    if i<0 or j<0:
        return False
    if i>=l or j>=w:
        return False
    return True

def A_molod(matrix):
    l = len(matrix)
    w = len(matrix[0])
    start=[0,0]
    finish=[l-1,w-1]
    open = PriorityQueue()
    

    max_int_path = 401
    g_score = [[401 for i in range(w)] for j in range(l)]

    g_score[0][0] = 0

    f_score = [[401 for i in range(w)] for j in range(l)]
    f_score[0][0] = manhattan_distance(start,finish)

    open.put(Node([0,0],g_score[0][0],f_score[0][0]))

    finish_algo = False
    while open.not_empty and not finish_algo:
        current_node = open.get()
        for j in range(4):
            next_pos = choose_direction(j,current_node)
            if check_boundaries(next_pos[0],next_pos[1],l,w):
                if matrix[next_pos[0]][next_pos[1]] != 1:
                    temp_g = current_node.g + 1
                    temp_f = temp_g + manhattan_distance(next_pos,finish)
                    if temp_f < f_score[next_pos[0]][next_pos[1]]:
                        f_score[next_pos[0]][next_pos[1]] = temp_f
                        g_score[next_pos[0]][next_pos[1]] = temp_g
                        open.put(Node(next_pos,temp_g,temp_f))
                    if next_pos == [l-1,w-1]:
                        return temp_g
        if open.qsize() == 0:
            return max_int_path
                        
def at_least_two_zeroes_near(matrix,i,j):
    count_zeros = 0
    l = len(matrix)
    w = len(matrix[0])
    if check_boundaries(i+1,j,l,w) and matrix[i+1][j] == 0:
        count_zeros += 1
    if check_boundaries(i,j+1,l,w) and matrix[i][j+1] == 0:
        count_zeros += 1
    if check_boundaries(i,j-1,l,w) and matrix[i][j-1] == 0:
        count_zeros += 1
    if check_boundaries(i-1,j,l,w) and matrix[i-1][j] == 0:
        count_zeros += 1
    if count_zeros > 1:
        return True
    else:
        return False

def solution(matrix):
    min_shortest_path = 401
    l = len(matrix)
    w = len(matrix[0])
    for i in range(l):
        for j in range(w):
            if matrix[i][j] == 1 and at_least_two_zeroes_near(matrix,i,j):
                new_matrix = copy.deepcopy(matrix)
                new_matrix[i][j] = 0
                shortest_path = A_molod(new_matrix)
                if shortest_path < min_shortest_path:
                    min_shortest_path = shortest_path
    return min_shortest_path + 1

