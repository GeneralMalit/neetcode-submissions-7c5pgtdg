class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = {}
        for i in t:
            count_t[i] = 1 + count_t.get(i, 0)
        window = {}
        l = 0
        res, res_len = [-1, -1], float("inf")
        have, need = 0, len(count_t)
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in count_t:
                if window[c] == count_t[c]:
                    have += 1
            while have == need:
                if r - l + 1 < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                c = s[l]
                window[c] -= 1
                l += 1
                if c in count_t:
                    if window[c] < count_t[c]:
                        have -=1
        l, r = res
        print(f"l, r = {l, r}")
        return s[l:r + 1] if res_len != float("inf") else ""