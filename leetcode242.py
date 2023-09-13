class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(list(s)) == sorted(list(t))


s = Solution()
print(s.isAnagram("anagram", "nagaram") == True)
print(s.isAnagram("rat", "car") == False)
