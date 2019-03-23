ez = "990" 
iterations = int(2)


def simpleRecursion(n, input):
    if n > 0:
        ezList = [str(int(i) +1) for i in input] #creating list from input whilst using a counter and type casting
        output = ''.join(ezList)
        print(output)
        n -= 1
        simpleRecursion(n,output)
    else
        return output
simpleRecursion(iterations,ez)