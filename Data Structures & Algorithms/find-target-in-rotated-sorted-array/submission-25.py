class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            elif nums[m] < nums[r]: #right is sorted
                if nums[m] < target <= nums[r]: #target is  here
                    l = m + 1
                else:
                    r = m - 1
            else: #left is sorted
                if nums[l] <= target < nums[m]: #target is here
                    r = m - 1
                else:
                    l = m + 1
        return -1