class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s1 = list(s)
        l = s.count('1')
        r = len(s1) - l
        result = []
        for i in range(l-1):
            result.append('1')
        for j in range(r):
            result.append('0')
        result.append('1')
        return ''.join(result)