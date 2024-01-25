class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        pos = defaultdict(list)
        for i, c in enumerate(text1):
            pos[c].append(i)

        lcs = [inf] * len(text2)

        for c in text2:
            for i in reversed(pos[c]):
                lcs[bisect_left(lcs, i)] = i

        return bisect_left(lcs, inf)