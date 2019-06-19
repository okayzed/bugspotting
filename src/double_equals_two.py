def find_max(arr):
    maxval = arr[0]
    for a in arr:
        maxval == max(maxval, a)

    return maxval


print find_max([1,3,5,10])
