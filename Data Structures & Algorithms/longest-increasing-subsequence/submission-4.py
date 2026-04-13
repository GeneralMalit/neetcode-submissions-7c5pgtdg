import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] > res[-1]:
                res.append(nums[i])
            else:
                j = bisect.bisect_left(res, nums[i])
                res[j] = nums[i]

        return len(res)
