from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        print(nums)
        pos = []
        for i in range(len(nums)):
            if nums[i] == 0:
                pos.append(i)
            else:
                if len(pos) > 0:
                    nums[pos[0]] = nums[i]
                    pos.pop(0)
                    pos.append(i)
                    nums[i] = 0
        print(nums)
        """
        Do not return anything, modify nums in-place instead.
        """

s = Solution()
s.moveZeroes([0, 1, 0, 3, 12])