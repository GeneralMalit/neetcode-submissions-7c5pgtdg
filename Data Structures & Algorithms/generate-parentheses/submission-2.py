class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(op, cl, s):
            if cl == n:
                res.append(s)
            if op > cl:
                backtrack(op, cl + 1, s + ")")
            if op < n:
                backtrack(op + 1, cl, s + "(")
        
        backtrack(0, 0, "")
        return res
