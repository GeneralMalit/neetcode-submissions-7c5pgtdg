class Solution:
    def isValid(self, s: str) -> bool:
        pair = {
            ']':'[',
            '}':'{',
            ')':'('
        }

        stk = []
        for i in s:
            if i in pair:
                if (stk and stk[-1] != pair[i]) or not stk:
                    return False
                stk.pop()
            else:
                stk.append(i)

        return len(stk) == 0