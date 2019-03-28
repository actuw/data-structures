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

def collatz_sequence_glide(resultList):
    i = int()
    glideCounter = int()
    while i != len(resultList):
        if resultList[0] > resultList[i]:
            glideCounter += 1
            i += 1
        else:
            i +=1
    return glideCounter

#def collatz_sequence_glide_recursion(resultList):
 #   {
 #       if (resultList[0] > resultList[i])
 #   }


    
print(collatz_sequence_recursion(7))
print(collatz_sequence_glide(collatz_sequence_recursion(3)))