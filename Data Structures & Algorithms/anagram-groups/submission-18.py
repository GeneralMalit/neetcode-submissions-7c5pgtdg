from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charmap = collections.defaultdict(list)

        for i in strs:
            clist = [0] * 26
            for char in i:
                clist[ord(char) - ord('a')] += 1
            charmap[tuple(clist)].append(i)
        
        return list(charmap.values())