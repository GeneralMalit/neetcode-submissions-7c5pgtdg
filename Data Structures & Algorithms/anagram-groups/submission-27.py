from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = defaultdict(list)
        for i in strs:
            ana = [0] * 26
            for c in i:
                ana[ord(c) - ord('a')] += 1
            ana_dict[tuple(ana)].append(i)
        return [val for idx, val in ana_dict.items()]
