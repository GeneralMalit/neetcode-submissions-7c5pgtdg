class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        d = {}

        for i in range(len(s)):
            c = s[i]
            if c in d and d[c] >= l:
                l = d[c] + 1
            d[c] = i 

            res = max(res, i - l + 1)
        return res