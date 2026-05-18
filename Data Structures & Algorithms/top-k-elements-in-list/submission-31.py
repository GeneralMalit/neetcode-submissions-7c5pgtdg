class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        e = {}
        for i in nums:
            e[i] = 1 + e.get(i, 0)
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, count in e.items():
            buckets[count].append(num)
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for j in buckets[i]:
                res.append(j)
                if len(res) == k:
                    return res
        return -1