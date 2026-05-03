class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = {}
        for i in t:
            count_t[i] = 1 + count_t.get(i, 0)
        res, res_len = [-1,-1], float("inf")
        have, need = 0, len(count_t)
        l = 0
        window = {}
        for r in range(len(s)):
            print(f"r = {s[r]}, res = {res}. res_len = {res_len}")
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in count_t and window[c] == count_t[c]:
                have += 1
            while have == need:
                if r - l + 1 < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                c = s[l]
                window[c] -= 1
                if c in count_t and window[c] < count_t[c]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r + 1] if res_len != float("inf") else ""
