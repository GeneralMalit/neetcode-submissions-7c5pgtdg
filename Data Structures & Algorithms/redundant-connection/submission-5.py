class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = list(range(len(edges) + 1))
        size = [1] * (len(edges) + 1)
        def find(i):
            if par[i] != i:
                par[i] = find(par[i])
            return par[i]

        def union(u, v):
            par1, par2 = find(u), find(v)
            if par1 == par2:
                return False
            
            if size[par1] > size[par2]:
                size[par1] += par2
                par[par2] = par1
            else:
                size[par2] += par1
                par[par1] = par2
            return True


        for u, v in edges:
            if not union(u, v):
                return [u, v]