def duplicate(numbers):
    # Time = O(n)
    # Space = O(n)
    arr = []
    for i in range(len(numbers)):
        if numbers[i] not in arr:
            arr.append(numbers[i])
        else:
            return numbers[i]

def duplicateXOR(numbers):
    xor_value = numbers[0]
    for i in range(1, len(numbers)):
        xor_value = xor_value ^ numbers[i]
    for j in range(1, len(numbers)):
        xor_value = xor_value ^ j

    return xor_value
num = [1,2,4,2,3,5]
print(duplicate(num))
print(duplicateXOR(num))