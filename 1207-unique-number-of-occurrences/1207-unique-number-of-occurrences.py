class Solution:
    def uniqueOccurrences(self, a: List[int]) -> bool:
        return max(Counter(Counter(a).values()).values())<2
        