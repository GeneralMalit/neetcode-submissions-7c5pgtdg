class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(idx, s, picked):
            if len(s) == len(nums):
                res.append(s[:])
            for i in range(idx, len(nums)):
                if picked[i]:
                    continue
                s.append(nums[i])
                picked[i] = True

                backtrack(0, s, picked)

                s.pop()
                picked[i] = False

        backtrack(0, [], [False] * len(nums))
        return res