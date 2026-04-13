class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l = 0
        idx = {}
        maxc = 1

        for i in range(len(s)):
            if s[i] in idx:
                l = max(l, idx[s[i]] + 1)
                
            maxc = max(maxc, i - l + 1)
            idx[s[i]] = i
        return maxc

        #did we see it yet
        #if not we add it and we increment maxc
        #if yes shrink the sliding window to the next boundary
        #append it
        #123414
            