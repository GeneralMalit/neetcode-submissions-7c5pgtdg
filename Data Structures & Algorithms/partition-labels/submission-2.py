class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_app = {val:idx for idx, val in enumerate(s)}
        anchor, i = 0, 0
        res = []
        for j in range(len(s)):
            i = max(i, last_app[s[j]])
            if j == i:
                res.append(j - anchor + 1)
                anchor = j + 1

        return res
