class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        c_1 = [0] * 26
        c_2 = [0] * 26

        for i in range(len(s1)):
            c_1[ord(s1[i]) - ord('a')] += 1
            c_2[ord(s2[i]) - ord('a')] += 1
        
        if c_1 == c_2:
            return True
        
        for i in range(len(s1), len(s2)):
            c_2[ord(s2[i]) - ord('a')] += 1
            c_2[ord(s2[i - len(s1)]) - ord('a')] -= 1
            if c_2 == c_1:
                return True
        return False
