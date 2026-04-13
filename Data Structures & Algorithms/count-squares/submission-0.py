from collections import Counter
class CountSquares:

    def __init__(self):
        self.count_point = Counter()
        

    def add(self, point: List[int]) -> None:
        self.count_point[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        res = 0
        for (qx, qy), count in self.count_point.items():
            if abs(qx - x) != abs(qy - y) or qx - x == 0:
                continue
            res += count * self.count_point[(qx, y)] * self.count_point[(x, qy)]
        return res

