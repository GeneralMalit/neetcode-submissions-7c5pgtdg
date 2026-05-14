class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cmax = 0
        numset = set(nums)
        for i in numset:
            while i - 1 in numset:
                i = i - 1
            curr = 1
            while i + 1 in numset:
                curr += 1
                i = i + 1
            cmax = max(cmax, curr)
        return cmax