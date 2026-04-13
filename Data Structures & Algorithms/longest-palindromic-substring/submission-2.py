class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1
        
        l, r = 0, 0
        for i in range(len(s)):
            ct = max(expand(i,i), expand(i,i+1))
            if ct > r - l:
                l = i - (ct - 1) // 2
                r = i  + ct // 2
        return s[l:r + 1]