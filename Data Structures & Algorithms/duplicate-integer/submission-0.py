class Solution:
    def hasDuplicate(self, nums) -> bool:
        toCheck = []
        for i in nums:
            if len(toCheck) == 0:
                toCheck.append(i)
            else:
                try:
                    ind = toCheck.index(i)
                    return True
                except:
                    toCheck.append(i)

        return False