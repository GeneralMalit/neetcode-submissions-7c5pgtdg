class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        cars = sorted(zip(position, speed), reverse=True)
        
        maxtime = float("-inf")
        for p, s in cars:
            time = (target - p)/s
            if time > maxtime:
                res += 1
                maxtime = max(maxtime, time)
        return res
