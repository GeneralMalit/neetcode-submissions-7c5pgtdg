class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        char = {}
        maxl = 0
        for r in range(len(s)):
            c = s[r]
            if c in char and char[c] >= l:
                l = char[c] + 1
            char[c] = r
            maxl = max(maxl, r - l + 1)


        return maxl