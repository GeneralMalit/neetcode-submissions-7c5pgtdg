class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cmax = 0
        numset = set(nums)
        for i in numset:
            if i - 1 in numset:
                continue
            else:
                curr = 1
                while i + 1 in numset:
                    i = i + 1
                    curr += 1
                cmax = max(curr, cmax)
        return cmax