from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for i in strs:
            s = [0] * 26
            for c in i:
                s[ord(c) - ord('a')] += 1
            groups[tuple(s)].append(i)
        return [i for i in groups.values()]
