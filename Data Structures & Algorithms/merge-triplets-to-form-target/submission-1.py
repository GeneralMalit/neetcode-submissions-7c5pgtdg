class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ok = set()
        for x, y, z in triplets:
            if x > target[0] or y > target[1] or z > target[2]:
                continue


            if x == target[0]:
                ok.add(0)
            if y == target[1]:
                ok.add(1)
            if z == target[2]:
                ok.add(2)
                
        return len(ok) == 3