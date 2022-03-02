def solve(A):
    A.sort()
    duracaoTotal = 3
    i = 0
    j = len(A)-1
    countDias=0

    while i <= j:
        countDias += 1
        if A[i]+A[j] <= duracaoTotal:
            i+=1
        j-=1
    print(countDias)


duracoes=[1.90,1.04,1.25,2.5,1.75]
solve(duracoes)