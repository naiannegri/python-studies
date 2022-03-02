def solution(numbers, left, right):
    list=[]
    for i in range(len(numbers)):
        x = numbers[i]/(i+1)
        print(x)
        if x >= left and x <= right and x % 1 == 0:
            list.append(True)
        else:
            list.append(False)
    print(list)
        
numbers = [8, 5, 6, 16, 5]
left = 1
right = 3
solution(numbers,left,right)