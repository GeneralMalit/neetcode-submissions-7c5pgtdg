class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for idx, val in enumerate(nums):
            s[val] = idx
        print(f"s = {s}")
        for i in range(len(nums)):
            num = nums[i]
            diff = target - num
            if diff in s and s[diff] != i:
                return [i, s[diff]]
        return -1