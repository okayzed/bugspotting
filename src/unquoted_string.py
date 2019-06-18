# returns if string s has the string 'needle' in it
# i.e. has_needle("has needle") should return True
# has_needle("foobar") should return False
def has_needle(s):
    return s.find(needle) != -1


print has_needle("foobar")
print has_needle("has a needle")
