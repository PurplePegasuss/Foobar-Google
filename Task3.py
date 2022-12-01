import itertools


def solution(l):
    # Your code here
    sorted_list = sorted(l,reverse=True)
    combinations_len = len(l)

    for j in range(combinations_len,-1,-1):
        generator = itertools.combinations(sorted_list,j)
        for permutation in generator:
            if len(permutation)>1:
                if int(''.join(map(str, permutation))) % 3 == 0:
                    return int(''.join(map(str, permutation)))
            elif len(permutation) == 1:
                if list(permutation)[0] % 3 == 0:
                    return list(permutation)[0]
    return 0


a = solution([6,3,4,2,1])
print(a)