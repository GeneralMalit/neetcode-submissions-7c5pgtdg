class Solution:
    def isValid(self, s: str) -> bool:
        stk = []

        partner = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }

        for i in s:
            if i in partner:
                if not stk or stk[-1] != partner[i]:
                    return False
                else:
                    stk.pop()
            else:
                stk.append(i)
        
        return True if not stk else False