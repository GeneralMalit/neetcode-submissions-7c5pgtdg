class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        window = {}
        res, res_len = [-1, -1], float("inf")
        have, need = 0, len(countT)
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if r - l + 1 < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                c = s[l]
                window[c] -= 1
                l += 1
                if c in countT and window[c] < countT[c]:
                    have -=1

        l, r = res
        return s[l: r + 1] if res_len != float("inf") else ""