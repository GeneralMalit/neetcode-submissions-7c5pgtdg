class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for t in tokens:
            if t in "+-/*":
                b = int(stk.pop())
                a = int(stk.pop())
                if t == "+":
                    stk.append(b + a)
                elif t == "-":
                    stk.append(a - b)
                elif t == "*":
                    stk.append(b * a)
                else:
                    stk.append(int(a/b))
            else:
                stk.append(t)
        return int(stk[-1])