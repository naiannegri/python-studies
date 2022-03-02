def solution(a):
    minSum = 1000000
    minNumber = 0
    if len(a) <= 1:
        return a[0]
    i = 0 
    testValue = 0
    for i in range(len(a)):
        testValue = 0
        for j in range(len(a)):
            if i != j:
                testValue += abs(a[j] - a[i])
                print(i,j,testValue)
        if testValue < minSum:
            minSum = testValue
            minNumber = a[i]
    print(minNumber)
    return minNumber
    
a = [-10, -10, -10, -10, -10, -9, -9, -9, -8, -8, -7, -6, -5, -4, -3, -2, -1, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
solution(a)

