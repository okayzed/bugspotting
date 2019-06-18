class Solution:
    def is_palindrome(self, s):
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True

print Solution.is_palindrome("foobar")
print Solution.is_palindrome("hannah")

