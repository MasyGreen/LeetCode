from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
            min_len = min(map(lambda x: len(x), strs))
            if min_len == 0:
                return ""
            for i in range(0, min_len + 1):
                s = list(filter(lambda x: x[:i] == strs[0][:i], strs))
                if len(s) < len(strs):
                    return strs[0][:i - 1]
                if i == min_len:
                    return strs[0][:i]

#                print(len(list(s)))
#                print(strs[0][:i])
#        return ""

s = Solution()
print(s.longestCommonPrefix(["ab", "a"]) == "a")
print(s.longestCommonPrefix(["flower", "flow", "flight"]) == "fl")
print(s.longestCommonPrefix(["dog", "racecar", "car"]) == "")
print(s.longestCommonPrefix(["", ""]) == "")
print("end")