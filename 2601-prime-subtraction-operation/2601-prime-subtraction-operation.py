class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        # Step 1: Generate a list of prime numbers up to the maximum number in nums
        p = []  # List to store prime numbers
        for i in range(2, max(nums)):
            # Check if 'i' is prime by testing divisibility with previously found primes
            for j in p:
                if i % j == 0:  # If 'i' is divisible by any prime 'j', it is not prime
                    break  # Exit the loop if 'i' is not prime
            else:
                # If no divisors were found, 'i' is prime; add it to the list
                p.append(i)

        n = len(nums)  # Length of the input array
        # Step 2: Iterate through the array from second-to-last element to the first
        for i in range(n - 2, -1, -1):
            # If current element is already less than the next one, continue to next iteration
            if nums[i] < nums[i + 1]:
                continue
            
            # Step 3: Find the largest prime that can be subtracted from nums[i]
            j = bisect_right(p, nums[i] - nums[i + 1])  # Find insertion point for nums[i] - nums[i + 1]
            
            # Check if we found a valid prime or if it is too large
            if j == len(p) or p[j] >= nums[i]:
                return False  # No valid prime found, return False
            
            # Step 4: Subtract the found prime from nums[i]
            nums[i] -= p[j]  # Adjust current element
            
        return True  # If all adjustments are valid, return True
        