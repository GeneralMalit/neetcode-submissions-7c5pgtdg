class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for i in nums:
            hmap[i] = hmap.get(i, 0) + 1

        fbuck = [[] for _ in range(len(nums) + 1)]
        for key, val in hmap.items():
            fbuck[val].append(key)
        res = []
        for i in range(len(fbuck) - 1, 0, -1):
            for j in fbuck[i]:
                res.append(j)
                if len(res) == k:
                    return res