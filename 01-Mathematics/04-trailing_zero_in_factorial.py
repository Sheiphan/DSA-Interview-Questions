def count_trailing_zero_in_factorial(n):
    """
    Counts the number of trailing zeros in a factorial of a given number.

    Args:
        n (int): The number for which to count the trailing zeros.

    Returns:
        int: The number of trailing zeros.
    """
    count = 0

    # Initialize a variable to represent the number 5, which will be used to
    # check for trailing zeros.
    i = 5

    while n / i >= 1:
        # Increment the count by the integer division of n by i. This is done to
        # account for the number of times i will divide n without leaving a
        # remainder.
        count += int(n / i)

        # Multiply i by 5 to move to the next power of 5.
        i *= 5

    return count


print(count_trailing_zero_in_factorial(10))
