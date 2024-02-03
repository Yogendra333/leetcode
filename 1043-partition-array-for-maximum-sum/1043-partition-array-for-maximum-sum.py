class Solution:
    def maxSumAfterPartitioning(self, a: List[int], k: int) -> int:
        return (f:=cache(lambda i,m,l:max((m:=max(m,a[i]))*(l:=l+1)+f(i+1,0,0),(l<k)*f(i+1,m,l)) if i-len(a) else m*l))(0,0,0)