class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res =[]
        digit_map = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }

        def backtrack(i, s):
            if i == len(digits):
                res.append("".join(s)) if len(s) > 0 else None
                return
            
            for digit in digit_map[digits[i]]:
                s.append(digit)
                backtrack(i + 1, s)
                s.pop()

        backtrack(0, [])
        return res

