class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = [0] * 26
        s2 = [0] * 26
        for i in s:
                s1[ord(i) - ord('a')] += 1

        for i in t:
                s2[ord(i) - ord('a')] += 1

        return s1 == s2
