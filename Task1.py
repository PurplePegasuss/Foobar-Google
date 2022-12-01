import math

def new_prime(p,len_array,sieve_array):
    p_new = 0
    p_new_index = 0
    
    for j in range(len_array):
        if sieve_array[j] > p:
            p_new = sieve_array[j]
            p_new_index = j
            break
    return p_new,p_new_index

def delete_zeros(array):
    return [str(j) for j in array if j != 0]

def solution(i):
    
    n = 10005
    upperbound_for_n = math.ceil(n*math.log(n) + n*math.log(math.log(n)))
    
    unsieved_array = []
    
    for j in range(2,upperbound_for_n+1):
        unsieved_array.append(j)
    
    p = 2
    p_index = 0
    p_square_constraint = False
    
    while not p_square_constraint:
        for j in range(p_index+1,upperbound_for_n-1):
            if unsieved_array[j] % p == 0:
                unsieved_array[j] = 0
        p,p_index = new_prime(p,upperbound_for_n-1,unsieved_array)
        if p*p > upperbound_for_n:
            p_square_constraint = True
    
    sieved_aray = delete_zeros(unsieved_array)
    print(''.join(sieved_aray)[i:i+5])

solution(3)