class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_count = 0
        d = {}
        max_len = 0
        for r in range(len(s)):
            d[s[r]] = 1 + d.get(s[r], 0)
            max_count = max(max_count, d[s[r]])
            if k < (r - l + 1) - max_count:
                d[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len


