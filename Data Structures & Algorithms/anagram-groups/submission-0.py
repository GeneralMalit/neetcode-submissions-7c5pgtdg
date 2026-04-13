class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapped = dict()
        out = []
        for i in strs:
            fp = "".join(sorted(i))
            if fp not in mapped:
                mapped[fp] = [i]
            else:
                mapped[fp].append(i)
        for keys, values in mapped.items():
            out.append(values)
        return out