class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        r = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in r:
                return [r[diff], i]
            r[v] = i
        return -1