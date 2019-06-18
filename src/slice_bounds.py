# Implement the function strStr().
# strStr takes two parameters a main string (haystack) and a substring (needle) 
# and returns the the first index of the match. If there is no match, the function will return -1
# i.e if haystack = "foo bar bar" and needle = "bar"
# the function will return 4

# if the needle is an empty string, the haystack is returned


def strStr(haystack, needle):
    if len(needle) == 0:
        return haystack

    for i in range(len(haystack) - len(needle)):
        if haystack[i: len(needle)] == needle:
            return i
    return -1

print(strStr("endless need for needles", "needle")) # the function should return 17 
