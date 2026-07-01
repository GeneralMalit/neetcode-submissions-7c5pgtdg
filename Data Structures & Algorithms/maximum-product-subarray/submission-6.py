class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mps = nums[0]
        max_left = nums[0]
        min_left = nums[0]

        for i in range(1, len(nums)):
            temp = max_left
            max_left = max(nums[i], nums[i] * max_left, nums[i] * min_left)
            min_left = min(nums[i], nums[i] * temp, nums[i] * min_left)

            mps = max(mps, max_left, min_left)

        return mps