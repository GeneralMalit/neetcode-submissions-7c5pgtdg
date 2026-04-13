class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos = sorted(zip(position, speed))
        car_fleet = 0
        print(f"pos = {pos}")
        #s = d / t
        slowest = 0
        while pos:
            p, s = pos.pop()
            time = (target - p) / s
            if time > slowest:
                slowest = time
                car_fleet += 1
        return car_fleet

            