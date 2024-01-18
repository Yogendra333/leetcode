class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        arr = [0] * 46
        cnt = 3
        arr[1] = 1
        arr[2] = 2

        for i in range(3, n + 1):
            arr[i] = arr[i - 1] + arr[i - 2]
            cnt += 1

        return arr[cnt - 1]