class Solution:
    def isValid(self, s: str) -> bool:
        valid = {
            "]":"[",
            "}":"{",
            ")":"("
        }
        stk = []
        for i in s:
            if i in valid:
                if stk and stk[-1] == valid[i]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(i)
        return True if stk == [] else False