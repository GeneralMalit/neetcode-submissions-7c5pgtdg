class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, s, picked):
            if len(s) == len(nums):
                res.append(s[:])

            for j in range(i, len(nums)):
                if picked[j]:
                    continue
                picked[j] = True
                s.append(nums[j])

                dfs(0, s, picked)

                picked[j] = False
                s.pop()

        dfs(0, [], [False] * len(nums))
        return res