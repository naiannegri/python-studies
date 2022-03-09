def solution(inputArray, k):
    i = 0
    newList = []
    n=k
    while i <= len(inputArray)-1:
        if i == k-1:
            k+=n
        else:
            newList.append(inputArray[i])
        i+=1
        print(i,k)
    print(newList)
    return newList
    

solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)