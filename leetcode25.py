import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(re.findall('[a-z0-9]', s.lower()))
        return s == s[::-1]

s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama") == True)
print(s.isPalindrome("race a car") == False)


