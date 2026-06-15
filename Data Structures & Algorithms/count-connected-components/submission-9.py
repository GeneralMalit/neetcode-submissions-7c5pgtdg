class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = list(range(n))
        def find(i):
            if i != par[i]:
                par[i] = find(par[i])
            return par[i]
        def union(u, v):
            par1, par2 = find(u), find(v)
            if par1 != par2:
                par[par2] = par1
                return 1
            return 0

        count = n
        for u, v in edges:
            count -= union(u, v)
        return count