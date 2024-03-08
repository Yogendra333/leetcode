class Solution:
    def maxFrequencyElements(self, a: List[int]) -> int:
        return (f:=sorted(Counter(a).values())).count(f[-1])*f[-1]