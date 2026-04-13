class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stk = []

        for idx, val in enumerate(temperatures):
            while stk and temperatures[stk[-1]] < val:
                upd = stk.pop()
                res[upd] = idx - upd
            stk.append(idx)
        
        return res
