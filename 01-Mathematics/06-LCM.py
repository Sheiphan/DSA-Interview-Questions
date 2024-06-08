def lcm_naive(a, b):
    res = max(a, b)
    while True:
        if res % a == 0 and res % b == 0:
            break
        res += 1
    return res


print(lcm_naive(4, 6))


def hcf_or_gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return hcf_or_gcd_recursive(b, a % b)


def lcm_efficient(a, b):
    return abs(a * b) // hcf_or_gcd_recursive(a, b)


print(lcm_efficient(4, 6))
