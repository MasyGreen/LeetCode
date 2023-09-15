class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == '0' and b == '0':
            return '0'

        a = a.zfill(max(len(a), len(b)))[::-1]
        b = b.zfill(max(len(a), len(b)))[::-1]

        print(f'{a=}; {b=}')

        result = ''
        ind = 0
        for i, j in zip(a, b):
            if int(i) + int(j) + ind == 3:
                result = result + '1'
                ind = 1
            elif int(i) + int(j) + ind == 2:
                result = result + '0'
                ind = 1
            elif int(i) + int(j) + ind == 1:
                result = result + '1'
                ind = 0
            else:
                result = result + '0'
                ind = 0
        if ind == 1:
            result = result + '1'
        print(result[::-1])
        return result[::-1]


s = Solution()

print(s.addBinary(a="100", b="110010") == "110110")

print(s.addBinary(a="1111", b="1111") == "11110")

print(s.addBinary(a="11", b="1") == "100")
print(s.addBinary(a="1010", b="1011") == "10101")

