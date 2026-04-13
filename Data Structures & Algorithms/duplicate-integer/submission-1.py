class Solution:
    def hasDuplicate(self, nums) -> bool:
        a = set()
        for i in nums:
            if i in a:
                return True
            else:
                a.add(i)

        return False