from collections import Counter
class CountSquares:

    def __init__(self):
        self.counts = Counter()
    def add(self, point: List[int]) -> None:
        self.counts[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        res = 0

        for (qx, qy), count in self.counts.items():
            if abs(qx - x) != abs(qy - y) or (qx - x) == 0:
                continue
            res += count * self.counts[(qx, y)] * self.counts[(x, qy)]
        return res