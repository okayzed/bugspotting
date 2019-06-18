# list all duplicate values in arr
def find_duplicates(arr):
    dupes = set()
    seen = {}
    for a in arr:
        if seen[a] == True:
            dupes.add(a)
        else:
            seen[a] = True

    return seen

print find_duplicates([1,2,3,2,4,5,1])
