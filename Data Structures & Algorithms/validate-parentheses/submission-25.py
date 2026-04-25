class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ']':'[',
            ')':'(',
            '}':'{'
        }
        stk = []
        for i in s:
            if i in pairs:
                if stk and stk[-1] == pairs[i]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(i)
        return len(stk) == 0