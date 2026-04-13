class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = []
        line = sorted(zip(position, speed), reverse=True)
        time = float('-inf')
        groups = 0
        for i in line:
            group = []
            taken = (target - i[0]) / i[1]
            if taken > time:
                groups += 1
                time = taken
        return groups

            
            


        return res