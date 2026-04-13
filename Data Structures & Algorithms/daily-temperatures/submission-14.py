from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = collections.deque()
        res = [0] * len(temperatures)
        for idx, val in enumerate(temperatures):
            while stk and stk[-1][0] < val:
                res[stk[-1][1]] = idx - stk[-1][1]
                stk.pop()

            stk.append([val, idx])
        return res