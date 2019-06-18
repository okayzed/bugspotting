import sys
sys.setrecursionlimit(5)

def sum(arr, i=0):
    return sum(arr, i+1) + arr[i]

print sum([3, 5, 2])
