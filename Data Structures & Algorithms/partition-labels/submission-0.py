class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {char:i for i, char in enumerate(s)}
        j = 0
        anchor = 0
        res = []
        for i, char in enumerate(s):
            j = max(j, last_index[char])
            if i == j:
                res.append(j - anchor + 1)
                anchor = i + 1
        return res