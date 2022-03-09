import itertools

def solution(inputArray):
    perm = list(itertools.permutations(inputArray))
    for array in perm:
        if stringsRearrange(array) == True:
            return True
    return False


def stringsRearrange(perm):
    for i in range(len(perm)-1):
        if sum([a != b for a, b in zip(perm[i], perm[i + 1])]) != 1:
            return False
    return True




    
solution(["ab", "bb", "aa"])
