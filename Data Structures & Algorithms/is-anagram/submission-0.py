class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        collection = {} #we are using a dict for this one
        for i in s:
            if i not in collection:
                collection[i] = 1
                continue
            collection[i] += 1
        for i in t:
            if i not in collection:
                return False
            else:
                collection[i] -= 1
                if collection[i] < 0:
                    return False
        x = collection.values()
        for i in x:
            if i != 0:
                return False
        return True
            


