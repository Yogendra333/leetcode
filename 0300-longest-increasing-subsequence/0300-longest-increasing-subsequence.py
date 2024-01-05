from sortedcontainers import SortedDict

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return (lambda d:any(setitem(d,bisect_left(d.values(),q),q) for q in nums) or len(d))(SortedDict())