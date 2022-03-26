def solution(n, firstNumber):
    radialPosition = n/2
    diametral = int(firstNumber + radialPosition)
    if diametral > n:
        diametral = diametral - n
    print(diametral)
    return diametral

solution(10,2)