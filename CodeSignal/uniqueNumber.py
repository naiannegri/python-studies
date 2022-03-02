import collections
def lonelyinteger(a):
    # Write your code here
    dict = collections.Counter(a)
    listNumbers = [*dict.keys()]
    listValues = [*dict.values()]
    count=0
    print(listNumbers)
    for number in listValues:
        if number == 1: 
            uniqueValue = listNumbers[count]
        count+=1
    print(uniqueValue)
    return uniqueValue

a=[1,2,3,4,3,2,1]
lonelyinteger(a)