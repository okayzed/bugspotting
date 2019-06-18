class Solution:
    def is_palindrome(s):
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True

s = Solution()
print s.is_palindrome("foobar")
print s.is_palindrome("hannah")
