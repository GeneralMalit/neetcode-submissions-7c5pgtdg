class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        rs = set()
        for i in nums:
            if i in rs:
                return True
            rs.add(i)
        return False