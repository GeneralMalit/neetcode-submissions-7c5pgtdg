class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        print(f"cars = {cars}")
        res = 0
        time = float("-inf")
        for pos, spd in cars:
            curr = (target - pos) / spd
            if curr > time:
                res += 1
                time = curr
        return res