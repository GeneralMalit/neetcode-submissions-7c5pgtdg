class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(op, cp, s):
            if cp == n:
                res.append(s)

            if cp < op:
                backtrack(op, cp + 1, s + ")")
            
            if op < n:
                backtrack(op + 1, cp, s + "(")

        backtrack(0, 0, "")
        return res