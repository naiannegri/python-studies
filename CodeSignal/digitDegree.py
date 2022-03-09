def recursiveSum1 (input):
    ## WRITE YOUR CODE HERE
    if len(input) == 0: 
        return 0
    else:
        return input[0] + recursiveSum1(input[1:])
counter=[0]
def solution(n):
    strNum = str(n)
    listVal = []
    for number in strNum:
        numInt = int(number)
        listVal.append(numInt)
    if len(listVal) <= 1:
        print(counter[0])
        return counter[0]
    else:
        counter[0]+=1
        sumVal = recursiveSum1(listVal)
        result = solution(sumVal)
    return counter[0]


solution(100)