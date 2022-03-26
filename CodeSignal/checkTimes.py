def solution(min1, min2_10, min11, s):
    sumValues = 0
    countTimes = 0
    while sumValues < s:
        countTimes += 1
        if countTimes == 1:
            sumValues += min1
        elif 2 <= countTimes <= 10: 
            sumValues += min2_10
        elif countTimes >= 11: 
            sumValues += min11
        if sumValues > s:
            countTimes -= 1
            
            
        print(countTimes, sumValues)
        
    print(countTimes, sumValues)
    return countTimes

solution(2,2,1,24)
#solution(3,1,2,20)
#solution(1,2,1,6)
#solution(2,2,1,2)
solution(10,1,2,22)