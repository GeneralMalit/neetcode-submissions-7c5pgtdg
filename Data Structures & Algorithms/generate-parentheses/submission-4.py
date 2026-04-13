class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(cp, op, s):
            if cp == n:
                res.append(s[:])
            if cp < op:
                dfs(cp + 1, op, s + ")")
            if op < n:
                dfs(cp, op + 1, s + "(")
        dfs(0, 0, "")
        return res
