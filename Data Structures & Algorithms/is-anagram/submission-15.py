class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_ct = [0] * 26
        for i in s:
            char_ct[ord(i) - ord('a')] += 1

        for i in t:
            char_ct[ord(i) - ord('a')] -= 1
        
        return True if char_ct == [0] * 26 else False