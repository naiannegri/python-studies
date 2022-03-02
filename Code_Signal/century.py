def solution(year):
    century = year/100
    int_test = century - int(century)
    int_conv = int(century)
    print(century)
    if int_test == 0: 
        pass
    elif int_test != 0:
        century = int(century)+1
    return print(century)

solution(1905)
