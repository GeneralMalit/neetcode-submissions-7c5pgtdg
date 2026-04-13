class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ("".join(char for char in s if char.isalnum())).lower()
        print(f"{s}")
        l, r = 0, len(s) - 1
        while l <= r:
            print(f"{l}{r}")
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True