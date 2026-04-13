class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for l in range(i + 1, len(nums)):

                r = len(nums) - 1
                while l < r:
                    total = nums[i] + nums[l] + nums[r]
                    if l < r and total == 0:
                        res.add((nums[i], nums[l], nums[r]))
                        break
                    elif total > 0:
                        r -= 1
                    else:
                        l += 1
        return list(res)
