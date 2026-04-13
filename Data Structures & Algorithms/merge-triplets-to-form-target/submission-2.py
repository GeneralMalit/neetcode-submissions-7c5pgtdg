class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = set()
        for x, y, z in triplets:
            if x > target[0] or y > target[1] or z > target[2]:
                continue
            
            if x == target[0]:
                found.add(0)
            if y == target[1]:
                found.add(1)

            if z == target[2]:
                found.add(2)
        return len(found) == 3