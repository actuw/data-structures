input = int()
result = []

def input_odd_or_even_check(input):
    return


def collatz_sequence(input):
    resultList = []
    while input != 1:
        resultList.append(input)
        if input % 2 > 0:
            input = ((3 * input) + 1)
        else:
            input = (input / 2)    
    print(str(resultList))

collatz_sequence(30)

        