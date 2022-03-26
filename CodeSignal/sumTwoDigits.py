import functools
def solution(n):
    sumValues = functools.reduce(lambda a,b: int(a)+int(b),str(n))
    print(sumValues)
    return sumValues
solution(29)