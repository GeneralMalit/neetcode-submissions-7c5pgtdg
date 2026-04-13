class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, s, visited):
            if len(s) == len(nums):
                res.append(s[:])

            for j in range(i, len(nums)):
                if visited[j]:
                    continue
                s.append(nums[j])
                visited[j] = True

                backtrack(0, s, visited)

                s.pop()
                visited[j] = False

        backtrack(0, [], [False] * len(nums))
        return res