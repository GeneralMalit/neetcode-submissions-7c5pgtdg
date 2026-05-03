class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, others = 0, 0    
        res = 0
        ct = {}
        for r in range(len(s)):
            c = s[r]
            ct[c] = 1 + ct.get(c, 0)
            others = max(others, ct[c])
            if (r - l + 1) - others >  k:
                
                c = s[l]
                ct[c] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res