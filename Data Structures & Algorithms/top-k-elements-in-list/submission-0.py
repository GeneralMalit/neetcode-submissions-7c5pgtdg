class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # first solution that i think of is hash table 
        thedict = dict()
        newarr = []
        
        for i in nums:
            if i not in thedict:
                thedict[i] = 1
            else:
                thedict[i] += 1
        for x,y in thedict.items():  
            newarr.append([x, y])
        newarr.sort(key=lambda arr:arr[1], reverse=True)
        out = []
        for i in range(k):
            out.append(newarr[i][0])
        return out