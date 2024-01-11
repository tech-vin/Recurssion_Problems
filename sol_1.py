def fact(n):
    if (n == 0):
        return 1

    return n * fact(n-1)

testcases = [5, 7, 10, 2]
print([fact(n) for n in testcases])