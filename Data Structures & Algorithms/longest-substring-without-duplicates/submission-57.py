class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        st = {}
        for r in range(len(s)):
            if s[r] in st:
                l = max(l, st[s[r]] + 1)
            res = max(res, r - l + 1)
            st[s[r]] = r
        return res