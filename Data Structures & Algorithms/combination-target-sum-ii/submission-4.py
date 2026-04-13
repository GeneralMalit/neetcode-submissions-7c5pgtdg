class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(idx, s, remaining):
            if remaining == 0:
                res.append(s[:])

            if remaining < 0:
                return

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i - 1] == candidates[i]:
                    continue
                
                s.append(candidates[i])
                backtrack(i + 1, s, remaining - candidates[i])
                s.pop()

        
        backtrack(0, [], target)
        return res
