from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        print(f'{nums=}, {target=}')
        f = list(filter(lambda s: s <= target, nums))
        if target == 0 or len(f) == 0:
            return 0
        if f[-1] == target:
            print(f'X {len(f)=}')
            return len(f)
        else:
            if len(f) < len(nums):
                if nums[len(f)] > f[-1]:
                    return len(f)
                else:
                    return len(f) - 1 + target - f[-1]
            else:
                return len(f)


s = Solution()
print(s.searchInsert([-1, 3, 5, 6], -1) == 1)
print(s.searchInsert([2, 3, 4, 7, 8, 9], 11) == 6)
print(s.searchInsert([2, 5], 1) == 0)
print(s.searchInsert([3, 6, 7, 8, 10], 5) == 1)
print(s.searchInsert([1, 3, 5, 6], 5) == 2)
print(s.searchInsert([1, 3, 5, 6], 2) == 1)
print(s.searchInsert([1, 3, 5, 6], 7) == 4)
print(s.searchInsert([1, 3, 5, 6], 0) == 0)
