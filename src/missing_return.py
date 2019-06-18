def find_max(arr):
    maxval = arr[0]
    for val in arr:
        maxval = max(val, maxval)


print find_max([10, 3, 9, 8, 21])
