import functools
def solution(a, b, c):
    if a==b:
        return c
    elif a==c:
        return b
    else:
        return a

solution(5,5,1)