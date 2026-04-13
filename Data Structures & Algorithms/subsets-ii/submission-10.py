class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res =[]
        def dfs(idx, s):
            res.append(s[:])
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                s.append(nums[i])
                dfs(i + 1, s)
                s.pop()
        dfs(0, [])
        return res