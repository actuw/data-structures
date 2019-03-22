ez = "56890" 
counter = int(0)


def simpleRecursion(n, input):
    ezList2 = []
    if n == 9: #checking if number of iterations has gotten to 10
        ez = str("".join(ezList2)) #combining list back to string
        print(ez)
    else:
        ezList = [int(i) for i in input] #creating list from input
        ezList2 = [y +1 for y in ezList] #creating new list to add to
        n += 1
        g = int()
        while g < len(ezList2): #while counter is less then length of list
            if ezList2[g] == 10: #if number at current index is 10 
                ezList2[g] = 1
                ezList2.insert(g+1, 0)
            else:
                g += 1
        simpleRecursion(n, ezList2) #recursive func
        return 
simpleRecursion(counter,ez)