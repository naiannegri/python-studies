def solution(inputString):
    na=[p.split(')')[0] for p in inputString.split('(') if ')' in p]
    so=re.sub("[\(\[].*?[\)\]]", "", inputString)
    indices = [i for i, x in enumerate(inputString) if x == "("]

    count=0
    naRev=[]
    result=[]
    for names in na:
        inv=names[::-1]
        naRev.append(inv)
        print(naRev)
    #firstHalf=inputString[:number]
    for number in indices:
        if len(number) == 1: 
            return so[:number]+naRev[count]+so[number:]
        else:
            return 

        count+=1
        print(result)
    

inputString="bar(foo(foo(bar)baz(blim)))bar"
solution(inputString)
