class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(idx, s, remaining):
            if remaining == 0:
                res.append(s[:])
            if remaining < 0:
                return
            
            for i in range(idx, len(nums)):
                s.append(nums[i])
                backtrack(i, s, remaining - nums[i])
                s.pop()
        backtrack(0, [], target)
        return res