class Solution:
    @cache
    def findPaths(self, m: int, n: int, c: int, i: int, j: int) -> int:
        return not(m>i>-1<j<n) or c and sum(self.findPaths(m,n,c-1,i+o,j+p) for o,p in ((-1,0),(0,1),(1,0),(0,-1)))%(10**9+7)