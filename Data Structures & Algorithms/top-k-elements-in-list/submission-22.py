class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        for i in nums:
            d[i] = 1 + d.get(i, 0)

        buckets = [[] for _ in range(len(nums) + 1)]
        for key, val in d.items():
            buckets[val].append(key)
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for item in buckets[i]:
                res.append(item)
                if len(res) == k:
                    return res
