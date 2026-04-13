class Solution:
    def checkValidString(self, s: str) -> bool:
        lo, hi = 0, 0
        for c in s:
            if c == "(":
                hi += 1
                lo += 1
            elif c == ")":
                hi -= 1
                lo -= 1
            else:
                hi += 1
                lo -= 1
            
            if hi < 0:
                return False
            lo = max(lo, 0)
        return lo == 0
