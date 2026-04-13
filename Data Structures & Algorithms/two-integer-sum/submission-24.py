class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            num = nums[i]
            diff = target - num
            if diff in d:
                return [d[diff], i]
            d[num] = i
        return -1
