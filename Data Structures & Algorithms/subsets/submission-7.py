class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, s):
            res.append(s[:])

            for j in range(i, len(nums)):
                s.append(nums[j])
                dfs(j + 1, s)
                s.pop()

        dfs(0, [])
        return res