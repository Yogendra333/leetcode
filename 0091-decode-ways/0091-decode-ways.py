class Solution:
    def numDecodings(self, s: str) -> int:
        sset = {str(i) for i in range(1,27)}
        if s[0] == "0":
            return 0
        prev_2 = 1
        prev = 1

        for i in range(1,len(s)):
            if s[i] == "0" and s[i-1] == "0":
                return 0
            if s[i] != "0" and s[i-1:i+1] in sset:
                prev_2, prev = prev, prev_2 + prev
            elif s[i] != "0":
                prev_2, prev = prev, prev
            elif s[i-1:i+1] not in sset:
                return 0
            else:
                prev_2, prev = prev_2, prev_2
        return prev