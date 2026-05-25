class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        res = [0] * len(temperatures)

        for idx, val in enumerate(temperatures):
            while stk and temperatures[stk[-1]] < val:
                res[stk[-1]] = idx - stk[-1]
                stk.pop()
            stk.append(idx)
        
        return res