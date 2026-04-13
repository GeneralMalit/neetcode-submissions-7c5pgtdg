class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(idx, s):
            res.append(s[:])
            for i in range(idx, len(nums)):
                s.append(nums[i])
                backtrack(i + 1, s)
                s.pop()
        
        backtrack(0, [])
        return res