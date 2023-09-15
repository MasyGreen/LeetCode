class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        pos = s.strip()[::-1]
        if len(pos) == 0:
            return 0
        if pos.find(" ") == -1:
            return len(pos)
        else:
            return pos.find(" ")

s = Solution()
print(s.lengthOfLastWord(" a") == 1)
print(s.lengthOfLastWord("Hello World") == 5)
print(s.lengthOfLastWord("   fly me   to   the moon  ") == 4)
print(s.lengthOfLastWord("luffy is still joyboy") == 6)