import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [nums[0]]

        for num in nums:
            if num > lis[-1]:
                lis.append(num)
            else:
                i = bisect.bisect_left(lis, num)
                lis[i] = num
        return len(lis)
