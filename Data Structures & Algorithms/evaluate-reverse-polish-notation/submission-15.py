class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for t in tokens:
            if t in "+-*/":
                b = stk.pop()
                a = stk.pop()
                print(f"{a} {t} {b}")
                if t == "+":
                    stk.append(a + b)
                elif t == "-":
                    stk.append(a - b)
                elif t == "*":
                    stk.append(a * b)
                else:
                    stk.append(int(a/b))
                print(f"stk = {stk}")
            else:
                stk.append(int(t))
        
        return stk[-1]