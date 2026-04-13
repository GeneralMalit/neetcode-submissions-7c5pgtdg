class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maindict = {}
        for idx, val in enumerate(nums): 
            maindict[val] = idx #initialize dict, value: array index
        for idx, val in enumerate(nums):#for every element in the array:
            dif = target - val
            if dif in maindict and maindict[dif] != idx:
                return sorted([idx, maindict[dif]]) #if difference exists in the array, return indices of element and difference
            

        