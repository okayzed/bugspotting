def sum(arr):
    s = 0
    i = 0
    while i <= len(arr):
        s += arr[i]
        i += 1

    return s


print sum([1,2,3,4,5])
