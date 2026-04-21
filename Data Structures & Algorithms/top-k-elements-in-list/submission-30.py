from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        e = {}
        for i in nums:
            e[i] = 1 + e.get(i, 0)
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, count in e.items():
            bucket[count].append(num)
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for j in bucket[i]:
                res.append(j)
                if len(res) == k:
                    return res