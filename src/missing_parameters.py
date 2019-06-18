def is_palindrome(s, i, j):
    if i >= j:
        return True

    if s[i] != s[j]:
        return False

    return is_palindrome(s, i+1, j-1)

print is_palindrome("foobar")
print is_palindrome("hannah")
    
