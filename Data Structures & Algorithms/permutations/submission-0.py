class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(path, used):
            if len(nums) == len(path):
                res.append(path[:])
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                used[i] = True
                path.append(nums[i])
                
                backtrack(path, used)

                used[i] = False
                path.pop()
        
        backtrack([], [False] * len(nums))
        return res