class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stk = []

        for i, t in enumerate(temperatures):
            while stk and t > temperatures[stk[-1]]:
                idx = stk.pop()
                ans[idx] = i - idx
            stk.append(i)
        return ans
