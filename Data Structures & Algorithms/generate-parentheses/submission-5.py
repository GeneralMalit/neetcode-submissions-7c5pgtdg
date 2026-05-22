class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(op, cp, s):
            if cp == n:
                res.append(s)
            if cp < op:
                dfs(op, cp + 1, s + ")")
            if op < n:
                dfs(op + 1, cp, s + "(")
        dfs(0, 0, "")
        return res