from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_list = collections.defaultdict(list)

        for word in strs:
            char_ct = [0] * 26
            for c in word:
                char_ct[ord(c) - ord('a')] += 1
            word_list[tuple(char_ct)].append(word)
        return [i for i in word_list.values()]