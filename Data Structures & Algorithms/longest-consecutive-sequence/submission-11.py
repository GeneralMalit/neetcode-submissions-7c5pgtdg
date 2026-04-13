class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        currmax = 0
        for i in numset:
            if i - 1 in numset:
                continue
            else:
                curr = 1
                while i + 1 in numset:
                    i += 1
                    curr += 1
                currmax = max(curr, currmax)
        return currmax