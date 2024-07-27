# T:O(n) | S:O(n)
def printNameNTimes(i, n):
    if i > n:
        return
    print("Sheiphan")
    printNameNTimes(i+1, n)

printNameNTimes(1, 5)
