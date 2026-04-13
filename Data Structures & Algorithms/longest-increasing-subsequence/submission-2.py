import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [nums[0]]

        for num in nums:
            if num > res[-1]:
                res.append(num)
            else:
                i = bisect.bisect_left(res, num)
                res[i] = num
        
        return len(res)