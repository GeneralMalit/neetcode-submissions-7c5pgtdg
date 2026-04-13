class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        def expand_len(l, r):
            while l >= 0 and r < len(s) and s[r] == s[l]:
                l -= 1
                r += 1
            return r - l - 1

        for i in range(len(s)):
            max_len = max(expand_len(i, i), expand_len(i, i + 1))
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]