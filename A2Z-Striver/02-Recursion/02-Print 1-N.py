def printOneToN(i,n):
    if i > n:
        return
    print(i)
    printOneToN(i+1, n)
    
# printOneToN(1, 10)

# Using Backtracking
def printOneToNBack(n):
    if n < 1:
        return
    printOneToNBack(n-1)
    print(n)
    
printOneToNBack(10)