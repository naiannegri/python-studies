def solution(value1, weight1, value2, weight2, maxW):
    totalWeight = [weight1,weight2]
    totalValue = [value1,value2]
    sumWeight = sum(totalWeight)
    if sumWeight <= maxW:
        result = sum(totalValue)
    else:
        if totalValue[0] > totalValue[1]:
            if totalWeight[0] <= maxW:
                result = totalValue[0]
            elif totalWeight[1] <= maxW:
                result = totalValue[1]
            else:
                result = 0
        else:
            if totalWeight[1] <= maxW:
                result = totalValue[1]
            elif totalWeight[0] <= maxW:
                result = totalValue[0]
            else:
                result = 0
    print(result)
    return result


solution(2,5,3,4,5)