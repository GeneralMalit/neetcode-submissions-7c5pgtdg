class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for i in nums:
            hmap[i] = hmap.get(i, 0) + 1

        freq_b = [[] for _ in range(len(nums) + 1)]

        for num, freq in hmap.items():
            freq_b[freq].append(num)
        res = []
        for i in range(len(freq_b) - 1, 0, -1):
            for j in freq_b[i]:
                res.append(j)
                if len(res) == k:
                    return res
        