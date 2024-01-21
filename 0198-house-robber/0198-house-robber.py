class Solution:
    def rob(self, nums: list[int]) -> int:

        if len(nums) < 3: return max(nums)

        prev, curr = nums[0], max(nums[0], nums[1])
        
        for n in range(2, len(nums)):
            curr, prev = max(nums[n]+prev, curr), curr

        return curr