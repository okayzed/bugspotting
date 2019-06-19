def sum(arr, i=0):
    if i > len(arr):
        return 0

    return sum(arr, i+1) + arr[i]

print sum([1,2,3])
