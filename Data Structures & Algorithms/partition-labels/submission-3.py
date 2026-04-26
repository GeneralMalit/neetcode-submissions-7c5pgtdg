class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        la = {val:idx for idx, val in enumerate(s)}
        anchor, i = 0, 0
        res = []
        for j in range(len(s)):
            i = max(i, la[s[j]])
            if i == j:
                res.append(j - anchor + 1)
                anchor = j + 1
        return res