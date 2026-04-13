class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        idx = {}
        maxlen = 0
        l = 0

        for r in range(len(s)):
            if s[r] in idx:
                l = max(l, idx[s[r]] + 1)
            maxlen = max(maxlen, r - l + 1)
            idx[s[r]] = r
        return maxlen