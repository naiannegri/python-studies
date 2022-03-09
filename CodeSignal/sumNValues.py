def solution(inputArray, k):
    maxValue=sum(inputArray[:k])
    maxV = maxValue
    for i in range(len(inputArray)-k):
        maxValue += (inputArray[i+k] - inputArray[i])
        if maxV < maxValue:
            maxV = maxValue
        print(inputArray[i+k], inputArray[i])
    return maxV

solution([2, 3, 5, 1, 6],2)