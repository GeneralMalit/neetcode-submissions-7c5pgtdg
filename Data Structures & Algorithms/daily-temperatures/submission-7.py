class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for idx, val in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < val:
                popped = stack.pop()
                res[popped] = idx - popped 
            stack.append(idx)
        return res

