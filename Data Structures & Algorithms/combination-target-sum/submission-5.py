class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, s, remaining):
            if remaining == 0:
                res.append(s[:])
            
            if remaining < 0:
                return 

            for j in range(i, len(nums)):
                s.append(nums[j])
                dfs(j, s, remaining - nums[j])
                s.pop()
        
        dfs(0, [], target)
        return res