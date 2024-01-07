class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        total_count = 0
        n = len(nums)
        subseq = [{} for _ in range(n)]
        
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                count_j = subseq[j].get(diff, 0)
                count_i = subseq[i].get(diff, 0)
                subseq[i][diff] = count_i + count_j + 1
                total_count += count_j
            
        return total_count