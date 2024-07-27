def checkForPalindrome(arr, i):
    n = len(arr)
    if i == n // 2:
        return True
    if arr[i] == arr[n - i - 1]:
        return checkForPalindrome(arr, i + 1)
    else:
        return False


arr = [1, 2, 2, 2, 1]
print(checkForPalindrome(arr, i=0))


def checkForPalindromeForString(s, i):
    n = len(s)
    if i == n // 2:
        return True
    if s[i] == s[n - i - 1]:
        return checkForPalindromeForString(s, i + 1)
    else:
        return False


print(checkForPalindromeForString("ababa", i=0))
