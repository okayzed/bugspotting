def is_palindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return false
        i += 1
        j -= 1

    return true

is_palindrome("foobar")
is_palindrome("hannah")
