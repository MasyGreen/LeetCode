class Solution:
    def mySqrt(self, x: int) -> int:
        return int(str(x ** (0.5)).split(".")[0])

s = Solution()
print(s.mySqrt(4)==2)
print(s.mySqrt(5)==2)
print(s.mySqrt(1024)==32)
