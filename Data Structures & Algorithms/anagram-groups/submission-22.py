from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_list = collections.defaultdict(list)

        for word in strs:
            word_count = [0] * 26
            for char in word:
                word_count[ord(char) - ord('a')] += 1
            word_list[tuple(word_count)].append(word)
        res = []
        for k, v in (word_list).items():
            res.append(v)
        return res
