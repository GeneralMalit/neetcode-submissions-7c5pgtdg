class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        out = []
        for idx, i in enumerate(nums):
            hashMap[i] = idx
        for idx, i in enumerate(nums): #for every number in nums
            #compute for the difference
            dif = target - i
            if dif in hashMap: #if difference exists
                if idx == hashMap[dif]:
                    continue
                out.append(idx)
                out.append(hashMap[dif])
                break
            else:
                continue

    
        return sorted(out)