class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            print(f"m = {m}")
            if nums[m] == target:
                return m
            
            if nums[m] > nums[r]: #if left side is sorted
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else: #if right side is sorted
                if nums[m] < target <= nums[r]: #if target is at right side
                    l = m + 1
                else:
                    r = m - 1
        
        return -1
