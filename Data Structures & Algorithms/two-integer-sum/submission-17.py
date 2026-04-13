class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = dict()
        for i in range(len(nums)):
            num = nums[i]
            diff = target - num
            if diff in a:
                return [a[diff], i]
            a[num] = i
        return -1