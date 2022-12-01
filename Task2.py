def solution(l, t):
    # Your code here
    min_sum_indexes = [-1,-1]
    min_sum_value = "99100"

    for i in range(len(l)):
        sum = 0
        for j in range(i,len(l)):
            sum += l[j]
            if sum == t and min_sum_value > str(i) + str(j):
                min_sum_indexes = [i,j]
                min_sum_value = str(i) + str(j)

    return min_sum_indexes

 