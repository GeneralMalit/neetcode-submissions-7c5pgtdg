class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        b = {}
        for i in nums:
            b[i] = 1 + b.get(i, 0)
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for idx, ct in b.items():
            buckets[ct].append(idx)
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for j in buckets[i]:
                res.append(j)
                if len(res) == k:
                    return res
        return -1

