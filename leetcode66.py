from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 0:
            digits.append(1)
            return digits
        val = 1
        for i in range(len(digits), 0, -1):
            if digits[i - 1] + val < 10:
                digits[i - 1] = digits[i - 1] + val
                val = 0
            else:
                digits[i - 1] = 0
                val = 1
        if val == 1:
            digits.insert(0, 1)
        return digits


s = Solution()
r = s.plusOne([4, 3, 2, 1])
print(r == [4, 3, 2, 2])
print(f'{list(r)}\n-----------------\n')

print(s.plusOne([]) == [1])
print('-----------------\n')

print(s.plusOne([9, 9]) == [1, 0, 0])
print('-----------------\n')