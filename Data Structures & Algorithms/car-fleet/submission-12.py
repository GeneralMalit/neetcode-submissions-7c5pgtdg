class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([i for i in zip(position, speed)], reverse=True)
        fleet = 0

        maxTime = 0

        for i in cars:
            time = (target - i[0]) / i[1]
            if time > maxTime:
                fleet += 1
                maxTime = time
            
        
        return fleet