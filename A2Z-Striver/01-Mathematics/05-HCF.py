def hcf_or_gcd_recursive(a, b):
    """
    Recursive function to calculate the HCF (Highest Common Factor) or GCD (Greatest Common Divisor)
    of two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The HCF or GCD of the two numbers.
    """
    # Base case: if b is 0, the HCF or GCD is a
    if b == 0:
        return a

    # Recursive case: keep dividing b by a until b becomes 0
    else:
        return hcf_or_gcd_recursive(b, a % b)


def hcf_or_gcd(a, b):
    """
    This function calculates HCF (Highest Common Factor) or GCD (Greatest Common Divisor) of two numbers.

    It starts by finding the minimum of the two numbers. This is the maximum possible GCD. Then it iteratively
    reduces the number by 1 until it finds a number that divides both numbers.

    Args:
        a (int): first number
        b (int): second number

    Returns:
        int: hcf or gcd of the two numbers
    """
    res = min(a, b)
    while res > 0:
        if a % res == 0 and b % res == 0:
            break
        res -= 1
    return res


def hcf_or_gcd_euclidean(a, b):
    """
    Calculate the HCF (Highest Common Factor) or GCD (Greatest Common Divisor)
    of two numbers using the Euclidean method.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The HCF or GCD of the two numbers.
    """
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


print(hcf_or_gcd_euclidean(10, 15))
