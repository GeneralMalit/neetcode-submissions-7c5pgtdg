class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(s, i):
            res.append(s[:])
            for j in range(i, len(nums)):
                s.append(nums[j])
                dfs(s, j + 1)
                s.pop()
        dfs([], 0)
        return res