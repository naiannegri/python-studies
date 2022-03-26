import functools
import math
def truncate(f, n):
    return math.floor(f * 10 ** n) / 10 ** n
def solution(n):
    hour = n/60
    hourMin = str(hour).split(".")
    hour =float(hourMin[0] + '.' + str(int(hourMin[1])*60))
    hourFormat = round(hour,2)
    checkedNew = str(hourFormat).replace(".", "")
    sumValues = functools.reduce(lambda a,b: int(a)+int(b),str(checkedNew))
    print(sumValues)

    return sumValues
solution(240)