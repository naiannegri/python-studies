def timeConversion(s):
    # Write your code here
    if s[-2:] == 'PM':
        a=int(s[:2])
        if a != 12:
            print(a)
            a=a+12
            a=str(a)
            print(a+s[2:-2])
            return a+s[2:-2]
        else:
            print(s[:-2])
            return s[:-2]
    else:
        a=int(s[:2])
        if a == 12:
            print("00"+s[2:-2])
            return "00"+s[2:-2]
        else:
            print(s[:-2])
            return s[:-2]

s="12:01:00PM"
timeConversion(s)
