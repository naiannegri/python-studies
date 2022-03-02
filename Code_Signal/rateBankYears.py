def solution(deposit, rate, threshold):
    i = 0
    while deposit <= threshold:
        deposit += deposit*(rate/100)
        i+=1
    print (i)
    return i


deposit = 100
rate = 
threshold = 170
solution(deposit,rate,threshold)