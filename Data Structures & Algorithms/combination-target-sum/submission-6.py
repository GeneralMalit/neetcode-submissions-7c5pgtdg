class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(j, s, remaining):
            if remaining == 0:
                res.append(s[:])
            
            if remaining < 0:
                return 

            for i in range(j, len(nums)):
                s.append(nums[i])
                dfs(i, s, remaining - nums[i])
                s.pop()
        dfs(0, [], target)
        return res
