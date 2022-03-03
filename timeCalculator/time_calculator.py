import datetime 


def solve(s, n):
      h, m = map(int, s[:-2].split(':'))
      h %= 12
      if s[-2:] == 'PM':
         h += 12
      t = h * 60 + m + n
      h, m = divmod(t, 60)
      h %= 24
      suffix = 'a' if h < 12 else 'p'
      h %= 12
      if h == 0:
         h = 12
      return "{:02d}:{:02d}{}m".format(h, m, suffix)

def timeConversion(s):
    a, m = s.split(":")
    a = int(a)
    if s[-2:] == 'PM':
        if a != 12:
            a=a+12
            a=str(a)
            return a+":"+m[:-2]
        else:
            return a+":"+m[:-2]
    else:
        if a == 12:
            return "00"+":"+m[:-2]
        else:
            return s[:-2]

def add_time(start, duration, day = ''):
    myDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]*1000
    myTime = start[:-3]
    resultConv = timeConversion(start)
    h, m = resultConv.split(":")
    hSum, mSum = duration.split(":")
    d = datetime.timedelta(hours=int(h), minutes=int(m))
    dSum = datetime.timedelta(hours=int(hSum), minutes=int(mSum))
    dSumMin = dSum.total_seconds()
    min = int(dSumMin // 60)
    resultSum = solve(start,min)
    

    mySumDay = str((datetime.timedelta(hours=int(h), minutes=int(m)) + datetime.timedelta(hours=int(hSum), minutes=int(mSum))))
    mySum = resultSum[:-2]
    myTime = resultSum[-2:]

    if myTime == "am":
        myHour = mySum + " AM" 
    else:
        myHour = mySum + " PM"
    if myHour[0] == "0":
        myHour = myHour[1:]

    if day == '':
        if mySumDay.find("day") > 0:
            days = int(mySumDay[:2])
            if days == 1:
                daysResult = "(next day)"
            else:
                daysResult = "( " + str(days) + " days later)"
        else:
            daysResult = ''
    else:
        day = day.capitalize()
        myHour = myHour + ","
        if mySumDay.find("day") == -1:
            daysResult = day 
        elif mySumDay.find("day") > 0:
            days = int(mySumDay[:2])
            if days == 1:
                daysResult =  day + " (next day)"
            else:
                indexDay = myDays.index(day)
                daysResult =  myDays[indexDay+days-3] + " (" + str(days) + " days later)"

    return (myHour,daysResult)

add_time("8:16 PM", "466:02", "tuesday")