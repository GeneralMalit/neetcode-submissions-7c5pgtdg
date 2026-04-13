class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxf = 0
        maxlen = 0
        l = 0

        for i in range(len(s)):
            count[s[i]] = 1 + count.get(s[i], 0)
            maxf = max(maxf, count[s[i]])

            if (i - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            maxlen = max(maxlen, i - l + 1)
        
        return maxlen