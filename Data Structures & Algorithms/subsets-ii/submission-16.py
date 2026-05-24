class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def bt(i, s):
          res.append(s[:])
          for j in range(i, len(nums)):
            if j > i and nums[j] == nums[j - 1]:
              continue
            s.append(nums[j])
            bt(j + 1, s)
            s.pop()

        bt(0, [])
        return res