class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        def bt(l):
            if l == len(s):
                res.append(path[:])
            for r in range(l, len(s)):
                substr = s[l:r + 1]
                if substr == substr[::-1]:
                    path.append(substr)
                    bt(r + 1)
                    path.pop()

        bt(0)
        return res