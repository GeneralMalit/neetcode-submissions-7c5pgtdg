class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '}':'{',
            ']':'[',
            ')':'(',
        }
        stack = []

        for i in range(len(s)):
            c = s[i]
            if c in pairs:
                if not stack or stack[-1] != pairs[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)

        return True if not stack else False
