def solution(inputArray):
    sum=0
    q = inputArray[0]
    for i in inputArray[1:]:
        if i <= q:
            sum += q-i+1
            q=q+1
        else:
            q=i
    print(sum)
    return sum
inputArray=[2, 3, 2]
solution(inputArray)