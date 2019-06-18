def sum(arr):
    s = 0
    for i in xrange(arr):
        s += arr[i]
    return s

arr = [1,3,5,7,9]
print sum(arr)
