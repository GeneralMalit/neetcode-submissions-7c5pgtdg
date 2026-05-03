class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ct = {}
        res = 0
        l = 0
        for r in range(len(s)):
            if s[r] in ct:
                l = max(l, ct[s[r]] + 1)
            res = max(res, (r - l + 1))
            ct[s[r]] = r
        return res