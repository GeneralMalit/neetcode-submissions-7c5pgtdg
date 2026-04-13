class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        stack = []
        for i in s:
            print(f"stack = {stack}")
            if i in "]})":
                if stack and stack[-1] == pairs[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return True if not stack else False
