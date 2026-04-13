class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char = {}
        maxf = 0
        maxc = 0
        l = 0
        for r in range(len(s)):
            c = s[r]
            char[c] = 1 + char.get(c, 0)
            maxf = max(maxf, char[c])

            while k < (r - l + 1) - maxf:
                char[s[l]] -= 1
                l += 1
            maxc = max(maxc, r - l + 1)
        return maxc