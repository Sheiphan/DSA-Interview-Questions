def subarrayWithGivenSum(k, arr):
    n = len(arr)
    maxCount = 0
    for i in range(n):
        count = 0
        sumTillNow = 0
        for j in range(i, n):
            sumTillNow += arr[j]
            count += 1
            if sumTillNow == k:
                maxCount = max(maxCount, count)

    return maxCount


k = 10
arr = [2, 3, 5, 1, 9]
print(subarrayWithGivenSum(k, arr))


def getLongestusingPrefixSum(arr, k):
    prefix_sum = {}
    Sum = 0
    max_length = 0
    
    for i in range(len(arr)):
        Sum += arr[i]
        
        # Check if the current sum is equal to k
        if Sum == k:
            max_length = i + 1
        
        # If the sum - k is in the prefix_sum, update the max_length
        if (Sum - k) in prefix_sum:
            max_length = max(max_length, i - prefix_sum[Sum - k])
        
        # Only add the sum to prefix_sum if it is not already there
        # to ensure we get the longest sub-array
        if Sum not in prefix_sum:
            prefix_sum[Sum] = i
    
    return max_length


def getLongestSubarray(a, k):
    n = len(a)  # size of the array.

    left, right = 0, 0  # 2 pointers
    Sum = a[0]
    maxLen = 0
    while right < n:
        # if sum > k, reduce the subarray from left
        # until sum becomes less or equal to k:
        while left <= right and Sum > k:
            Sum -= a[left]
            left += 1

        # if sum = k, update the maxLen i.e. answer:
        if Sum == k:
            maxLen = max(maxLen, right - left + 1)

        # Move forward the right pointer:
        right += 1
        if right < n:
            Sum += a[right]

    return maxLen


if __name__ == "__main__":
    a = [1, 2, 3, 1, 1, 1, 1, 4, 2, 3]
    k = 3

    length = getLongestSubarray(a, k)
    print(f"The length of the longest subarray is: {length}")
    getLongestusingPrefixSum(a, k)
