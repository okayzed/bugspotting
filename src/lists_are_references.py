# generates all subsets from array
def all_subsets(arr, i=0, cur=[], output=[]):
    if i >= len(arr):
        output.append(cur)
        return

    all_subsets(arr, i+1, cur, output)

    cur.append(arr[i])
    all_subsets(arr, i+1, cur, output)
    cur.pop()
    return output

# should print the following lists
# [], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]
# but prints [[], [], [], [], [], [], [], []] instead
print all_subsets([1,2,3])
