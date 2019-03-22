ez = "990" 
iterations = int(1)


def simpleRecursion(n, input):
    ezList = [str(int(i) +1) for i in input] #creating list from input whilst using a counter and type casting
    g = int()
    if ezList[g] == '10': #if number at current index is 10 
        ezList[g] = '1'
        ezList.insert(g+1, '0')
    else:
        ezList[g] = str(int(ezList[g] += 1))
        g += 1
    if n != 0:
        simpleRecursion(n-=1, ezList) #recursive func
    else:
        return 
simpleRecursion(iterations,ez)