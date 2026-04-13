class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        self.maximum = 0
        num_set = set(nums)

        for i in num_set:
            if i - 1 not in num_set:
                run = 1
                while i + 1 in num_set:
                    run += 1
                    i += 1
                self.maximum = max(self.maximum, run)
        return self.maximum
        