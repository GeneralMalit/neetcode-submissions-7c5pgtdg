class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {val:idx for idx, val in enumerate(s)}
        res = []
        anchor, i = 0, 0
        j = 0
        for i in range(len(s)):
                j = max(j, d[s[i]])
                if i == j:
                        res.append(i - anchor + 1)
                        anchor = i + 1
        return res