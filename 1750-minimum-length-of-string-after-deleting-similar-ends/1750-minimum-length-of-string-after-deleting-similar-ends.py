class Solution:
    def minimumLength(self, s: str) -> int:
        l = 0
        r = len(s) - 1
        if len(s) == 1:
            return 1
        while r >= l:
            if s[l] != s[r]:
                break
            while r > 0 and s[r] == s[r - 1]:
                r -= 1
            while l <= r and s[l] == s[l + 1]:
                l += 1
            
            l += 1
            r -= 1
            
        return r - l + 1 if r - l + 1 >= 0 else r - l + 3
        