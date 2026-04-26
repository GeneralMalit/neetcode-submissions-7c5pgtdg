class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for c in tokens:
            if c in "-+/*":
                b = int(stk.pop())
                a = int(stk.pop())
                if c == "+":
                    stk.append(a + b)
                elif c == "-":
                    stk.append(a - b)
                elif c == "*":
                    stk.append(a * b)
                else:
                    stk.append(int(a/b))
            else:
                stk.append(c)
        return int(stk[-1])