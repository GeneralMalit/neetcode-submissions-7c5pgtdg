class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def backtrack(start):
            if start == len(s):
                res.append(path[:])
            
            for i in range(start, len(s)):
                substring = s[start: i + 1]
                if substring == substring[::-1]:
                    path.append(substring)
                    backtrack(i + 1)
                    path.pop()

        backtrack(0)
        return res