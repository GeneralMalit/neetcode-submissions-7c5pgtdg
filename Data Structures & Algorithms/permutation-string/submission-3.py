class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_c = [0] * 26
        w_c = [0] * 26

        for i in range(len(s1)):
            s1_c[ord(s1[i]) - ord('a')] = 1 + s1_c[ord(s1[i]) - ord('a')] 
            w_c[ord(s2[i]) - ord('a')] = 1 + w_c[ord(s2[i]) - ord('a')]
        if s1_c == w_c:
            return True
        
        for i in range(len(s1), len(s2)):
            w_c[ord(s2[i]) - ord('a')] = 1 + w_c[ord(s2[i]) - ord('a')]
            w_c[ord(s2[i - len(s1)]) - ord('a')] -= 1
            if s1_c == w_c:
                return True
        
        return False