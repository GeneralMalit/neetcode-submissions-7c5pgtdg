from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = Counter()
        d2 = Counter()
        for i in s:
            d1[i] += 1
        for j in t:
            d2[j] += 1
        return d1 == d2

