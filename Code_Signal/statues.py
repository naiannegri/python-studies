def solution(statues):
    statues.sort()
    sizeList=len(statues)
    count=0
    for number in statues:
        if count < len(statues)-1:
            if statues[count]+1 < statues[count+1]:
                statues.insert(count+1,statues[count]+1)
            else:
                pass
            count += 1
        else:
            break
        
    result = sizeList - len(statues)
    if result < 0:
        result=-result

    return result

statues=[5, 4, 6]
solution(statues)
