class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = 0
        cars = sorted(zip(position, speed), reverse=True)
        min_time = 0

        for pos, spd in cars:
            time = (target - pos) / (spd)
            if time > min_time:
                fleet += 1
                min_time = time
            
        return fleet

