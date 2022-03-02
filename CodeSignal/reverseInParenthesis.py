import re
def reverseParentheses(inputString):
    list={}
    count=0
    for name in inputString:
        if name == "(":
            count+=1
    print(count)
    if count==1:
        for i in range(len(inputString)):
            if inputString[i] == "(":
                start = i
                #print (inputString[:start])
            if inputString[i] == ")":
                end = i
                list[inputString[start+1:end]]=inputString[start+1:end][::-1]
    else: 
        for i in range(len(inputString)):
            inputString=reverseParentheses(inputString)
    print(list)
    return list

def writeWord(inputString):
    listRev=reverseParentheses(inputString)
    keys2 = listRev.keys()
    values = listRev.values()
    #print(listRev)
    for i in listRev:
        rx = r"" + re.escape(i)
        inputString = re.sub(rx,listRev[i],inputString)
    table = re.sub(r"[()]", "", inputString)
    print(table)
    print(inputString)
    return inputString


inputString = "foo(bar(baz))blim"
writeWord(inputString)