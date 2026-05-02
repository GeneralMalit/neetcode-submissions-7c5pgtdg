class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        idx = {}
        l = 0
        maxl = 0
        for r in range(len(s)):
            if s[r] in idx:
                l = max(l, idx[s[r]] + 1)
            maxl = max(maxl, r - l + 1)
            idx[s[r]] = r
        return maxl