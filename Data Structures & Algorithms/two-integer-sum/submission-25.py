class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rset = {}
        for idx, num in enumerate(nums):
            miss = target - num
            if miss in rset:
                return [rset[miss], idx]
            
            else:
                rset[num] = idx
        return -1