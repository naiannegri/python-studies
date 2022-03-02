##For inputArray = [3, 6, -2, -5, 7, 3], the output should be 
##solution(inputArray) = 21.

def solution(inputArray):
    max=inputArray[0]*inputArray[1]
    print(sizeList)
    for i in range(len(inputArray)-1):
        test=inputArray[i]*inputArray[i+1]
        if test > max:
            max=test
    print(max)
    return max
a=[3, 6, -2, -5, 7, 3]
solution(a)
    
        
