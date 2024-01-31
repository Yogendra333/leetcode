class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                _, old_idx = stack.pop()
                output[old_idx] = idx - old_idx
            
            stack.append((temp, idx))
        
        return output 