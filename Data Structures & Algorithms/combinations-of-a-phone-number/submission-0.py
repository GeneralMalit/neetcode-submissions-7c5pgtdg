class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_map = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        
        res = []

        def backtrack(idx, s):
            if idx == len(digits):
                res.append(s) if s != "" else None
                return 
            
            curr_digit = digits[idx]
            for letter in phone_map[curr_digit]:
                s += letter
                backtrack(idx + 1, s)
                s = s[:-1]
        
        backtrack(0, "")
        return res