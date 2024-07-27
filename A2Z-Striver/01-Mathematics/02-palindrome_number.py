def check_palindrome(num):
    """
    Check if a given number is a palindrome.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is a palindrome, False otherwise.

    Algorithm:
        1. Initialize a variable `rev` to store the reversed number.
        2. Initialize a variable `temp` to store the original number.
        3. While `num` is greater than 0:
            - Calculate the last digit of `num` using `num % 10`.
            - Multiply `rev` by 10 and add the last digit.
            - Divide `num` by 10 to remove the last digit.
        4. Compare `temp` with `rev` to check if the number is a palindrome.

    Example:
        >>> check_palindrome(121)
        True
        >>> check_palindrome(123)
        False
    """
    rev = 0
    temp = num
    while num > 0:
        rev = rev * 10 + num % 10
        num = num // 10
    return temp == rev


print(check_palindrome(121))
