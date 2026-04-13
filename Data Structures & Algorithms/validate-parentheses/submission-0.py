class Solution:
    def isValid(self, s: str) -> bool:
        # first thing i thought of here is the switch-case statement in JavaScript, which in Python, is match-case.
        stack = []
        for i in s:
            print(f"stack is currently looking = {stack} case now is {i}")
            
            match i:
                case "(" | "{" | "[":
                    stack.append(i)
                case ")":
                    if stack == []:
                        return False
                    if stack.pop() != "(":
                        return False
                case "}":
                    if stack == []:
                        return False
                    if stack.pop() != "{":
                        return False
                case "]":
                    if stack == []:
                        return False
                    if stack.pop() != "[":
                        return False
                case _:
                    return False
        
        if stack != []:
            return False
        else:
            return True

        