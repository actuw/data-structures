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
    resultListAlias = resultList
    resultListAlias.append(input)
    if input == 1:
        return resultListAlias
    if input % 2 > 0:
        input = ((3 * input) + 1)
        collatz_sequence_recursion(input,resultListAlias)
    else:
        input = (input / 2)
        collatz_sequence_recursion(input,resultListAlias)
        
print(collatz_sequence_recursion(7))