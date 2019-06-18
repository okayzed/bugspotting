# this takes in a string like "abc" and
# generates all strings created by inserting
# a space at every position in the string.
# in this case, all strings will be
# "a bc" and "ab c"
# for "abcd", all strings will be
# "a bcd", "ab cd", "abc d"
def generate_all_words(s):
    ret = []
    for i in xrange(1, len(s)-1):
        c = str(s)
        c[i] = " "
        ret.append(c)

    return ret
