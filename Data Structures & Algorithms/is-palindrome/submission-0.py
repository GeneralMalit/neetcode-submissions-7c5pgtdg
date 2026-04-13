class Solution:
    def isPalindrome(self, s: str) -> bool:
        toProcess = [i.lower() for i in s.replace(" ", "") if i.isalnum()]
        L = 0
        R = len(toProcess) - 1

        while L < R:
            if toProcess[L] != toProcess[R]:
                return False
            L += 1
            R -= 1
        return True