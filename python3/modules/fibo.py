def printAllFib(n):
    a, b = 0, 1
    for i in range(n):
        print(a, "   ")
        next_term = a+b;
        a = b;
        b = next_term

printAllFib(5)


