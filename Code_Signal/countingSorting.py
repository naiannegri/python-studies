def countingSort(arr):
    list100 = [0]*100
    sortedList=[]
    for i in range(len(arr)):
        list100[arr[i]] = list100[arr[i]]+1
    for i in range(len(list100)):
        if list100[i] != 0:
            sortedList = sortedList+[i]*list100[i]
    return sortedList



arr = [1,1,3,2,1]
countingSort(arr)