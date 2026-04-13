class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(idx, s, picked):
            if len(s) == len(nums):
                res.append(s[:])
            
            for i in range(len(nums)):
                if picked[i]:
                    continue
                
                picked[i] = True
                s.append(nums[i])

                backtrack(0, s, picked)

                picked[i] = False
                s.pop()

        backtrack(0, [], [False] * len(nums))
        return res