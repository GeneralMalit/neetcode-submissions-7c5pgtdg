class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ']': '[',
            '}': '{',
            ')': '('
        }
        stack = []
        for i in range(len(s)):
            c = s[i]
            
            if c in '([{':
                stack.append(c)
            
            else:
                if not stack:
                    return False
                
                if pairs[c] != stack[-1]:
                    return False
                else:
                    stack.pop()
        
        return True if not stack else False