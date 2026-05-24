class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def bt(op, cp, s):
            if cp == n:
                res.append(s[:])

            if cp < op:
                bt(op, cp + 1, s + ")")

            if op < n:
                bt(op + 1, cp, s + "(")
        bt(0, 0, "")
        return res