def solution(divisor, bound):
    for i in range(bound+1):
        if i % divisor == 0:
            maxNum = i
        #print(i)
    print(maxNum)
    return maxNum
solution(10,50)