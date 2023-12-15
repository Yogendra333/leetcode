class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        frm,to=zip(*paths)
        return (set(to)-set(frm)).pop()