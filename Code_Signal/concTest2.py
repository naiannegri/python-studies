def solution(a, b, k):
    count=0
    b=b[::-1]
    count2=0
    for x,y in zip(a,b):
        print(x,y)
        x=str(x)
        y=str(y)
        xy=x+y
        print(xy)
        xy=int(xy)
        if xy < k:
            count+=1
            print(count)
    return count
    
a=[16, 1, 4, 2, 14]
b=[7, 11, 2, 0, 15]
k=743
solution(a,b,k)