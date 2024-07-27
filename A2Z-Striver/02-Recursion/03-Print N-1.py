def printNtoOne(n):
    if n < 1:
        return
    print(n)
    printNtoOne(n-1)
    
printNtoOne(5)

# Using Backtracking
def printNtoOneBack(i, n):
    if i > n:
        return
    printNtoOneBack(i+1, n)
    print(i)
    
printNtoOneBack(1,10)