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
        collatz_sequence_recursion(input,resultList)
    else:
        input = (input / 2)
        collatz_sequence_recursion(input,resultList)
        
print(collatz_sequence_recursion(7))