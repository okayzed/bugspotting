def is_palindrome(s, i, j):
    if s[i] != s[j]:
        return False

    return is_palindrome(s, i+1, j-1)

print is_palindrome("foobar", 0, len("foobar") - 1)
print is_palindrome("hannah", 0, len("hannah") - 1)
