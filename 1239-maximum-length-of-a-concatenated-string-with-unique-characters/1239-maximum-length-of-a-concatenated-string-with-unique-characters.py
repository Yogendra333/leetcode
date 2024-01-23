class Solution:
    def backtrack(self, i, u, a):
        return max((self.backtrack(j+1, u|a[j], a) for j in range(i, len(a)) if not u & a[j]), default = len(u))

    def maxLength(self, arr: List[str]) -> int:
        return self.backtrack(0, set(), [u for s in arr if len(u := set(s)) == len(s)])
        