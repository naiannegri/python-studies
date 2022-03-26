def solution(code):
    n = 8
    newList = [code[i:i+n] for i in range(0, len(code), n)]
    print(newList)
    resultAsci = ''
    for number in newList: 
        decimal = int(number,2)
        asci = chr(decimal)
        resultAsci += asci
    print(resultAsci)
    return resultAsci
solution("010010000110010101101100011011000110111100100001")