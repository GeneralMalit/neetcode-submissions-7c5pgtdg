class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rset = {}
        for idx, i in enumerate(nums):
            missing = target - i
            if missing in rset:
                return [rset[missing], idx]
            rset[i] = idx
        return -1
            
