class Solution:
    def rob(self, nums: List[int]) -> int:

        house1 = 0
        house2 = 0

        for i in range(len(nums)):
            curr = max(house2 + nums[i], house1)
            house2 = house1
            house1 = curr
        return house1