class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(2, len(nums), 3):
            if nums[i] - nums[i - 2] <= k:
                ans.append(nums[i - 2: i + 1])
            else:
                return []
        return ans