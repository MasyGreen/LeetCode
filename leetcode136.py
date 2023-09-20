from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        while len(nums) != 1:
            s = nums[0]
            nums.remove(s)
            try:
                nums.remove(s)
            except:
                return s
        return nums[0]


        return []


s = Solution()

print(s.singleNumber([2, 2, 1]) == 1)
print(s.singleNumber([4, 1, 2, 1, 2]) == 4)
print(s.singleNumber([2]) == 2)
