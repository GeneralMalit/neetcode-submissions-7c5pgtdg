class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []
        digit_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(i, s):
            if i == len(digits):
                res.append(s[:])
                return
            
            for char in digit_map[digits[i]]:
                s += char
                backtrack(i + 1, s)
                s = s[:-1]
            
        backtrack(0, "")
        return res