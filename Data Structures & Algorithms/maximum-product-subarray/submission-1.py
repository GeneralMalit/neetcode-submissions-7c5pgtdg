class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_ct = nums[0]
        max_ct = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            temp = max_ct
            max_ct = max(nums[i], max_ct * nums[i], min_ct * nums[i])
            min_ct = min(nums[i], temp * nums[i], min_ct * nums[i])
            res = max(res, max_ct, min_ct)

        return res