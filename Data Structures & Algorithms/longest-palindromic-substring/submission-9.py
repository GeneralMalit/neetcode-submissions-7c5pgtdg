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
            temp_len = max(expand(i, i), expand(i, i + 1))
            if temp_len > res_len:
                l = i - (temp_len - 1) // 2
                r = i + temp_len // 2
                res_len = temp_len
        return s[l:r + 1]