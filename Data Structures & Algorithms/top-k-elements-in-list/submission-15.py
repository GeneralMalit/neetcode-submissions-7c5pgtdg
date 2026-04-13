from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        buckets = collections.defaultdict(list)
        for i in nums:
            d[i] = 1 + d.get(i, 0)

        for key, val in d.items():
            buckets[val].append(key)
        res = []
        for amt, key in sorted(buckets.items(), reverse = True):
            for i in key:
                res.append(i)
                k -= 1
                if k == 0:
                    return res