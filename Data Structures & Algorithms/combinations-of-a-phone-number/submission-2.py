class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        numbers = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(idx, s):
            if idx == len(digits):
                res.append(s)
                return

            digit = digits[idx]
            for char in numbers[digit]:
                s += char
                backtrack(idx + 1, s)
                s = s[:-1]
        
        backtrack(0, "")
        return res