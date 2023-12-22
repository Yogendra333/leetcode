class Solution:
    def maxScore(self, s: str) -> int:
        sum,m=0,0
        for i in range(1,len(s)):
            sum+=s[:i].count('0') 
            sum+=s[i:].count('1')
            m=max(sum,m)
            sum=0
        return m