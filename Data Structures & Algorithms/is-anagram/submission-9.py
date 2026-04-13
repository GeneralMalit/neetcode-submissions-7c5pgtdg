class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hs = {}
        for i in s:
            hs[i] = hs.get(i, 0) + 1
        for i in t:
            hs[i] = hs.get(i, 0) - 1

        return False if any(x != 0 for x in hs.values()) else True