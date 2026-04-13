class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = 1 + d.get(i, 0)
        
        items = sorted([(val, key) for key, val in d.items()], reverse = True)
        res = []
        for i in range(k):
            res.append(items[i][1])
        return res