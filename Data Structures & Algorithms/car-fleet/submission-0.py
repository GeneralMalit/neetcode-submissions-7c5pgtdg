class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = sorted(zip(position, speed), reverse=True)

        fleets = 0
        curr_slowest = 0

        for p, s in times:
            curr = (target - p) / s
            if curr > curr_slowest:
                fleets += 1
                curr_slowest = curr
        return fleets