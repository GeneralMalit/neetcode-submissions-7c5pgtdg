class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, remaining, s):
            if remaining == 0:
                res.append(s[:])
            if remaining < 0:
                return 
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                
                s.append(candidates[j])
                dfs(j + 1, remaining - candidates[j], s)
                s.pop()
        dfs(0, target, [])
        return res