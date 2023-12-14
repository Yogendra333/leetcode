class Solution(object):
    def onesMinusZeros(self, grid):
        m, n = len(grid), len(grid[0])
        row = [0] * m  #taken extra space to count 1's
        col = [0] * n
        
        #this two loops for count 1's in each row and column
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                col[j] += grid[i][j]
                row[i] += grid[i][j]
        ans = []
        for i in range(len(grid)):
            temp = []
            for j in range(len(grid[0])):
                temp.append(row[i] + col[j] - (n - row[i]) - (m - col[j]))
            ans.append(temp)
        return ans