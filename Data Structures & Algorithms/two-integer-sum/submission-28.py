class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numset = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in numset:
                return [numset[diff], i]
            numset[nums[i]] = i
        return -1
        