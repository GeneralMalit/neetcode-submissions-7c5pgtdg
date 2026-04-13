class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hs = {}
        for char in s:
            hs[char] = hs.get(char, 0) + 1 
        
        for char in t:
            if char not in hs:
                return False
            
            hs[char] -= 1

            if hs[char] < 0:
                return False
        
        return True