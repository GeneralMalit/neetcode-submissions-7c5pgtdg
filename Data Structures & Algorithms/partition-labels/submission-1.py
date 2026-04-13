class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        anchor, j = 0, 0
        char_map = {char:i for i, char in enumerate(s)}
        res = []
        for i in range(len(s)):
            j = max(j, char_map[s[i]])
            if i == j:
                res.append(j - anchor + 1)
                anchor = i + 1
        return res