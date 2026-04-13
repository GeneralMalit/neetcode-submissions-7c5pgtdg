class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        stack = []

        close_open = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }


        for char in s:
            if char in close_open:
                if stack and stack[-1] == close_open[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return True if not stack else False