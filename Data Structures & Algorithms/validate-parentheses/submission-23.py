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
                if not stk or (stk[-1] != pair[i]):
                    return False
                stk.pop()
            else:
                stk.append(i)

        return len(stk) == 0