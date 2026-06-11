class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = list(range(len(edges) + 1))
        size = [1] * (len(edges) + 1)

        def find(i):
            if par[i] != i:
                par[i] = find(par[i])

            return par[i]

        def union(u, v):
            r1, r2 = find(u), find(v)
            if r1 == r2:
                return False
            
            if size[r1] > size[r2]:
                size[r1] += r2
                par[r2] = r1
            else:
                size[r2] += r1
                par[r1] = r2
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]