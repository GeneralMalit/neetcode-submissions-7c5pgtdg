class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = {}
        for i in nums:
            s[i] = 1 + s.get(i, 0)

        fb = [[] for _ in range(len(nums) + 1)]

        for n, c in s.items():
            fb[c].append(n)
        res = []
        for i in range(len(fb) - 1, 0, -1):
            for j in fb[i]:
                res.append(j)
                if len(res) == k:
                    return res
                    