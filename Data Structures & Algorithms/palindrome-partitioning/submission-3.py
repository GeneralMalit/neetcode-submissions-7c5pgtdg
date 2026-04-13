class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        def backtrack(l):
            if l == len(s):
                res.append(path[:])
            for r in range(l, len(s)):
                substring = s[l:r +1]
                if substring == substring[::-1]:
                    path.append(substring)
                    backtrack(r + 1)
                    path.pop()
        backtrack(0)
        return res
                    
