class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        res = [0] * len(temperatures)
        for idx, val in enumerate(temperatures):
            while stk and temperatures[stk[-1]] < val:
                i = stk.pop()
                res[i] = idx - i
            stk.append(idx)
        return res 