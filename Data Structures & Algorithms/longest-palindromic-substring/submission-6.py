class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1
        l, r = 0, 0
        res_len = 0
        for i in range(len(s)):
            mres = max(expand(i, i), expand(i, i + 1))
            if mres > res_len:
                res_len = mres
                l = i - (mres - 1) // 2
                r = i + mres // 2
        return s[l:r + 1] if res_len != 0 else ""