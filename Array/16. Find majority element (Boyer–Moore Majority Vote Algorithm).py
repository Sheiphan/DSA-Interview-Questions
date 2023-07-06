# majority element -> frequency > n/2
def majorityBruteForce0(nums):
    # Time: O(n^2)
    # Space: O(1)
    max_count = 0
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[i] == nums[j]:
                count += 1
                if count > len(nums) // 2:
                    return nums[j]


def majorityElement(nums):
    # Time: O(n)
    # Space: O(n)
    hashmap = {}
    n = len(nums)

    for i in range(n):
        current_number = nums[i]
        if current_number not in hashmap:
            hashmap[current_number] = 1
        else:
            hashmap[current_number] += 1
        if hashmap[current_number] > n // 2:
            return current_number


# Boyer-Moore Algorithm
def boyerMooreAlgo(nums):
    # Time: O(n)
    # Space: O(1)
    candidate = count = 0
    for i in range(len(nums)):
        if count == 0:
            candidate = nums[i]
        if nums[i] == candidate:
            count += 1
        else:
            count -= 1
    return candidate


def mostFrequentBruteForce(nums):
    max_count = 0
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[i] == nums[j]:
                count += 1
        max_count = max(count, max_count)
        if count == max_count:
            ans = nums[i]
    return ans


arr = [7, 7, 7, 7, 8, 2, 2, 2]
print(majorityBruteForce0(arr))
print(boyerMooreAlgo(arr))
