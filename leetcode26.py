from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        ind = 0
        for i, num in enumerate(nums):
            if i > 0 and nums[ind] != nums[i]:
                nums[ind + 1] = num
                ind = ind + 1

        return ind + 1


s = Solution()
nums = [1, 1, 2]
print(s.removeDuplicates(nums) == 2)

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(s.removeDuplicates(nums) == 5)
