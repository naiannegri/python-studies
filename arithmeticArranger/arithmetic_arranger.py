def arithmetic_arranger(arr,val=False):
    rightFormat = []
    listArr = []
    dashes = []
    bottomDown = []
    bottomUp = []
    result = []
    count2=0
    if len(arr) > 5:
        return "Error: Too many problems."
    for operations in arr:
        #turns the values into a list 
        operators = operations.split(" ")

        ##checks if operators are only '+' and '-'
        if operators[1] != "+" and  operators[1] != "-":
            return "Error: Operator must be '+' or '-'."
        
        ##check if there's only digits
        if operators[0].isdigit() == False or operators[2].isdigit() == False:
            return "Error: Numbers must only contain digits."
        
        ##counts digits return error if more than 4
        for items in operators:
            count = 0
            for numbers in items:
                count += 1
            if count > 4: 
                return "Error: Numbers cannot be more than four digits."

        ##do the operation
        if operators[1] == "+":
            calcResult = int(operators[0]) + int(operators[2])
        else:
            calcResult = int(operators[0]) - int(operators[2])
        
        #returns results in the right format
        if len(operators[0]) > len(operators[2]):
            maxLen = len(operators[0])
            minLen = len(operators[2])
        else:
            maxLen = len(operators[2])
            minLen = len(operators[0])
        dashes.append("-"*(maxLen+2))
        spacemaxUp = " " * (abs(len(operators[0]) - len(dashes[count2])))
        spacemaxUnder = " " * (abs(len(operators[2]) - len(dashes[count2])) - 1)
        spaceResult = " "* (abs(len(str(calcResult)) - len(dashes[count2])))
        bottomUp.append(spacemaxUp + operators[0])
        bottomDown.append(operators[1] + spacemaxUnder + operators[2])
        result.append(spaceResult + str(calcResult))
        count2 += 1
    bottomUp1 = '    '.join(bottomUp)
    bottomDown1 = '    '.join(bottomDown)
    dashes1 = '    '.join(dashes)
    result1 = '    '.join(result)
    if val: 
        arranged_problems = bottomUp1 +'\n' + bottomDown1 + '\n' + dashes1 + '\n' + result1
    else:
        arranged_problems = bottomUp1 +'\n' + bottomDown1 + '\n' + dashes1 


    return arranged_problems