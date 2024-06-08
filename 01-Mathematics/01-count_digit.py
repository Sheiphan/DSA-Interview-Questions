def count_digit(n):
    """
    Calculates the number of digits in a given positive integer.

    Parameters:
        n (int): The positive integer to count the digits of.

    Returns:
        int: The number of digits in the given integer.
    """
    count = 0
    while n != 0:
        n = n // 10
        count += 1
    return count


number = 1234
print(count_digit(number))
