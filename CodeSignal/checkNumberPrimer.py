def solution(product):
    if product == 0: return 10
    if product > 1:
        for i in range(2, product):
            if (product % i) == 0:
                break
            else:
                return -1
    for i in range(3600):
        a = 1 
        for j in str(i):
            a *= int(j)
            if a == product: 
                print (i)
                return i




solution(450)