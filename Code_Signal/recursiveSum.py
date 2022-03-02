## Write a program that calculates the sum of a list recursively

def showResults (input, output):
    print("Sum of {} is {}".format(input, output))

##################################################
def recursiveSum1 (input):
    ## WRITE YOUR CODE HERE
    if len(input) == 0: 
        return 0
    else:
        return input[0] + recursiveSum1(input[1:])

##################################################
##################################################
def recursiveSum2 (input):
    if len(input) == 0: 
        return 0
    elif type(input[0]) == int:
        return input[0] + recursiveSum2(input[1:])
    else:
        return recursiveSum2(input[0]) + recursiveSum2(input[1:])

    L = [ [1, [2, [3]]], [4, 5, 6], [7, 8, 9]]

##################################################


input_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output_1 = recursiveSum1(input_1) # We expect 45
showResults(input_1, output_1)

input_2 = [1, [2, [3, 4, 5], [6, [7], 8]], 9]
output_2 = recursiveSum2(input_2) # We expect 45
showResults(input_2, output_2)