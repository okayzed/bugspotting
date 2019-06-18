def prod(arr, i=0):
    if i >= len(arr):
        return 1

    return arr[i] * prod(arr, i+1)

# if you run this file nothing happens, why?
