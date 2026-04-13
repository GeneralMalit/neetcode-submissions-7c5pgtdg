from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.time = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time:
            self.time[key] = []
        self.time[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time:
            return ""
        res = ""
        values = self.time[key]
        print(f"values = {values}")
        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2
            if values[m][0] <= timestamp:
                res = values[m][1]
                l = m + 1
            else:
                r = m - 1

        return res
        
