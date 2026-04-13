class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1
        l, r = 0, 0
        res = float("-inf")
        for i in range(len(s)):
            curr = max(expand(i, i), expand(i, i + 1))
            if curr > res:
                l = i - (curr - 1) // 2
                r = i + curr // 2
                res = curr
        return s[l:r + 1]