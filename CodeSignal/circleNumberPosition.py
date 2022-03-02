def solution(n, firstNumber):
    result = int(firstNumber + n/2)
    if result > n-1:
        result = result - n
    print (result)
    return result



n = 4
firstNumber = 1
solution(n,firstNumber)