def collatz_sequence(input):
    resultList = []
    while input != 1:
        resultList.append(input)
        if input % 2 > 0:
            input = ((3 * input) + 1)
        else:
            input = (input / 2)
    resultList.append(input)    
    return resultList

print(collatz_sequence(30))

def collatz_sequence_recursion(input, resultList = None):
    if resultList is None:
        resultList = []
    resultList.append(input)
    if input == 1:
        return resultList
    if input % 2 > 0:
        input = ((3 * input) + 1)
        return collatz_sequence_recursion(input,resultList)
    else:
        input = (input / 2)
        return collatz_sequence_recursion(input,resultList)

def collatz_sequence_recursion_glide(input, resultList = None):
    if resultList is None:
        resultList = []
    resultList.append(input)
    if input == 1:
        return resultList
    if input % 2 > 0:
        input = ((3 * input) + 1)
        return collatz_sequence_recursion(input,resultList)
    else:
        input = (input / 2)
        return collatz_sequence_recursion(input,resultList)
        
print(collatz_sequence_recursion(7))


def glide_calc(resultList):
    input = resultList[0]
    while 
    return count
    
    
glide_calc(collatz_sequence_recursion(15))