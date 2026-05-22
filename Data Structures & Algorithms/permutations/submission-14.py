class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, s, visited):
            if len(s) == len(nums):
                res.append(s[:])
                return 
            for j in range(len(nums)):
                if visited[j]:
                    continue

                visited[j] = True
                s.append(nums[j])

                dfs(i + 1, s, visited)

                visited[j] = False
                s.pop()

        dfs(0, [], [False] * len(nums))
        return res
                