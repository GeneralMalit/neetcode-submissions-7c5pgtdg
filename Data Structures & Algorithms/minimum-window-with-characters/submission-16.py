class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        countT = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        countS = {}
        res, res_len = [-1, -1], float("inf")
        l = 0
        have, need = 0, len(countT)

        for r in range(len(s)):
            c = s[r]
            countS[c] = 1 + countS.get(c, 0)
            if c in countT and countT[c] == countS[c]:
                have += 1
            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                c = s[l]
                countS[c] -= 1
                if c in countT and countS[c] < countT[c]:
                    have -=1 
                l += 1
            
        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""