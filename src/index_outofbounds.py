# Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).
# Input: [1,3,5,4,7]
# Output: 3


def lcis(arr):
    i = 0
    cur_count = 0
    max_count = 0

    while (i < len(arr)):
        if arr[i] < arr[i+1]:
            cur_count += 1
            max_count = max(cur_count, max_count)
        i += 1

    return max_count

print(lcis([1,3,5,4,7]))
