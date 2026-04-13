class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf, res = 0, 0
        ch = {}
        l = 0

        for r in range(0, len(s)):
            char = s[r]
            ch[char] = 1 + ch.get(char, 0)
            maxf = max(maxf, ch[char])

            if (r - l + 1) - maxf > k:
                ch[s[l]] -= 1
                l += 1
            
            res = max(res, (r - l + 1))
        return res
