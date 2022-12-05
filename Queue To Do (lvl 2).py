def solution(first_worker_id,checkpoint):
    backwards_checkpoint = checkpoint
    calculate_checksum = 0
    while backwards_checkpoint != 0:
        calculate_checksum ^= xor_o1(first_worker_id) ^ xor_o1(first_worker_id + backwards_checkpoint)
        backwards_checkpoint -= 1
        first_worker_id += checkpoint
    return calculate_checksum
    
def xor_o1(n) :
    if n == 0:
        return 0
    n = n - 1

    if n % 4 == 0 :
        return n

    if n % 4 == 1 :
        return 1
 
    if n % 4 == 2 :
        return n + 1
    return 0
